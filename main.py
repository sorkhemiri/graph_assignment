from models import Vertex, Edge
from utils import get_input, create_graph

if __name__ == "__main__":
    # edges = get_input()
    edges = [(1, 2), (1, 2), (3, 2), (5, 6), (4, 2)]
    graph = create_graph(edges=edges)
    v1 = Vertex(name=1)
    v2 = Vertex(name=2)
    e = Edge(v1, v2)
    graph.remove_edge(e)
    graph.edges
