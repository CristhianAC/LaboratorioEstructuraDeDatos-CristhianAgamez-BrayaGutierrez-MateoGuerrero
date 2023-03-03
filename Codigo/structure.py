import dash
from graficador import graficador
import dash_html_components as html
import dash_core_components as dcc
class htmlwriter():
    def __init__(self) -> None:
        
        self.app = dash.Dash()
        graf = graficador()
        self.fig=graf.generador()
        self.fig.show()
    def     
        

