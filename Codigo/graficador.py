import plotly.graph_objects as go
import networkx as nx
import igraph
from igraph import Graph, EdgeSeq
from creadorDeArbol import creadorDeArbol
class graficador:
    def __init__(self) -> None:
        self.treeCreator = creadorDeArbol()
        self.treeCreator.lector("./CSV/User_track_data.csv")
        self.treeCreator.lector("./CSV/User_track_data_2.csv")
        self.tree = self.treeCreator.lector("./CSV/User_track_data_3.csv")
        self.tree.llamarImpresiones("postorden")
        self.G = nx.Graph()
    def generador(self):
        nodos = self.tree.recorrer([])
        try:
            for i in nodos:
                self.G.add_node(i.nombre)
        except:
            print("a")
        self.tree.agregadorDeVertices(node=self.tree.raiz,G=self.G)
        nr_vertices = len(nodos)
        v_label = list(map(str, range(nr_vertices)))
        G = Graph.Tree(nr_vertices, 2) # 2 stands for children number
        lay = G.layout('rt')

        position = {k: lay[k] for k in range(nr_vertices)}
        Y = [lay[k][1] for k in range(nr_vertices)]
        M = max(Y)
        print(position)
        es = EdgeSeq(G) # sequence of edges
        E = [e.tuple for e in G.es] # list of edges

        L = len(position)
        Xn = [position[k][0] for k in range(L)]
        Yn = [2*M-position[k][1] for k in range(L)]
        Xe = []
        Ye = []
        for edge in E:
            Xe+=[position[edge[0]][0],position[edge[1]][0], None]
            Ye+=[2*M-position[edge[0]][1],2*M-position[edge[1]][1], None]

        labels = v_label

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=Xe,
                        y=Ye,
                        mode='lines',
                        line=dict(color='rgb(210,210,210)', width=1),
                        hoverinfo='none'
                        ))
        fig.add_trace(go.Scatter(x=Xn,
                        y=Yn,
                        mode='markers',
                        name='bla',
                        marker=dict(symbol='circle-dot',
                                        size=18,
                                        color='#6175c1',    #'#DB4551',
                                        line=dict(color='rgb(50,50,50)', width=1)
                                        ),
                        text=labels,
                        hoverinfo='text',
                        opacity=0.8
                        ))
        fig.show()

        




