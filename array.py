import numpy as np
ar1 = np.array([[1,2],[3,4]])
ar2 = np.array([[5,6],[7,8]])
print(" add two matrices")
print(np.add (ar1,ar2))
print("subtract two matrices")
print(np.subtract(ar1, ar2))
print("multiply individual elements of the matrices")
print(np.multiply(ar1, ar2))
print("divide the elements of the matrices")
print(np.divide(ar1, ar2))
print("Perform matrix multiplication")
print(np.dot(ar1, ar2))
print("Display the transpose of the matrices")
print(ar1.transpose())
print(ar2.transpose())
print("Sum the elements of the matrices")
print(np.trace(ar1))
print(np.trace(ar2))



