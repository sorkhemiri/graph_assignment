from copy import deepcopy

from utils import get_input, create_graph

if __name__ == "__main__":
    edges = get_input()
    graph = create_graph(edges=edges)
    shopstan_edges = []
    for edge in graph.edges:
        g = deepcopy(graph)
        g.remove_edge(edge=edge)
        if g.has_broken():
            shopstan_edges.append(edge)

    for edge in shopstan_edges:
        print(edge.vertices[0].name, edge.vertices[1].name)
