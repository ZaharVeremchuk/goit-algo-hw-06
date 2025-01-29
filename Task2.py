from collections import deque

def dfs_iterative(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex]))  

def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited  

graph = {
    "Еспрессо": ["Капучіно", "Aфогато", "Американо", "Латe"],
    "Молоко": ["Капучіно", "Aфогато","Латe"],
    "Морозиво": ["Aфогато"],
    "Гаряча вода": ["Американо"],
    "Капучіно": ["Еспрессо", "Молоко"],
    "Aфогато": ["Еспрессо", "Молоко","Морозиво"],
    "Американо": ["Еспрессо", "Гаряча вода"],
    "Латe": ["Еспрессо", "Молоко"]
}
print("Ітеративний DFS")
dfs_tree = dfs_iterative(graph, "Еспрессо")

print("\nІтеративний BFS")
bfs_tree = bfs_iterative(graph, "Еспрессо")