---
aliases:
tags:
  - algorithms
created_at: 2026-04-10T23:14:00
title: Preparation Plan
description:
---
## Active Recall

##### 1. Does it involve a range?
##### 2. Does it involve heirarchy or paths?

## Data Structures

| **No.** | **Data Structure**        | **Best Used For...**                              | **Key Property**                       |
| ------- | ------------------------- | ------------------------------------------------- | -------------------------------------- |
| 1       | **Hash Map / Set**        | Instant lookups and counting.                     | $O(1)$ average search time.            |
| 2       | **Stack**                 | Undo operations, recursion, and nested logic.     | LIFO (Last-In, First-Out).             |
| 3       | **Queue**                 | Processing tasks in order, level-by-level search. | FIFO (First-In, First-Out).            |
| 4       | **Heap (Priority Queue)** | Finding the "best" (min/max) element quickly.     | $O(1)$ to find, $O(\log n)$ to remove. |
| 5       | **Tree (BST / Trie)**     | Hierarchical data and prefix searching.           | Logarithmic height (usually).          |
| 6       | **Graph**                 | Representing networks or connections.             | Nodes and Edges.                       |

## Programming Patterns
### A. Linear Patterns (Arrays, Strings, Lists)

- **Two Pointers:** Moving from both ends or at different speeds to find a pair or partition.
- **Sliding Window:** Maintaining a sub-section of data to find a maximum or minimum range.
- **Prefix Sum:** Pre-calculating sums to answer range-sum queries in O(1).
- **Monotonic Stack:** Using a stack to find the "next greater" or "previous smaller" element.

### B. Search & Optimization Patterns

- **Binary Search:** Efficiently narrowing down a sorted search space.
- **Breadth-First Search (BFS):** Layer-by-layer exploration (Shortest path).
- **Depth-First Search (DFS):** Exhaustive branch exploration (Pathfinding).
- **Backtracking:** Trying all possibilities but "pruning" paths that fail.

### C. Advanced Logic Patterns

- **Dynamic Programming (DP):** Breaking a problem into sub-problems and storing results (Memoization).
- **Greedy:** Making the locally optimal choice at each step to find a global optimum.
- **Topological Sort:** Ordering tasks that have dependencies (e.g., Course Schedule).


