import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.euler import has_eulerian_path, eulerian_path, is_eulerian, eulerian_circuit
from networkx.algorithms.approximation import traveling_salesman_problem

def analyze_eulerian_path(G : nx.Graph):
    degrees = {node: val for (node, val) in G.degree()}
    even_degree_count = sum(1 for degree in degrees.values() if degree % 2 == 0)
    odd_degree_count = sum(1 for degree in degrees.values() if degree % 2 != 0)
    eulerian_path_exists = (odd_degree_count == 2 or odd_degree_count == 0)
    if even_degree_count == len(G.nodes):
        print("Every vertex has an even degree. The graph has an Eulerian circuit.")
    elif odd_degree_count == 2:
        print("Exactly two vertices have an odd degree. The graph has an Eulerian path.")
    else:
        print("The graph has neither an Eulerian path nor an Eulerian circuit.")
    if eulerian_path_exists:
        e_path = list(eulerian_path(G))
        print("Eulerian Path:", e_path)
    if eulerian_circuit_exists:
        e_circuit = list(eulerian_circuit(G))
        print("Eulerian Circuit:", e_circuit)
    return eulerian_path_exists


def is_valid_vertex(v, pos, path, G):
    # Check if the current vertex and the last vertex in the path have an edge
    if G.has_edge(path[pos - 1], v) == False:
        return False
    # Check if the vertex is already in the path
    if v in path:
        return False
    return True

def hamiltonian_path_util(G, path, pos):
    # Base case: If all vertices are included in the path
    if pos == len(G.nodes):
        return True
    # Try different vertices as the next candidate in the Hamiltonian Path
    for v in G.nodes:
        if is_valid_vertex(v, pos, path, G):
            path[pos] = v
            # Recur to construct the rest of the path
            if hamiltonian_path_util(G, path, pos + 1):
                return True
            # If adding vertex v doesn't lead to a solution, remove it
            path[pos] = -1

    return False
def find_hamiltonian_path(G):
    path = [-1] * len(G.nodes)

    # Try to find a Hamiltonian Path starting from each vertex
    for start_vertex in G.nodes:
        path[0] = start_vertex
        if hamiltonian_path_util(G, path, 1):
            return path

def analyze_graph():
    # Step 1: Create a random graph
    # Step 2: Check if the graph has an Eulerian path or circuit
    G = nx.gnp_random_graph(5, 0.5, directed=False)
    # Ensure that the graph has an Eulerian path to make the line graph, 
    while not has_eulerian_path(G):
        G = nx.gnp_random_graph(5, 0.5, directed=False)
    # Step 3: Construct the line graph
    L_G = nx.line_graph(G)
    # Step 4: Since we made sure that the graph has an Eulerian path, the line graph will have a Hamiltonian path
    # we Found the Hamiltonian Path using the backtracking algorithm
    hamiltonian_path = find_hamiltonian_path(L_G)
    print("Hamiltonian Path in line graph (approx):", hamiltonian_path)
    # Plotting the original graph and its line graph
    path_edges = []
    if hamiltonian_path:
        path_edges = [(hamiltonian_path[i], hamiltonian_path[i + 1]) for i in range(len(hamiltonian_path) - 1)]

    # Plotting the original graph
    plt.figure(figsize=(10, 5))

    pos = nx.spring_layout(G)  # Layout for the graph
    plt.subplot(121)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=16)
    plt.title("Original Graph")

    # Plotting the line graph
    plt.subplot(122)
    pos_LG = nx.spring_layout(L_G)
    nx.draw(L_G, pos_LG, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=500, font_size=16)
    plt.title("Line Graph")

    # Highlight the Hamiltonian path
    if path_edges:
        nx.draw_networkx_edges(L_G, pos_LG, edgelist=path_edges, edge_color='r', width=2)

    plt.show()

# Run the analysis
analyze_graph()
