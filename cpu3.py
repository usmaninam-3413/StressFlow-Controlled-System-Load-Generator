# Matrix multiplication stress
import numpy as np

while True:
    a = np.random.rand(300, 300)
    b = np.random.rand(300, 300)
    np.dot(a, b)