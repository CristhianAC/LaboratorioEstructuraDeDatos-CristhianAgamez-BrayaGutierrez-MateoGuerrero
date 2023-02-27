import plotly.graph_objects as go
import networkx as nx
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
        pos = nx.spring_layout(self.G)
        node_x = []
        node_y = []
        for key in pos:
            node_x.append(pos[key][0])
            node_y.append(pos[key][1])
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            text=list(self.G.nodes),
            textposition="bottom center",
            hoverinfo='text',
            marker=dict(
                showscale=False,
                color='red',
                size=20
            )
        )
        
        edge_x = []
        edge_y = []
        for edge in self.G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=1, color='black'),
            hoverinfo='none',
            mode='lines'
        )
        fig = go.Figure(
            data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='Spotify',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                )
            )
        fig.show()



        




