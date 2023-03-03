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
        
        self.nodos = self.tree.recorrer([])
        print(self.tree.raiz.songs)
        self.nombres=[]
        self.song=[]
        for k in self.nodos:
            if k is not None:
                self.nombres.append(k.nombre)
        for k in self.nodos:
            if k is not None:
                self.song.append(k.songs)
        self.nr_vertices = len(self.nombres)
        self.G = Graph.Tree(self.nr_vertices, 2)
    def make_annotations(self, pos, text,font_size=10, font_color='rgb(0,0,0)'):
        L=len(pos)
        if len(text)!=L:
            raise ValueError('The lists pos and text must have the same len')
        annotations = []
        for k in range(L):
            
            annotations.append(
                dict(
                    
                        text = self.nombres[k], 
                    x=pos[self.nombres[k]][0], y=pos[self.nombres[k]][1],
                    xref='x1', yref='y1',
                    font=dict(color=font_color, size=font_size),
                    showarrow=False)
            )
        return annotations
    def generador(self):
        nodos = self.tree.recorrer([])
        
        
        try:
            for i in nodos:
                self.G.add_node(i.nombre)
        except:
            print("a")
        
        
        v_label = list(map(str, range(self.nr_vertices)))
        
        lay = self.G.layout('rt')
        position ={}
        Y =[]
        for k in nodos:
            if k is not None:
                position[k.nombre] = k.coords
                Y.append(k.coords[1])
        Xn=[]
        Yn=[]
        for k in nodos:
            if k is not None:
                posicionY = position[k.nombre][1]
                Xn.append(position[k.nombre][0]) 
                Yn.append(posicionY)
        Xe = []
        Ye = []
        for i in range(len(nodos)):
            nodo = nodos[i]
            if nodo is not None:
                izq = 2*i+1
                der = 2*i+2
                if izq<len(nodos) and nodos[izq] is not None:
                    hijoizq = nodos[izq]
                    Xe+=[position[nodo.nombre][0],position[hijoizq.nombre][0], None]
                    
                    Ye+=[position[nodo.nombre][1],position[hijoizq.nombre][1], None]
                if der<len(nodos) and nodos[der] is not None:
                    hijoder = nodos[der]
                    Xe+=[position[nodo.nombre][0],position[hijoder.nombre][0], None]
                    
                    Ye+=[position[nodo.nombre][1],position[hijoder.nombre][1], None]
        labels = v_label
        #print(nodos)
        #print(Ye)
        #print(position)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=Xe,
                        y=Ye,
                        mode='lines',
                        line=dict(color='rgb(210,210,210)', width=5),
                        hoverinfo='none'
                        ))
        fig.add_trace(go.Scatter(x=Xn,
                        y=Yn,
                        mode='markers',
                        name='bla',
                        marker=dict(symbol='circle-dot',
                                        size=30,
                                        color='#6175c1',    #'#DB4551',
                                        line=dict(color='rgb(50,50,50)', width=1)
                                        ),
                        text=labels,
                        hoverinfo='text',
                        opacity=0.8
                        ))
        axis = dict(showline=False, 
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            )

        fig.update_layout(
                    annotations=self.make_annotations(pos = position,text = v_label),
                    font_size=12,
                    showlegend=False,
                    xaxis=axis,
                    yaxis=axis,
                    margin=dict(l=40, r=40, b=85, t=100),
                    hovermode = 'closest',
                    plot_bgcolor='rgb(248,248,248)'
                    )
        return fig

        




