from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)
# Output :
# SVC()

list(clf.predict(iris.data[:3]))
# Output :
# [0, 0, 0]

clf.fit(iris.data, iris.target_names[iris.target])
# Output :
# SVC()

list(clf.predict(iris.data[:3]))
# Output :
# ['setosa', 'setosa', 'setosa']