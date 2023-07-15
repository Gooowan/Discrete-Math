import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import time

# Клас Graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    # Функція для додавання ребра до графа
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Функція для знаходження всіх циклів
    def findCyclesUtil(self, u, parent, visited, recStack, cycles):
        visited[u] = True
        recStack[u] = True

        for neighbor in self.graph[u]:
            if not visited[neighbor]:
                parent[neighbor] = u
                self.findCyclesUtil(neighbor, parent, visited, recStack, cycles)
            elif recStack[neighbor]:
                cycle = []
                node = u
                while node != neighbor:
                    cycle.append(node)
                    node = parent[node]
                cycle.append(node)
                cycles.append(cycle)

        recStack[u] = False

    # Функція для перевірки, чи всі вершини покриті циклами довжиною >=3
    def checkCoverage(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        parent = [-1] * self.V
        cycles = []

        for node in range(self.V):
            if not visited[node]:
                self.findCyclesUtil(node, parent, visited, recStack, cycles)

        valid_cycles = [cycle for cycle in cycles if len(cycle) >= 3]
        covered = set()
        for cycle in valid_cycles:
            covered.update(cycle)

        return covered == set(range(self.V))

# Функція для вирішення проблеми
def solve(size):
    g = Graph(size)
    for i in range(size):
        g.addEdge(i, (i+1)%size)
        g.addEdge((i+1)%size, (i+2)%size)
        g.addEdge((i+2)%size, i)

    if g.checkCoverage():
        return f"Всі вершини покриті циклами довжиною >= 3"
    else:
        return f"Не всі вершини покриті циклами довжиною >= 3"

# Запуск розв'язку з заданими ребрами
def run_solve():
    # Створення кореневого вікна Tkinter
    root = tk.Tk()

    # Запит користувача ввести розмір графа
    size_button = tk.Button(root, text="Введіть розмір графа", command=lambda: get_size_and_solve(root))
    size_button.pack()

    root.mainloop()

# Функція для отримання розміру та розв'язання
def get_size_and_solve(root):
    # Запит користувача ввести розмір графа
    size = simpledialog.askinteger("Input", "Введіть розмір графа")

    # Перевірка, чи вводив користувач число
    if size is None:
        messagebox.showinfo("Вихід", "Розмір не введено, вихід.")
        return

    # Вимірювання часу виконання алгоритму
    start_time = time.time()
    result = solve(size)
    end_time = time.time()

    # Виведення результату та часу виконання у вікні повідомлення
    messagebox.showinfo("Результат", f"{result}\nРозмір графа: {size}, Час виконання: {end_time - start_time} секунд")

run_solve()
