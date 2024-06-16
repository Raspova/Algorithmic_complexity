import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.euler import has_eulerian_path, eulerian_path, is_eulerian, eulerian_circuit
from networkx.algorithms.approximation import traveling_salesman_problem

def analyze_graph():
    # Step 1: Create a random graph
    G = nx.gnp_random_graph(5, 0.5, directed=False)
    # Step 2: Check for Eulerian path or circuit
    eulerian_path_exists = has_eulerian_path(G)
    eulerian_circuit_exists = is_eulerian(G)
    print("Eulerian Path exists:", eulerian_path_exists)
    print("Eulerian Circuit exists:", eulerian_circuit_exists)
    if eulerian_path_exists:
        e_path = list(eulerian_path(G))
        print("Eulerian Path:", e_path)
    else:
        e_path = None
    if eulerian_circuit_exists:
        e_circuit = list(eulerian_circuit(G))
        print("Eulerian Circuit:", e_circuit)
    else:
        e_circuit = None
    # Step 3: Construct the line graph
    L_G = nx.line_graph(G)
    # Step 4: Use an approximation to find Hamiltonian path in the line graph
    # We'll use the Traveling Salesman Problem (TSP) solver as a proxy for the Hamiltonian path
    hamiltonian_path_approx = traveling_salesman_problem(L_G)
    print("Hamiltonian Path in line graph (approx):", hamiltonian_path_approx)
    # Plotting the original graph and its line graph
    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=16)
    plt.title("Original Graph")
    plt.subplot(122)
    nx.draw(L_G, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=500, font_size=16)
    plt.title("Line Graph")
    plt.show()
# Run the analysis
analyze_graph()
