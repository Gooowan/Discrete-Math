import time

# Оголошуємо клас для представлення графу
class Graph:
    # Метод ініціалізації графу
    def __init__(self, edges):
        # Створюємо порожній словник для графу
        self.graph = {}
        # Проходимо по всіх заданих ребрах
        for edge in edges:
            # Додаємо кожне ребро до графу
            if edge[0] not in self.graph:
                self.graph[edge[0]] = [edge[1]]
            else:
                self.graph[edge[0]].append(edge[1])

            # Переконуємося, що граф є ненапрямленим
            if edge[1] not in self.graph:
                self.graph[edge[1]] = [edge[0]]
            else:
                self.graph[edge[1]].append(edge[0])

    # Метод для пошуку циклів у графі
    def find_cycles(self):
        # Створюємо порожній список для збереження циклів
        cycles = []
        # Проходимо по всіх вершинах графу
        for start_node in self.graph:
            # Створюємо стек для DFS
            stack = [(start_node, [start_node])]
            # Продовжуємо поки в стеці є елементи
            while stack:
                # Беремо вершину зі стеку
                node, path = stack.pop()
                # Перевіряємо, чи є шлях циклом
                if path and (node == path[0]):
                    cycles.append(path)
                    continue
                # Проходимо по всіх сусідніх вершинах
                for adjacent in self.graph.get(node, []):
                    # Якщо вершина ще не відвідана, додаємо її до стеку
                    if adjacent not in path:
                        stack.append((adjacent, path + [adjacent]))
                    # Якщо ми знайшли цикл
                    else:
                        if adjacent == path[0] and len(path) >= 3:
                            stack.append((adjacent, path + [adjacent]))
        # Повертаємо всі цикли з довжиною більше або рівною 3
        return [cycle for cycle in cycles if len(cycle) >= 3]

    # Метод для перевірки, чи всі вершини покриті циклами
    def check_coverage(self, cycles):
        # Створюємо множину для збереження покритих вершин
        covered = set()
        # Проходимо по всіх циклах та додаємо їх до покритих вершин
        for cycle in cycles:
            covered.update(cycle)
        # Перевіряємо, чи всі вершини покриті
        return covered == set(self.graph.keys())


# Функція для вирішення задачі
def solve(edges):
    # Створюємо граф
    G = Graph(edges)
    # Знаходимо цикли в графі
    cycles = G.find_cycles()
    # Перевіряємо покриття та виводимо результат
    if G.check_coverage(cycles):
        print("Всі вершини покриті циклами довжиною >= 3")
    else:
        print("Не всі вершини покриті циклами довжиною >= 3")


# Створюємо список ребер для тестування

sizes = [10, 100, 1000]

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
