import dash
from graficador import graficador
import dash_html_components as html
import dash_core_components as dcc

import dash_bootstrap_components as dbc
class htmlwriter():
    def __init__(self) -> None:
        
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
        graf = graficador()
        self.fig=graf.generador()
        self.changer()
    def changer(self):
        self.app.layout = html.Tbody(style={'background-color': 'black'})
        self.app.layout = html.Div([
            html.H1("Arbol De Spotify", style={'textAlign' : 'center', 'padding-top' : 20 }),
            html.H3("By: Cristhian Agamez, Mateo Guerrero, Brayan Gutierrez",style={'textAlign' : 'center', 'font-size':20, 
                                                                                    'padding-bottom' : 20} ),
            
            dcc.Graph(figure=self.fig,style={'height' : 800, 'width' : 1100, 'textAlign' : 'center', 'background-color': 'rgb(0,0,0)'}
                        )
            
        ], style={'align-items': 'center'})
        self.app.run_server(debug= True, use_reloader=False)
        

