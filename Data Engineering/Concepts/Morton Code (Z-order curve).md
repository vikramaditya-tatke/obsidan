---
tags:
  - data-engineering
  - spatial
  - algorithms
  - clickhouse
---

## Morton Code (Z-order curve)

### 1. Technical Definition

A **Morton Code** (or Z-order curve) is a space-filling curve that maps multidimensional data (e.g., 2D latitude/longitude) into a single dimension (an integer) while preserving **locality of reference**.

**Why it matters:** In database terms, it reduces a multi-dimensional range query (e.g., "points within this bounding box") into a set of 1D interval scans.
* **Without Morton:** Sorting by Latitude alone means points with the same latitude (e.g., London and Vancouver) are stored together, even if they are thousands of miles apart in Longitude. A query for "London" would scan mostly irrelevant data.
* **With Morton:** Points are sorted by their interleaved bits, meaning "London" is stored physically next to "Oxford" and "Reading". A bounding box query becomes a series of efficient range scans.

### 2. Implementation: Bit Interleaving

The core operation is **bit-interleaving**. While conceptually "shuffling cards," efficient implementations use **Magic Numbers** (bit masks) to "spread" the bits of each coordinate in `O(1)` time before combining them.

#### Python Implementation (Magic Numbers)

This function interleaves the bits of a 32-bit integer `x` to create a 64-bit sequence with gaps for `y`.

```python
def part1_by1(n):
    """
    Inserts a 0 bit after each bit of n.
    Example: 1111 -> 01010101
    """
    n &= 0x0000ffff
    n = (n | (n << 16)) & 0x0000ffff0000ffff
    n = (n | (n << 8))  & 0x00ff00ff00ff00ff
    n = (n | (n << 4))  & 0x0f0f0f0f0f0f0f0f
    n = (n | (n << 2))  & 0x3333333333333333
    n = (n | (n << 1))  & 0x5555555555555555
    return n

def morton_encode(x, y):
    """
    Interleaves bits of x and y to produce a Z-order curve index.
    """
    return (part1_by1(y) << 1) + part1_by1(x)
```

### 3. Web Mercator (EPSG:3857)

To use Morton Codes for geospatial data, we first need to project the spherical Earth onto a flat, integer-friendly grid. **Web Mercator** is the standard projection for this task.****

#### What is It?
**Web Mercator (EPSG:3857)** is a variant of the Mercator projection used by virtually all web mapping services (Google Maps, OpenStreetMap, Bing Maps). It simplifies the earth's shape to a perfect sphere to make calculations faster.

#### Why is it Used Here?

Morton Codes and Quadtrees require a **square coordinate system** to work perfectly.

1. **The "Square World"**: Web Mercator projects the world onto a perfect square (cutting off the poles at ~85.05° latitude).
2. **Integer Mapping**: This square can be easily mapped to a binary integer grid (e.g., `0` to `4,294,967,295`).
3. **Tiling Compatibility**: It aligns perfectly with standard XYZ tile schemes (Zoom/X/Y). A Z-order curve traversing this grid visits every tile in a quadtree hierarchically.

### 4. ClickHouse Implementation

In ClickHouse, Morton codes are used to sort data physically on disk (Primary Key), ensuring that points geographically close are stored in the same or adjacent blocks.

#### The `mortonEncode` Function

ClickHouse provides a native function `mortonEncode(x, y)`.

#### Example: Optimizing OpenStreetMap (OSM) Data

We use the Web Mercator logic to convert **Float (Lat/Lon)** to **UInt32** integers before encoding.

```sql
CREATE TABLE planes_mercator
(
    -- 1. Project Lat/Lon (EPSG:4326) to Web Mercator Integers
    -- Normalizes the world to a 0-1 range, then scales to full UInt32
    mercator_x UInt32 MATERIALIZED 0xFFFFFFFF * ((lon + 180) / 360),
    mercator_y UInt32 MATERIALIZED 0xFFFFFFFF * (1/2 - log(tan((lat + 90) / 360 * pi())) / 2 / pi()),

    time DateTime64(3),
    icao String,
    lat Float64,
    lon Float64,
    
    -- 2. Use MinMax indexes for pre-filtering (Skips huge chunks of data)
    INDEX idx_x (mercator_x) TYPE minmax,
    INDEX idx_y (mercator_y) TYPE minmax
) 
ENGINE = MergeTree
-- 3. Order by the Z-Order Curve (Physical Locality)
ORDER BY (mortonEncode(mercator_x, mercator_y), time);
```

**Deconstructing the Math:**
* `lon + 180 / 360`: Normalizes Longitude from `[-180, 180]` to `[0, 1]`.
* `1/2 - log(...)`: The Web Mercator formula for Latitude, normalized to `[0, 1]`.
* `0xFFFFFFFF * ...`: Scales the `[0, 1]` float to the full 32-bit integer space (`0` to `2^32-1`). This gives us the highest possible precision for the Z-curve interleaving.

### 5. Schema Design: Map vs. Tuple

When storing semi-structured data like OSM tags (`highway=primary`, `maxspeed=50`), the choice of data type impacts performance and flexibility.

#### Comparison

| Feature | `Map(String, String)` | `Tuple(...)` |
| :--- | :--- | :--- |
| **Structure** | **Flexible** (Keys defined at runtime) | **Rigid** (Order/Type defined at DDL) |
| **Query Style** | `tags['highway']` | `tuple.1` (by position) |
| **Indexing** | Supports **Bloom Filters** (Tokenbf) | Fast scan, hard to index specific keys |
| **Use Case** | **OSM Tags** (sparse, variable schema) | **Fixed Coordinates** (e.g., `Point(x, y)`) |

#### Recommendation

Use **Map** for tags. While slightly slower than dedicated columns, it allows querying any arbitrary tag key without schema migrations.

```sql
-- Example Query on Map
SELECT count() 
FROM osm_nodes 
WHERE tags['highway'] = 'traffic_signals'
```
