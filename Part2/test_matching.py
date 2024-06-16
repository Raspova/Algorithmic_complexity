import networkx as nx
from main import greedy_matching_based_on_degree, random_matching

def test_matching(graph, matching):
    matched_nodes = set()
    for u, v in matching:
        assert u in graph
        assert v in graph
        assert (u, v) in graph.edges or (v, u) in graph.edges
        assert u not in matched_nodes
        assert v not in matched_nodes
        matched_nodes.add(u)
        matched_nodes.add(v)
    print("All matchings are correct")

# Example test
graph = nx.gnp_random_graph(120, 0.04)
matching = greedy_matching_based_on_degree(graph)
test_matching(graph, matching)

matching = random_matching(graph)
test_matching(graph, matching)