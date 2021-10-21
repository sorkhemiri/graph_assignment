from copy import deepcopy

from utils import get_input, create_graph

if __name__ == "__main__":
    edges = get_input()
    if not edges:
        exit(1)
    graph = create_graph(edges=edges)
    if graph.has_broken():
        print("graph is broken already!")
        exit(1)
    shopstan_edges = []
    for edge in graph.edges:
        g = deepcopy(graph)
        g.remove_edge(edge=edge)
        if g.has_broken():
            shopstan_edges.append(edge)

    for edge in shopstan_edges:
        print(edge.vertices[0].name, edge.vertices[1].name)
