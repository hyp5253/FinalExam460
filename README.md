# The Torchbearer

**Student Name:** Husain Patanwala
**Student ID:** 130533998
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  _SSP from S only tells us minimum cost from source to a node. It is not enough because it doesn't tell us the shortest distance from an intermediate node to another target node._

- **What decision remains after all inter-location costs are known:**
  _We still have to choose in what order to visit all the nodes to minimize cost._

- **Why this requires a search over orders (one sentence):**
  _Must try all possible orderings to find order that visits all relic chambers in set M and minimizes fuel burned._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source                                                |
|------------------|-------------------------------------------------------------------|
| _Dungeon Entry_  | _Must enter the dungeon throught this node._                      |
| _Relic Chamber_  | _Must figure out min distance from one chamber room to the next._ |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer                      |
|---|----------------------------------|
| Data structure name | dictionary                       |
| What the keys represent | source node                      |
| What the values represent | dict of dest mapped to min cost  |
| Lookup time complexity | O(1)                             |
| Why O(1) lookup is possible | hashed keys are mapped to values |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _k+1_
- **Cost per run:** _O(mlogn) -> n=|V|, m=|E|, k=|M|_
- **Total complexity:** _O((k+1)mlogn)_
- **Justification (one line):** _Each run of SSP costs O(mlogn) and we need to run k+1 times to cover all relic chambers and source node._

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _We have found a series of nodes whose sum of edges from src to dest is the shortest possible._

- **For nodes not yet finalized (not in S):**
  _Still building our overall shortest path to dest and storing our shortest path so far to an intermediate node from src._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Distance to source is always 0 (possible shortest path). No other nodes have been reached or explored, so they are not in S._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Assuming no negative edges and if we use a min heap, we always pop off and take the smallest edge (a local choice). Optimal substructure let's our local choices to intermediate nodes build overall optimal solution._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _Your answer here._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Your answer here._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
