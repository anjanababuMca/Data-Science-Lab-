import numpy as np

A= np. array([[1,2],[3,4],[5,6]])
print(A)
U,s,VT=np.linalg.svd(A)
print(U)
print("singular Matrix:")
print(s)
print("Right Singular Matrix:")
print(VT)
sigma=np.zeros((A.shape[0],A.shape[1]))
np.fill_diagonal(sigma,s)
B= U.dot(sigma.dot(VT))
print("Reconstructed Matrix:\n",B)