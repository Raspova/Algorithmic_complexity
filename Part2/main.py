import networkx as nx
import random
import time
import matplotlib.pyplot as plt

def greedy_matching_based_on_degree(graph):
    nodes = sorted(graph.degree, key=lambda x: x[1], reverse=True)
    matched = set()
    matching = []

    for node, _ in nodes:
        if node not in matched:
            for neighbor in graph.neighbors(node):
                if neighbor not in matched:
                    matching.append((node, neighbor))
                    matched.add(node)
                    matched.add(neighbor)
                    break

    return matching

def random_matching(graph):
    nodes = list(graph.nodes())
    random.shuffle(nodes)
    matched = set()
    matching = []

    for node in nodes:
        if node not in matched:
            for neighbor in graph.neighbors(node):
                if neighbor not in matched:
                    matching.append((node, neighbor))
                    matched.add(node)
                    matched.add(neighbor)
                    break

    return matching

def compare_heuristics(trials=1000, n=120, p=0.04):
    greedy_sizes = []
    random_sizes = []

    for i in range(trials):
        graph = nx.gnp_random_graph(n, p)

        matching = greedy_matching_based_on_degree(graph)
        greedy_sizes.append(len(matching))

        matching = random_matching(graph)
        random_sizes.append(len(matching))

    # Plot for Greedy Matching
    plt.figure(figsize=(10, 6))
    plt.plot(range(trials), greedy_sizes, label='Greedy Matching Size')
    plt.xlabel('Number of Trials')
    plt.ylabel('Matching Size')
    plt.title('Greedy Matching Size over Trials')
    plt.legend()
    plt.show()

    # Plot for Random Matching
    plt.figure(figsize=(10, 6))
    plt.plot(range(trials), random_sizes, label='Random Matching Size')
    plt.xlabel('Number of Trials')
    plt.ylabel('Matching Size')
    plt.title('Random Matching Size over Trials')
    plt.legend()
    plt.show()

compare_heuristics()
