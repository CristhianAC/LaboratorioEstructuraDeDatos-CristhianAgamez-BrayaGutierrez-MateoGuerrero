#from graficador import graficador
#graf = graficador()
#graf.generador()
import networkx as nx
import matplotlib.pyplot as plt

# Creamos el grafo de ejemplo
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
G.add_weighted_edges_from([('A', 'B', 2), ('A', 'C', 3), ('B', 'C', 1),
                           ('B', 'D', 1), ('B', 'E', 4), ('C', 'E', 5),
                           ('D', 'E', 1), ('E', 'F', 1)])

# Calculamos el árbol de expansión mínima utilizando el algoritmo de Kruskal
T = nx.minimum_spanning_tree(G)

# Graficamos el árbol resultante
pos = nx.spring_layout(G)  # Calculamos la posición de los nodos
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(T, pos)
nx.draw_networkx_labels(G, pos)
plt.show()

