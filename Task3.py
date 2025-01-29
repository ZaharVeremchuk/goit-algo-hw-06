import networkx as nx


def print_table(distances, visited):
    # Верхній рядок таблиці
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)
    
    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        
        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\\n")

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
        
        # Вивід таблиці після кожного кроку
        print_table(distances, visited)

    return distances

graph = {
    "Еспресо": {"Капучіно": 30, "Aфогато": 60, "Американо": 60, "Латe": 60},
    "Молоко": {"Капучіно": 180, "Aфогато": 120,"Латe": 360},
    "Морозиво": {"Aфогато": 60},
    "Гаряча вода": {"Американо": 200},
    "Капучіно": {"Еспресо": 180, "Молоко": 30},
    "Aфогато": {"Еспресо": 60 , "Молоко": 120, "Морозиво": 60},
    "Американо": {"Еспресо": 60, "Гаряча вода": 200},
    "Латe": {"Еспресо": 60, "Молоко": 360}
}
shortest_paths = dijkstra(graph, 'Еспресо')
print(shortest_paths)  # виведе найкоротші шляхи від вузла 'Еспресо' до всіх інших вузлів

G = nx.Graph()

G.add_nodes_from(['Еспресо', 'Молоко',  'Морозиво', 'Гаряча вода', 'Американо', 'Латe', 'Aфогато', 'Капучіно'])

G.add_edge("Еспресо", "Капучіно", weight = 30)
G.add_edge("Еспресо", "Aфогато", weight= 60)
G.add_edge("Еспресо", "Американо", weight= 60)
G.add_edge("Еспресо", "Латe", weight = 60)
G.add_edge("Молоко", "Aфогато", weight = 120)
G.add_edge("Молоко", "Латe", weight = 360)
G.add_edge("Молоко", "Капучіно", weight = 180)
G.add_edge("Морозиво", "Aфогато", weight = 60)
G.add_edge("Гаряча вода", "Американо", weight = 200)

# Застосування алгоритму Дейкстри
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source = "Еспресо", weight='вміст')

print(shortest_path_lengths)  # виведе довжини найкоротших шляхів від вузла 'Еспресо' до всіх інших вузлів
