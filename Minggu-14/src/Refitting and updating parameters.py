import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y=True)

clf = SVC()
clf.set_params(kernel='linear').fit(X, y)
# Output :
# SVC(kernel='linear')
clf.predict(X[:5])
# Output :
# array([0, 0, 0, 0, 0])

clf.set_params(kernel='rbf').fit(X, y)
# Output :
# SVC()
clf.predict(X[:5])
# Output :
# array([0, 0, 0, 0, 0])