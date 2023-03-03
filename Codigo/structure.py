import dash
from graficador import graficador
import dash_html_components as html
import dash_core_components as dcc

import dash_bootstrap_components as dbc
class htmlwriter():
    def __init__(self) -> None:
        #Se crea la pagina web y se le pone un CSS por defecto de bootstrap
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
        #Intancio el objeto que crea la grafica
        graf = graficador()
        #Guardo la figura dentro de un atributo
        self.fig=graf.generador()
        #Llamo al metodo Changer que es el que se encarga de ilustrar el frontend.
        self.changer()
    def changer(self):
        #Se crea un layout para escribir lo necesario.
        self.app.layout = html.Div([
            html.H1("Arbol De Spotify", style={'textAlign' : 'center', 'padding-top' : 20 }),
            html.H3("By: Cristhian Agamez, Mateo Guerrero, Brayan Gutierrez",style={'textAlign' : 'center', 'font-size':20, 
                                                                                    'padding-bottom' : 20} ),
            html.H2("Punto 1",style={'padding-bottom' : 20, 'padding-left' : 20} ),
            dcc.Graph(figure=self.fig,style={'height' : 800, 'width' : 1100, 'textAlign' : 'center', 'background-color': 'rgb(0,0,0)'}
                        ), html.Div([
            html.H2("Punto 2",style={ 'padding-left' : 20,'padding-top' : 20} ),
            html.Div([
                html.H3("a)",style={'padding-left' :20}),
                html.P(" Se desea usar un árbol de decisión para clasificar las flores de iris según su especie a partir de sus medidas morfológicas, por lo que se usarán 150 muestras de tres especies diferentes de iris: setosa, versicolor, virginica. Para ello se crea un clasificador de árbol de decisión que aprende a predecir la especie de una flor basándose en las características. El clasificador es entrenado con el conjunto de datos del iris obtenido desde la biblioteca scikit-learn. El resultado final será un árbol binario, en este árbol los nodos tendrán las características de las especies de iris y al mismo tiempo una condición y dependiendo de si es Verdadera (rama izquierda) o Falsa (rama derecha) se llegará a otro nodo que podrá ser una predicción final (nodo hoja) para concluir la especie resultante, u otro nodo que tiene otra condición (nodo interior) para continuar en el árbol.", 
                style={'padding-left' :20,'padding-top' : 20, 'width':'50%'}),
                html.H3("b)", style={'padding-left' :20}),
                html.P(" Uno de los miembros del grupo está interesado en el aprendizaje automático (machine learning), por lo que se decidió hacer uno de los problemas más sencillos en el área, además de permitir entender qué son los árboles de decisión y cómo interpretarlos.",
                style={'padding-left' :20,'padding-top' : 20, 'width':'50%', 'padding-right':20})
                
            ], style={'display':'flex'}), html.Div([
                html.P("--El dataset puede ser encontrado en el siguiente link--"),
                html.P("https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html")
            ],style={'textAlign' : 'center', 'font-size':15, 'padding-top':30}),
            html.H2("Codigo:", style={"padding-left":30}),
            html.Div([
                
                html.Div([
                    
                    html.Div([
                        html.P("from sklearn.tree import DecisionTreeClassifier, plot_tree"),
                        html.P("from sklearn.datasets import load_iris"),
                        html.P("import matplotlib.pyplot as plt"),
                        html.P("iris = load_iris()"),
                        html.P("clasificacion = DecisionTreeClassifier()"),
                        html.P("clasificacion.fit(iris.data, iris.target)"),
                        html.P("fig, ax = plt.subplots(figsize=(12, 12))"),
                        html.P("plot_tree(clasificacion, filled=True, feature_names=iris.feature_names, class_names=iris.target_names, ax=ax)"),
                        html.P("plt.show()")
                        
                    ], style = {'padding-left':30, 'padding-top':30})
                    
                ], style={'background-color':'rgb(48,48,48)', 'width':1000, 'height':'auto'})
            ], style={"justify-content" : 'center', 'display' : 'flex'})
            
            
            ])
            
            
        ], style={'align-items': 'center'})
        
        self.app.run_server(debug= True, use_reloader=False)
        

