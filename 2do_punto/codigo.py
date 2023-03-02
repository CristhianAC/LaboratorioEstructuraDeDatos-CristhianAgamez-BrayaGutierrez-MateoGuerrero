from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Cargar el conjunto de datos de iris
iris = load_iris()

# Crear un clasificador de árbol binario
clf = DecisionTreeClassifier()

# Entrenar el clasificador en el conjunto de entrenamiento
clf.fit(iris.data, iris.target)

# Visualizar el árbol
fig, ax = plt.subplots(figsize=(12, 12))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names, ax=ax)
plt.show()
