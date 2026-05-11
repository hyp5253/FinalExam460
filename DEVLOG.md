# Development Log – The Torchbearer

**Student Name:** Husain Patanwala
**Student ID:** 130533998

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – May 6th: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_It took me a while to try and figure out what the problem was asking of me.
I first plan to implement all of the smaller helper functions, like a single
dijkstra run and getting proper data structures set up. I plan to test by 
using the provided test cases, but also creating my own intermediate mini cases -
either print testing or if I have time unit tests. What I expect to be the most
difficult is finding the correct permutation that gives the min cost._

---

## Entry 2 – May 8th: Proofing and Design and Begin coding solution

_Worked on the invariant proofs, and created a counter example to prove why greedy
fails in comparison the optimal solution. I also have started hashing out the 
actual code solution._

---

## Entry 3 – May 9th: Defining the goal state

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_I assumed that we have reached our base case, aka the goal state if all the remaining relics are used.
However, I realized that because it's a directed graph, we also need to make sure that if we have reached 
all relic chambers, we need to have a path from our current location to the exit, and if not we have to 
discard this path. I resolved this problem by including a check in my goal function to see if we have visited
all chambers, and are not at the exit node, that we have a route to the exit._

---

## Entry 4 – May 10th: Explain state and pruning complexities

_I started to fill out the necessary answers in the README, but I felt that my language was too vague. So I 
had to make sure to properly articulate my answers especially in the pruning and state sections. _

---

## Entry 5 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|-----------------|
| Part 1: Problem Analysis | 2.5             |
| Part 2: Precomputation Design | 1               |
| Part 3: Algorithm Correctness | 1.5             |
| Part 4: Search Design | 1               |
| Part 5: State and Search Space | 2               |
| Part 6: Pruning | 1.5             |
| Part 7: Implementation | 1.5              |
| README and DEVLOG writing |                 |
| **Total** |                 |
