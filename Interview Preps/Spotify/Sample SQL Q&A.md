#### Sources:

- [[Rewrite as tweet]]
- [[Rewrite as tweet thread]]
- [[Questions for the Hiring Manager]]## **1. Find the earliest date each user played their third unique song**
```sql
WITH song_ranks AS (
    SELECT
        user_id,
        song_id,
        play_time,
        ROW_NUMBER() OVER (PARTITION BY user_id, song_id ORDER BY play_time) AS rn
    FROM plays
),
unique_songs AS (
    SELECT
        user_id,
        song_id,
        MIN(play_time) AS first_play_time
    FROM song_ranks
    WHERE rn = 1
    GROUP BY user_id, song_id
),
song_counts AS (
    SELECT
        user_id,
        song_id,
        first_play_time,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY first_play_time) AS song_order
    FROM unique_songs
)
SELECT
    user_id,
    first_play_time AS third_song_play_time
FROM song_counts
WHERE song_order = 3;

```

---

## **2. Top 10 Songs Using Windowing Types**

### **a. Global Window – All Time Top 10 Songs**

```sql
SELECT
    song_id,
    COUNT(*) AS play_count
FROM plays
GROUP BY song_id
ORDER BY play_count DESC
LIMIT 10;
```

---

### **b. Tumbling Window – Top 10 Songs in Fixed 1-Week Intervals**

```sql
WITH week_window AS (
    SELECT
        song_id,
        DATE_TRUNC('week', play_time) AS week,
        COUNT(*) AS play_count
    FROM plays
    GROUP BY song_id, DATE_TRUNC('week', play_time)
),
ranked_songs AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY week ORDER BY play_count DESC) AS rnk
    FROM week_window
)
SELECT *
FROM ranked_songs
WHERE rnk <= 10;

```

---

### **c. Sliding Window – Top 10 Songs Over Rolling 7-Day Period**

> Note: This is compute-intensive and might not be supported in all SQL engines. Assume `play_date` is a truncated version of `play_time`.

```sql
WITH dates AS (
    SELECT DISTINCT DATE(play_time) AS play_date FROM plays
),
daily_counts AS (
    SELECT
        d.play_date,
        p.song_id,
        COUNT(*) AS play_count
    FROM dates d
    JOIN plays p ON DATE(p.play_time) BETWEEN d.play_date - INTERVAL '6 days' AND d.play_date
    GROUP BY d.play_date, p.song_id
),
ranked AS (
    SELECT
        play_date,
        song_id,
        play_count,
        ROW_NUMBER() OVER (PARTITION BY play_date ORDER BY play_count DESC) AS rnk
    FROM daily_counts
)
SELECT *
FROM ranked
WHERE rnk <= 10;

```

---

### **d. Session Window – Top 10 Songs per User Session**

Assume a session is defined as 30+ minutes of inactivity ending a session.

```sql
WITH sessions AS (
    SELECT
        *,
        CASE 
            WHEN EXTRACT(EPOCH FROM (play_time - LAG(play_time) OVER (PARTITION BY user_id ORDER BY play_time))) > 1800 
            OR LAG(play_time) OVER (PARTITION BY user_id ORDER BY play_time) IS NULL
            THEN 1 ELSE 0 
        END AS new_session
    FROM plays
),
session_groups AS (
    SELECT
        *,
        SUM(new_session) OVER (PARTITION BY user_id ORDER BY play_time) AS session_id
    FROM sessions
),
session_song_counts AS (
    SELECT
        user_id,
        session_id,
        song_id,
        COUNT(*) AS song_count
    FROM session_groups
    GROUP BY user_id, session_id, song_id
),
ranked_sessions AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY user_id, session_id ORDER BY song_count DESC) AS rnk
    FROM session_song_counts
)
SELECT *
FROM ranked_sessions
WHERE rnk <= 10;

```

---

## **3. Find Users Who Listened to >100 Songs in Any Week**

```sql
WITH weekly_counts AS (
    SELECT
        user_id,
        DATE_TRUNC('week', play_time) AS week_start,
        COUNT(*) AS song_count
    FROM plays
    GROUP BY user_id, DATE_TRUNC('week', play_time)
)
SELECT user_id, week_start, song_count
FROM weekly_counts
WHERE song_count > 100;

```
