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
- **Justification (one line):** _Each run of SSP costs O(mlogn) and we need to run k+1 times to cover all relic chambers and spawn node._

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _We have found a series of nodes whose sum of edges from X to node V is the shortest possible._

- **For nodes not yet finalized (not in S):**
  _We have stored the shortest path from X to U, and the nodes in the path from X to U are in already S (building optimal solution from local greedy decisions)._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Distance to X is always 0 (possible shortest path). No other nodes have been reached or explored, so they are not in S (distance is not yet finalized)._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _If we use a min heap, we always pop off and take the smallest edge (a local choice). Because non-negative edges, we can't ever locally choose a larger value first, and end up with a better lesser costing path._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _All reachable nodes will be finalized and part of set S, meaning that the distance to each V from X is the shortest possible._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_To minimize total fuel burned, we must select the shortest route from current to next viable node (relic or exit)._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

### My Concrete Illustration
**Entrance:** S | **Relic chambers:** B, C, D | **Exit:** T

After computing cheapest inter-location travel costs, suppose you have:

| From \ To | B  | C   | D   | T   |
|-----------|----|-----|-----|-----|
| S         | 1  | 2   | 2   | --  |
| B         | -- | 100 | 20  | 10  |
| C         | 1  | --  | 100 | 20  |
| D         | 1  | 10  | --  | 100 |

Two possible routes:

- Greedy Route: S -> B -> D -> C -> T &nbsp; total fuel = 1 + 20 + 10 + 20 = **51**
- Optimal Route: S -> D -> C -> B -> T &nbsp; total fuel = 2 + 10 + 1 + 10= **23**

Both collect every relic. Both end at T. Their total costs differ. Knowing cheapest
point-to-point travel costs alone does not tell you which collection order is optimal.

- **The failure mode:** _Chooses the next closest relic chamber (aka the least costing fuel path)._
- **Counter-example setup:** _Check illustration above..._
- **What greedy picks:** _Always choose the cheapest fuel route without looking ahead._
- **What optimal picks:** _May choose a more expensive fuel route, that decrease total fuel burned._
- **Why greedy loses:** _Doesn't look ahead or consider other alternatives, and only cares about local best option._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _The best permutation (aka order of nodes) that minimizes fuel burned, visits all relic chambers, and starts and ends at the desginated nodes._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description                                                             |
|---|-----------------------|-----------|-------------------------------------------------------------------------|
| Current location | current_loc           | char      | represents the room we are currently at                                 |
| Relics already collected | relics_visited_order  | list      | tracks the relics we have selected along this path in our decision tree |
| Fuel cost so far | cost_so_far           | float     | tracks total fuel burned so far on this route                           |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer                                                                |
|---|----------------------------------------------------------------------------|
| Data structure chosen | set                                                                        |
| Operation: check if relic already collected | Time complexity: O(1)                                                      |
| Operation: mark a relic as collected | Time complexity: O(1)                                                      |
| Operation: unmark a relic (backtrack) | Time complexity: O(1)                                                      |
| Why this structure fits | Ensures unique elements, and allows for fast inserts, checks, and removals |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _(k)(k-1)(k-2)...(1) = k!_
- **Why:** _Spawn and exit are fixed, but we do need to permute the internal k relic chambers, so we then get k! possibilities._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _The best or least costing fuel path to a node._
- **When it is used:** _When deciding to continue exploring a path from a certain node._
- **What it allows the algorithm to skip:** _Any path that would give us a worse or less efficient fuel path._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Current location, relics visited order, remaining relics, best order found and associated fuel cost, current fuel cost._
- **What the lower bound accounts for:** _._
- **Why it never overestimates:** _._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _lecture notes_
- _https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/e54e0c08cfb4234858e90c9c24351321_MIT6_046JS12_lec06.pdf_
- _https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/312f4a419009b58f8147b75975db4347_MIT6_046JS15_lec11.pdf_
- _https://www.cs.cmu.edu/afs/cs/academic/class/15210-s15/www/lectures/shortest-paths-notes.pdf_
- _https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1262/lectures/11-backtracking1/_
