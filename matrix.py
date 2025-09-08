import numpy as np

m= int(input("Enter the number of rows(m): "))
n = int(input("Enter the number of columns(n): "))
U=np.array([list(map(float,input("Enter row values separated by space:").split())) for i in range(m)])
print("Matrix U:")
print(U)