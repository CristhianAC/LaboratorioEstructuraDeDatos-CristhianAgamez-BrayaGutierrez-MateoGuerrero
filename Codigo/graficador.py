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
        #Almaceno los nodos en una lista incluyendo los hijos none
        self.nodos = self.tree.recorrer([])
        
        
        self.nombres=[]
        self.song=[]
        #Almaceno los nombres de los nodos en una lista
        for k in self.nodos:
            if k is not None:
                self.nombres.append(k.nombre)
        #Almaceno las listas de canciones perteneciente a cada persona en una lista
        for k in self.nodos:
            if k is not None:
                self.song.append(k.songs)
        #Creo un atributo que almacene la cantidad de vertices
        self.nr_vertices = len(self.nombres)
        #Creo el apartado grafico del arbol, especificando que cada nodo tendrá dos hijos como maximo
        self.G = Graph.Tree(self.nr_vertices, 2)
    #Metodo que se encarga de reemplazar los numeros de los nodos por los nombres de los nodos correspondientes
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
    #Funcion que se encarga de generar el apartado grafico.
    def generador(self):
        nodos = self.tree.recorrer([])
        
        #Agrego los nodos correspondientes a las graficas
        try:
            for i in nodos:
                self.G.add_node(i.nombre)
        except:
            print("a")
        
        #Principalmente creo una lista que almacene los numeros por nivel y no por nombre.
        v_label = list(map(str, range(self.nr_vertices)))
        
        #Creo un diccionario que almacenará las coordenadas de los nodos
        position ={}
        Y =[]
        for k in nodos:
            if k is not None:
                position[k.nombre] = k.coords
                Y.append(k.coords[1])
        Xn=[]
        Yn=[]
        #Se agregaran las coordenadas de los nodos para posteriormente graficarlos en esa posicion
        for k in nodos:
            if k is not None:
                posicionY = position[k.nombre][1]
                Xn.append(position[k.nombre][0]) 
                Yn.append(posicionY)
        Xe = []
        Ye = []
        
        for i in range(len(nodos)):
            #Se recorre cada nodo
            nodo = nodos[i]
            #Y si ese nodo no esta vacio se calculará si tiene hijos en esa lista.
            #Posteriormente se tomará el nodo padre y trazará una linea entre el padre y el hijo, con los dos hijos.
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
        #Creo unas figuras
        fig = go.Figure()
        #Posteriormante se crean las lineas(Aristas) de las listas.
        fig.add_trace(go.Scatter(x=Xe,
                        y=Ye,
                        mode='lines',
                        line=dict(color='rgb(210,210,210)', width=5),
                        hoverinfo='none'
                        ))
        #Posteriormente se dibujan los nodos sobre las lineas(Aristas)
        fig.add_trace(go.Scatter(x=Xn,
                        y=Yn,
                        mode='markers',
                        name='bla',
                        marker=dict(symbol='circle-dot',
                                        size=30,
                                        color='rgb(32,96,61)',
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
        #actualizo el grafico, pero esta vez se quitan cosa como las coordenadas que aparecen en el ejex y ejey
        #Tambien agrego las notaciones/nombre del perteneciente del nodo
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
        #Retorno la grafica
        return fig

        




