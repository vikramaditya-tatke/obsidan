# Summary: Designing Data-Intensive Applications
**Author:** Martin Kleppmann

This summary covers the fundamental principles, algorithms, and trade-offs involved in designing data systems that are reliable, scalable, and maintainable.

---

## Part I: Foundations of Data Systems

This part establishes the vocabulary and fundamental concepts used throughout the book.

### Chapter 1: Reliable, Scalable, and Maintainable Applications

Applications must meet various requirements, categorized into:
*   **Reliability:** The system should continue to work correctly (performing the correct function at the desired level of performance) even in the face of adversity (hardware or software faults, and even human error).
    *   *Faults vs. Failures:* Faults are deviations from spec in components; failures are when the system as a whole stops providing service. We design for fault tolerance.
*   **Scalability:** As the system grows (in data volume, traffic volume, or complexity), there should be reasonable ways of dealing with that growth.
    *   *Load Parameters:* Describing load (e.g., requests/sec, read/write ratio).
    *   *Performance:* Latency (duration) vs. Response Time (client perspective). Tail latency (p95, p99) is critical for user experience.
*   **Maintainability:** Over time, many different people will work on the system, and they should all be able to work on it productively.
    *   *Operability:* Making life easy for operations teams.
    *   *Simplicity:* Managing complexity (removing accidental complexity).
    *   *Evolvability:* Making change easy.

### Chapter 2: Data Models and Query Languages

Data models have a profound effect on how software is written.
*   **Relational Model (SQL):** Data organized into relations (tables) of tuples (rows). Dominant for business data processing. Hides implementation details behind a clean interface.
*   **Document Model (NoSQL):** Targets use cases where data comes in self-contained documents and relationships are rare. Offers schema flexibility (schema-on-read) and better locality for document-like structures.
*   **Graph-Like Data Models:** Best for data with many-to-many relationships.
    *   *Property Graphs:* Vertices and edges with properties (e.g., Neo4j, Cypher).
    *   *Triple-Stores:* Subject-predicate-object triples (e.g., SPARQL, RDF).
    *   *Datalog:* Foundation for later query languages.

### Chapter 3: Storage and Retrieval

How databases store data on disk and find it again.
*   **Log-Structured Storage:** Append-only files.
    *   *SSTables (Sorted String Tables):* Key-value pairs sorted by key.
    *   *LSM-Trees (Log-Structured Merge-Trees):* Built on SSTables. Writes are fast (sequential). Used in LevelDB, RocksDB, Cassandra, HBase, Lucene.
*   **Page-Oriented Storage:**
    *   *B-Trees:* Break database into fixed-size pages. The standard for relational databases. Good for reads.
*   **OLTP vs. OLAP:**
    *   *OLTP (Online Transaction Processing):* Interactive, small queries, random access. Row-oriented storage.
    *   *OLAP (Online Analytic Processing):* Data warehousing, large scans, aggregates. Column-oriented storage (better compression, vectorized processing).

### Chapter 4: Encoding and Evolution

How data is represented when written to files or sent over the network.
*   **Formats:**
    *   *Textual:* JSON, XML, CSV (human-readable, but verbose and vague on types).
    *   *Binary:* Thrift, Protocol Buffers, Avro. Compact, efficient, require schemas.
*   **Schema Evolution:**
    *   *Backward compatibility:* New code can read old data.
    *   *Forward compatibility:* Old code can read new data.
*   **Dataflow Modes:**
    *   *Databases:* Process writing encodes, process reading decodes.
    *   *Service Calls (REST/RPC):* Client encodes request, server decodes; server encodes response, client decodes.
    *   *Message Passing:* Asynchronous message brokers (e.g., Kafka, RabbitMQ).

---

## Part II: Distributed Data

Moving from single-node to multi-node systems for scalability, fault tolerance, and latency.

### Chapter 5: Replication

Keeping a copy of the same data on multiple nodes.
*   **Leader-Based Replication (Active/Passive):**
    *   One leader accepts writes; followers replicate the leader's log.
    *   *Synchronous vs. Asynchronous:* Trade-off between durability and latency/availability.
    *   *Replication Logs:* Statement-based, WAL shipping, Logical (Row-based) log.
*   **Replication Lag & Consistency:**
    *   *Read-your-writes:* Users see their own updates.
    *   *Monotonic reads:* Users don't see things move backward in time.
    *   *Consistent prefix reads:* Preserves causal ordering.
*   **Multi-Leader Replication:**
    *   More than one node accepts writes. Good for multi-datacenter or offline clients.
    *   *Conflict Resolution:* Last-Write-Wins (LWW), merging values, custom logic.
