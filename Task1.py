import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

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
options = {
    "node_color" : "brown",
    "edge_color" : "green",
    "node_size" : 10000,
    "width" : 1,
    "with_labels" : True
}
top = nx.bipartite.sets(G)[1]
pos = nx.bipartite_layout(G, top ,align='horizontal')

nx.draw(G, pos, **options)
plt.show()


print(f'Вершини: {G.nodes()}' )
print(f'Ребра:  {G.edges()}')
print(f'\nКількісь вершин: {G.number_of_nodes()}')
print(f'Кількісь ребер: {G.number_of_edges()}')

degree_centrality = nx.degree_centrality(G)
print('\nНайбільше зєднань має Eспресо')
print(degree_centrality)


