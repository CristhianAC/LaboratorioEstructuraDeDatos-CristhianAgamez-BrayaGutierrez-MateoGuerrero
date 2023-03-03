#Se importan dos clases del módulo sklearn.tree que hace parte de la biblioteca scikit-learn
from sklearn.tree import DecisionTreeClassifier, plot_tree
#Se importa la función load_iris del módulo sklearn.tree que hace parte de la biblioteca scikit-learn
from sklearn.datasets import load_iris
#Se importa la biblioteca matplotlib como plt, permitirá visualizar un gráfico
import matplotlib.pyplot as plt

"""
Se carga el conjunto de datos del iris en la variable "iris", el conjunto de datos tiene
150 muestras de tres especies diferentes de iris, son: versicolor, setosa y virginica.
Cada muestra tiene cuatro características: longitud y ancho del sépalo, y longitud y ancho 
pétalo.
"""
iris = load_iris()

"""
Se crea un objeto de la clase "DecisionTreeClassifier()" que es básicamente un clasificador de árbol de decisión para predecir la clase 
que puede salir de un conjunto de muestras basándose en sus características.
En otras palabras permitirá crear los nodos y ramas del árbol de decisión
"""
clasificacion = DecisionTreeClassifier()

"""
Se entrenará al clasificador "clasificacion" con la información sobre las especies de iris. La función "fit()" toma como argumentos
"iris.data" que son los datos correspondientes a las características y "iris.target" contiene las 
las etiquetas de las muestras del conjunto de datos del iris. 
"clasificacion" usa la información obtenida para crear los nodos y ramas del árbol de decisión que permitirán predecir la 
clase de una flor de acuerdo a sus características.

|-------------Información contenida en los nodos-------------|

-----Todos los nodos contendrán la siguiente información:
gini: es un indice de pureza que mide la homogeneidad de las clases en el respectivo nodo, mientras más cerca de cero, 
será más homogéneo. Con los datos elegidos es básicamente que tan pura es la especie de iris.
samples: número de muestras que llegan al nodo.
value: distribución de clases en el nodo [50, 50, 50], primer puesto las setosas, segundo las versicolor y tercero las virginicas.
class: la clase predominante en el nodo, las clases son las especies de iris que son setosa, versicolor y virginica.

--Tener en cuenta lo siguiente:
Nodo raíz: Tendrá la característica que mejor divide los datos en dos grupos según el criterio de clasificación, la característica
será el ancho del pétalo de la flor(petal width).
Nodos internos: Tendrán como características lo que mejor divide los datos en cada rama según la clasificación propuesta, las características
son el largo del pétalo(petal length) y el largo del sépalo(sepal length).
Nodo hoja: serán el resultado final y contendrán en "class" la especie que ha sido predecida según cada decisión tomada y los datos dados.

------Explicación de las ramas:
Cuando una rama sale de un nodo, esta contiene la condición que se aplica a la característica del nodo para dividir los datos
en dos grupos, las condiciones serán valores númericos y establecen que el valor pedido sea menor que un valor númerico establecido, 
cuando la rama entra al nodo, esta contendra un True o False dependiendo de si se cumplio o no la condición dada por el nodo anterior.
Tener en cuenta, que en el árbol creado la rama izquierda corresponde a True(Verdadero) y la rama derecha a False(Falso)
"""
clasificacion.fit(iris.data, iris.target)

"""
La función "subplots()" recibe como argumentos el tamaño de la figura, en otras palabras permite crear una figura
y que esta tenga unos ejes, la variable "fig" es la que almacena la figura y permitirá modificar sus propiedades
la variable "ax" es la que almacena el conjunto de ejes y permitirá modificarlos
"""
fig, ax = plt.subplots(figsize=(12, 12))
"""
La función "plot_tree()" recibe como parametros:
"filled=True": los nodos se colorean según la clase predominante
"feature_names=iris.feature_names": nombre de las características usadas para entrenar al árbol
"class_names=iris.target_names": nombres de las clases del conjunto de datos
"ax=ax": se usa el objeto ax creado previamente, básicamente los ejes
"""
plot_tree(clasificacion, filled=True, feature_names=iris.feature_names, class_names=iris.target_names, ax=ax)

# La función show() mostrará la figura resultante en una ventana emergente
plt.show()