*   **Leaderless Replication (Dynamo-style):**
    *   Client sends writes to multiple nodes.
    *   *Quorums:* Read/Write quorums (w + r > n) to ensure overlap.
    *   *Repair:* Read repair and anti-entropy.

### Chapter 6: Partitioning

Splitting a large dataset into smaller subsets (shards).
*   **Partitioning Strategies:**
    *   *Key Range:* Assigns continuous ranges of keys. Efficient for range queries but risks hot spots.
    *   *Hash of Key:* Distributes load evenly but destroys ordering (no efficient range queries).
*   **Secondary Indexes:**
    *   *Document-Partitioned (Local):* Each partition manages its own index. Reads need scatter/gather.
    *   *Term-Partitioned (Global):* Index covers all data but is itself partitioned. Reads are efficient, writes are complex/slow.
*   **Rebalancing:** Moving load between nodes. Dynamic partitioning, fixed number of partitions.

### Chapter 7: Transactions

Grouping operations into logical units to simplify error handling and concurrency.
*   **ACID:** Atomicity (abortability), Consistency (application invariant), Isolation (concurrency control), Durability (storage).
*   **Isolation Levels:**
    *   *Read Committed:* No dirty reads, no dirty writes.
    *   *Snapshot Isolation (Repeatable Read):* Readers read from a consistent snapshot (MVCC). Prevents read skew.
    *   *Serializable:* Strongest isolation. Prevents all race conditions (including write skew and phantoms). Implemented via 2PL (Two-Phase Locking), Serial execution, or SSI (Serializable Snapshot Isolation).

### Chapter 8: The Trouble with Distributed Systems

The reality of partial failures in shared-nothing systems.
*   **Unreliable Networks:** Packets can be lost, delayed, or reordered. No upper bound on delay.
*   **Unreliable Clocks:** Time-of-day clocks (NTP) subject to skew and jumps. Monotonic clocks better for durations.
*   **Process Pauses:** GC pauses, virtual machine suspension.
*   **Truth & Lies:** A node cannot trust itself. Truth is defined by the majority (quorum). Fencing tokens prevent "zombie" leaders from causing corruption.

### Chapter 9: Consistency and Consensus

Building fault-tolerant abstractions.
*   **Linearizability:** Recency guarantee. System appears as a single copy of data.
*   **Ordering:** Causal ordering vs. Total ordering. Lamport timestamps.
*   **Total Order Broadcast:** Reliable delivery of messages in the same order to all nodes.
*   **Consensus:** Getting nodes to agree on a value.
    *   *FLP Result:* Consensus impossible in asynchronous model if nodes crash (theoretical limit).
    *   *Algorithms:* Paxos, Raft, Zab, VSR. Solve consensus using quorums and leader election.
    *   *Distributed Transactions:* Two-Phase Commit (2PC) is a blocking atomic commit protocol.

---

## Part III: Derived Data

Integrating multiple systems into a coherent architecture.

### Chapter 10: Batch Processing

Processing a large amount of bounded input data to produce output.
*   **MapReduce:**
    *   *Map:* Extract key-value pairs.
    *   *Shuffle:* Sort and group by key.
    *   *Reduce:* Process grouped values.
    *   Distributed filesystem (HDFS) acts as the glue.
*   **Joins:** Sort-merge joins, broadcast hash joins, partitioned hash joins.
*   **Dataflow Engines:** Spark, Flink, Tez. Optimization over MapReduce by avoiding materialization of intermediate state (using memory/network instead of disk).

### Chapter 11: Stream Processing

Processing unbounded streams of events.
*   **Messaging:**
    *   *Message Brokers:* AMQP/JMS (transient, consumer acknowledgement) vs. Log-based (Kafka - durable, replayable, consumer offsets).
*   **Processing:**
    *   *Complex Event Processing (CEP):* Searching for patterns.
    *   *Stream Analytics:* Aggregations over windows (Tumbling, Hopping, Sliding, Session).
*   **Time:** Event time vs. Processing time. Handling stragglers (watermarks).
*   **Fault Tolerance:** Exactly-once semantics (idempotence, atomic commit).

### Chapter 12: The Future of Data Systems

Synthesis and vision for the future.
*   **Data Integration:** No single tool fits all needs. Composing specialized tools (unbundling databases).
*   **Change Data Capture (CDC):** Unbinding the database write log to drive derived data systems (indexes, caches).
*   **Event Sourcing:** Modeling state changes as an immutable log of events.
*   **Lambda Architecture:** Combining batch and stream processing (now largely superseded by unified engines like Flink/Beam).
*   **Ethics:** Responsibility of engineers regarding privacy, bias, and the societal impact of data systems.
