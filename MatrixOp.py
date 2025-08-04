import numpy as np
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
print("Add two matrices:")
print(np.add(arr1,arr2))

print("Subtract two matrices:")
print(np.subtract(arr1,arr2))

print("Multiply two matrices:")
print(np.multiply(arr1,arr2))

print("Divide two matrices:")
print(np.divide(arr1,arr2))

print(" Matrix multiplication")
print(np.dot(arr1,arr2))

print("Transpose of the matrices")
print(arr1.transpose())
print(arr2.transpose())

print("Sum of diagonal elements")
print(np.trace(arr1))
print(np.trace(arr2))
