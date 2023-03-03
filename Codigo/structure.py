import dash
from graficador import graficador
import dash_html_components as html
import dash_core_components as dcc
class htmlwriter():
    def __init__(self) -> None:
        
        self.app = dash.Dash(__name__)
        graf = graficador()
        self.fig=graf.generador()
        self.changer()
    def changer(self):
        
        self.app.layout = html.Div([
            html.H1("Arbol De Spotify", style={'textAlign' : 'center', 'align-items': 'center'}),
            dcc.Graph(figure=self.fig,style={'height' : 800, 'width' : 1100, 'textAlign' : 'center'})
        ])
        self.app.run_server(debug= True, use_reloader=False)
        

