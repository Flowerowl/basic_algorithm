from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distance = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distance[(from_node, to_node)] = distance


def dijkstra(graph, init):
    visited = {init: 0}
    path = defaultdict(list)
    nodes = set(graph.nodes)
    print("Nodes: %s" % nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge_node in graph.edges[min_node]:
            weight = current_weight + graph.distance[(min_node, edge_node)]
            if edge_node not in visited or weight < visited[edge_node]:
                visited[edge_node] = weight
                path[edge_node] = min_node

    return visited


if __name__ == "__main__":
    g = Graph()

    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_node('E')
    g.add_node('F')
    g.add_node('G')

    g.add_edge('A', 'B', 12)
    g.add_edge('A', 'C', 7)
    g.add_edge('B', 'D', 1)
    g.add_edge('B', 'A', 12)
    g.add_edge('D', 'E', 8)
    g.add_edge('C', 'F', 3)
    g.add_edge('D', 'G', 5)
    g.add_edge('F', 'B', 1)
    g.add_edge('F', 'G', 2)
    g.add_edge('C', 'D', 13)
    g.add_edge('E', 'B', 6)

    print(f"Initial Distance: { g.distance }")
    print(f"Visited: { dijkstra(g, 'A') }")
