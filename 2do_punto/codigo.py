from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.datasets import load_iris
import graphviz

# Cargar el conjunto de datos de iris
iris = load_iris()

# Crear un clasificador de árbol binario
clf = DecisionTreeClassifier()

# Entrenar el clasificador en el conjunto de entrenamiento
clf.fit(iris.data, iris.target)

# Exportar el árbol a formato DOT
dot_data = export_graphviz(clf, out_file=None, 
                           feature_names=iris.feature_names,  
                           class_names=iris.target_names,  
                           filled=True, rounded=True,  
                           special_characters=True)

# Visualizar el árbol
graph = graphviz.Source(dot_data)  
graph.view()