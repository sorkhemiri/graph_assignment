def get_number_of_edges():
    number_of_edges = input()
    try:
        number_of_edges = int(number_of_edges)
        return number_of_edges
    except ValueError:
        print("enter correct integer")
        return get_number_of_edges()


def get_input():
    number_of_edges = get_number_of_edges()
    edges = []
    for i in range(number_of_edges):
        input_str = input()
        edge = input_str.strip().split()

        if len(edge) != 2:
            print("edge must consist of two vertices")
            return
        try:
            edge = tuple(int(v) for v in edge)
        except ValueError:
            print("vertex names must be integer")
            return
        if (edge in edges) or ((edge[1], edge[0]) in edges):
            continue
        edges.append(edge)
    return edges
