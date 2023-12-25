import networkx as nx


def day_25_01(lines: list[str]) -> int:
    graph = nx.Graph()
    for line in lines:
        node, connections = line.split(': ')
        connections = set(connections.split(' '))
        for connection in connections:
            graph.add_edge(node, connection)
            graph.add_edge(connection, node)
    minimum_cut = nx.minimum_edge_cut(graph)
    assert len(minimum_cut) == 3
    graph.remove_edges_from(minimum_cut)
    comp_1, comp_2 = nx.connected_components(graph)
    return len(comp_1) * len(comp_2)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_25_01(input_lines)
    print(result)
