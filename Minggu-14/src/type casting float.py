import numpy as np
from sklearn import kernel_approximation

rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
X = np.array(X, dtype='float32')
X.dtype
# Output :
# dtype('float32')

transformer = kernel_approximation.RBFSampler()
X_new = transformer.fit_transform(X)
X_new.dtype
# Output :
# dtype('float64')