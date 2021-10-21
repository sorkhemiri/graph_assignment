from models import Vertex
from utils import get_input, create_graph

if __name__ == "__main__":
    # edges = get_input()
    edges = [(1, 2), (1, 2), (3, 2), (5, 6), (4, 2)]
    graph = create_graph(edges=edges)
    graph.has_broken()
