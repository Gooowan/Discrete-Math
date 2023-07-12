import networkx as nx

# Функція для генерації графа
def generate_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

# Функція для пошуку циклів довжиною >= 3
def find_cycles(G):
    cycles = list(nx.simple_cycles(G))
    valid_cycles = [cycle for cycle in cycles if len(cycle) >= 3]
    return valid_cycles

# Функція для перевірки, чи всі вершини покриті
def check_coverage(G, cycles):
    covered = set()
    for cycle in cycles:
        covered.update(cycle)
    return covered == set(G.nodes)

# Функція для вирішення проблеми
def solve(edges):
    G = generate_graph(edges)
    cycles = find_cycles(G)
    if check_coverage(G, cycles):
        print("Всі вершини покриті циклами довжиною >= 3")
    else:
        print("Не всі вершини покриті циклами довжиною >= 3")

# Тестуємо функцію на графі
edges = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 3)]
solve(edges)
