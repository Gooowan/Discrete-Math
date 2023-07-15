import networkx as nx
import time

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
sizes = [1, 3, 10, 15, 25]
def generate_edges(n):
    edges = []
    # Створюємо цикли довжиною >= 3 для кожної вершини
    for i in range(n):
        # Генеруємо цикл з трьох вершин
        cycle = [(i, (i+1)%n), ((i+1)%n, (i+2)%n), ((i+2)%n, i)]
        # Додаємо тільки нові ребра до списку
        for edge in cycle:
            if edge not in edges and (edge[1], edge[0]) not in edges:
                edges.append(edge)
    return edges

# Запускаємо розв'язок з заданими ребрами
for size in sizes:
    # Генеруємо граф з випадковими ребрами
    edges = generate_edges(size)

    # Вимірюємо час виконання алгоритму
    start_time = time.time()
    solve(edges)
    end_time = time.time()

    # Виводимо час виконання
    print(f"Розмір графу: {size}, Час виконання: {end_time - start_time} секунди")
