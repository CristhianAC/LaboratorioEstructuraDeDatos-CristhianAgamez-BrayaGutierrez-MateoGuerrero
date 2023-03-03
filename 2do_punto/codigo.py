#Se importan dos clases del módulo sklearn.tree que hace parte de la biblioteca scikit-learn
from sklearn.tree import DecisionTreeClassifier, plot_tree
#Se importa la función load_iris del módulo sklearn.tree que hace parte de la biblioteca scikit-learn
from sklearn.datasets import load_iris
#Se importa la biblioteca matplotlib como plt, permitirá visualizar luego
import matplotlib.pyplot as plt

#Se carga el conjunto de datos del iris en la variable "iris", el conjunto de datos tiene
#150 muestras de tres especies diferentes de iris, son: versicolor, setosa y virginica
iris = load_iris()

#Se crea un clasificador de árbol de decisión para predecir la clase de una muestra basándose en sus características
# En otras palabras permitirá crear los nodos y ramas del árbol de decisión
clf = DecisionTreeClassifier()

"""
Se entrenará al clasificador "cfl" con la información sobre las especies de iris. La función fit toma como argumentos
"iris.data" que son los datos correspondientes a las características y "iris.target" contiene las 
las etiquetas de las muestras del conjunto de datos del iris. "cfl" usa la información obtenida para crear los nodos
y ramas del árbol de decisión que permitirán predecir la clase de una flor de acuerdo a sus características.

|-------------Información contenida en los nodos-------------|

-----Todos los nodos contendrán la siguiente información:
gini: es un indice de pureza que mide la homogeneidad de las clases en el respectivo nodo, mientras más cerca de cero, 
será más homogéneo.
samples: número de muestras que llegan al nodo.
value: distribución de clases en el nodo [50, 50, 50], primer puesto las setosas, segundo las versicolor y tercero las virginicas.
class: la clase predominante en el nodo, las clases son las especies de iris que son setosa, versicolor y virginica.

--Tener en cuenta lo siguiente:
Nodo raíz: Tendrá la característica que mejor divide los datos en dos grupos según el criterio de clasificación, la característica
será el ancho del pétalo de la flor(petal length).
Nodos internos: Tendrán como características que mejor dividen los datos en cada rama según la clasificación propuesta, las características
son el largo del pétalo y el largo del sépalo
"""
clf.fit(iris.data, iris.target)

#La función subplots recibe como argumentos el tamaño de la figura, en otras palabras permite crear una figura
#y que esta tenga unos ejes, la variable "fig" es la que almacena la figura y permitirá modificar sus propiedades
# la variable "ax" es la que almacena el conjunto de ejes y permitirá modificarlos
fig, ax = plt.subplots(figsize=(12, 12))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names, ax=ax)
plt.show()
