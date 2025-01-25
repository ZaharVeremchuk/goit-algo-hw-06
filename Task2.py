import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(['Еспрессо', 'Молоко',  'Морозиво', 'Гаряча вода', 'Американо', 'Латe', 'Aфогато', 'Капучіно'])
edges = [
    ("Еспрессо", "Капучіно"),
    ("Еспрессо", "Aфогато"),
    ("Еспрессо", "Американо"),
    ("Еспрессо", "Латe"),
    ("Молоко", "Aфогато"),
    ("Молоко", "Латe"),
    ("Молоко", "Капучіно"),
    ("Морозиво", "Aфогато"),
    ("Гаряча вода", "Американо")
    ]
G.add_edges_from(edges)

dfs_tree = nx.dfs_tree(G, source='Еспрессо')
print(list(dfs_tree.edges()))  # виведе ребра DFS-дерева з коренем у вузлі Еспрессо

bfs_tree = nx.bfs_tree(G, source='Еспрессо')
print(list(bfs_tree.edges())) # виведе ребра BFS-дерева з коренем у вузлі Еспрессо