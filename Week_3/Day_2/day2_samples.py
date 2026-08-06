import numpy as np

A = np.array([[3, 1], [1,3]])
determinant = np.linalg.det(A)
# print("Determinant: ", determinant)

#################

eigenValues, eigneVectors = np.linalg.eig(A)
# print("EigenVal\n", eigenValues)
# print("EigenVectors\n", eigneVectors)

##################

inverse = np.linalg.inv(A)
# print("Inverse of A: \n", inverse)

##################

U, S, Vt = np.linalg.svd(A)

# Av1/σ1 and Av2/σ2​.... v1,v2 are eigen vectors. σ1, σ2​ are singular values
print("U: \n", U)

#∣AtA−λI∣=0 => sqrt(λ1), sqrt(λ2)
print("Singular Values: \n", S)     

#when λ1(16), we get [1,1]. so dividing it by it's sqrt gives [0.707, 0.707]​..same with λ2(4)
print("V Transpose: \n", Vt)


