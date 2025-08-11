# Program 3
import numpy as np
matrix=np.random.randint(10,size=(2,2))
print("random Generated matrix:")
print(matrix)

#rank of matrix
rank=np.linalg.matrix_rank(matrix)
print("rank of matrix:",rank)

# determinant
det=np.linalg.det(matrix)
print("determinant of matrix:",det)

#Eigen values and vectors
Eval,Evect=np.linalg.eig(matrix)
print("Eigenvalues:",Eval)
print("Eigenvectors:",Evect)

# Transform Matrix in 1_D array

array_1D=matrix.flatten()
print("Transform Matrix in  1D array:",array_1D)


#inverse
inverse=np.linalg.inv(matrix)
print("Inverse of matrix:",inverse)