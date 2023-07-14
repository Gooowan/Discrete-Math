class Graph:
    def __init__(self, edges):
        self.graph = {}
        for edge in edges:
            if edge[0] not in self.graph:
                self.graph[edge[0]] = [edge[1]]
            else:
                self.graph[edge[0]].append(edge[1])

            if edge[1] not in self.graph:
                self.graph[edge[1]] = [edge[0]]
            else:
                self.graph[edge[1]].append(edge[0])

    def find_cycles(self):
        cycles = []
        for start_node in self.graph:
            stack = [(start_node, [start_node])]
            while stack:
                node, path = stack.pop()
                if path and (node == path[0]):
                    cycles.append(path)
                    continue
                for adjacent in self.graph.get(node, []):
                    if adjacent not in path:
                        stack.append((adjacent, path + [adjacent]))
                    else:
                        if adjacent == path[0] and len(path) >= 3:
                            stack.append((adjacent, path + [adjacent]))
        return [cycle for cycle in cycles if len(cycle) >= 3]

    def check_coverage(self, cycles):
        covered = set()
        for cycle in cycles:
            covered.update(cycle)
        return covered == set(self.graph.keys())

def solve(edges):
    G = Graph(edges)
    cycles = G.find_cycles()
    if G.check_coverage(cycles):
        print("Всі вершини покриті циклами довжиною >= 3")
    else:
        print("Не всі вершини покриті циклами довжиною >= 3")

edges = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 3)]
solve(edges)
