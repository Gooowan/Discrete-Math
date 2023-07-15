import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
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
        return f"Всі вершини покриті циклами довжиною >= 3"
    else:
        return f"Не всі вершини покриті циклами довжиною >= 3"

def generate_edges(n):
    edges = []
    # Створення циклів довжиною >= 3 для кожної вершини
    for i in range(n):
        # Генерація циклу з трьох вершин
        cycle = [(i, (i+1)%n), ((i+1)%n, (i+2)%n), ((i+2)%n, i)]
        # Додавання тільки нових ребер до списку
        for edge in cycle:
            if edge not in edges and (edge[1], edge[0]) not in edges:
                edges.append(edge)
    return edges

# Запуск розв'язку з заданими ребрами
def run_solve():
    # Створення кореневого вікна Tkinter
    root = tk.Tk()
    root.withdraw()

    # Запит користувача ввести розмір графа
    size = simpledialog.askinteger("Input", "Введіть розмір графа")

    # Перевірка, чи вводив користувач число
    if size is None:
        messagebox.showinfo("Вихід", "Розмір не введено, вихід.")
        return

    # Генерація графа з випадковими ребрами
    edges = generate_edges(size)

    # Вимірювання часу виконання алгоритму
    start_time = time.time()
    result = solve(edges)
    end_time = time.time()

    # Виведення результату та часу виконання у вікні повідомлення
    messagebox.showinfo("Результат", f"{result}\nРозмір графа: {size}, Час виконання: {end_time - start_time} секунд")

# Запуск функції
run_solve()
