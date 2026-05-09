"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: ___________________________
Student ID:   ___________________________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq

# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """

    answer = """
    SSP from S only tells us minimum cost from source to a node. It is not enough because it doesn't tell us the shortest distance from an intermediate node to another target node.
    We still have to choose in what order to visit all the nodes to minimize cost.
    Must try all possible orderings to find order that visits all relic chambers in set M and minimizes fuel burned.
    """

    return answer


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    """
    # couldn't our entry point be a relic chamber?
    # also if we start out with, and we want to check if there is a dupe we'd need to traverse at most N elements
    # instead just add to set which can't have dupes then convert to list

    sources = set()
    sources.add(spawn)

    # also technically the exit node could be a relic chamber but
    # that means that it'll be added through this relic iteration sequence
    for relic in relics: sources.add(relic)

    return list(sources)


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    """
    # the graph is already in the form of an adjacency list
    # no need to convert from edge list -> adj list

    # the number of keys is how many nodes we have in the graph
    n = len(graph.keys())
    INF = float("inf")

    # can't index these nodes we can use a dict to map node -> best so far
    best_so_far = { node : INF for node in graph.keys() }
    
    best_so_far[source] = 0
    # we want to the heap to have min cost on top so do tuple of
    # (cost, node)
    heap = [(0, source)]
    
    while heap:
        fuel_burned, u = heapq.heappop(heap)
        
        # we don't want to store anything worse
        if fuel_burned > best_so_far[u]: continue
        
        for v, fuel_cost_to_v in graph[u]:
            cost_to_v_from_u = fuel_burned + fuel_cost_to_v
            
            if cost_to_v_from_u < best_so_far[v]:
                best_so_far[v] = cost_to_v_from_u
                # we want to explore paths to other nodes from this better one
                heapq.heappush(heap, (cost_to_v_from_u, v))

    return best_so_far


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    precomputed = {}
    sources = select_sources(spawn, relics, exit_node)

    for src in sources:
        costs = run_dijkstra(graph, src)
        precomputed[src] = costs

    return precomputed

# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return "TODO"


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return "TODO"


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    current_loc = spawn
    relics_visited_order = []
    remaining_relics = set(relics)
    cost_so_far = 0
    best = [float('inf'), []]

    _explore(dist_table, current_loc, remaining_relics, relics_visited_order, cost_so_far, exit_node, best)
    return tuple(best)

def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """

    # base case if we have reached all relic chambers
    def _goal() -> bool:
        if not relics_remaining and dist_table[current_loc][exit_node] != float("inf"):
            return True
        return False

    best_cost = best[0]
    total_cost = cost_so_far + dist_table[current_loc][exit_node]
    if _goal() and total_cost < best_cost:
        best[0] = total_cost
        best[1] = relics_visited_order.copy()
        return
    if cost_so_far >= best_cost: # this is the pruning thing
        return
    for r in relics_remaining.copy():
        if dist_table[current_loc][r] != float("inf"):
            # make choice
            relics_remaining.remove(r)
            relics_visited_order.append(r)
            cost_so_far += dist_table[current_loc][r]
            # recursive call
            _explore(dist_table, r, relics_remaining, relics_visited_order, cost_so_far, exit_node, best)
            # undo choice
            cost_so_far -= dist_table[current_loc][r]
            relics_visited_order.pop()
            relics_remaining.add(r)


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    result = find_optimal_route(dist_table, spawn, relics, exit_node)
    return result


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
