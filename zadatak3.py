import numpy as np

vector_a = np.array([1, 3, 5])
vector_b = np.array([[2], [4], [6]])

mat_mul = np.multiply(vector_a, vector_b)
vect_dot = np.dot(vector_a, vector_b)
mat_exp = np.linalg.matrix_power(mat_mul, 2)
sub_mat = mat_exp[1:, 1:]

print(vector_a)
print(vector_b)

print(mat_mul)
print(vect_dot)
print(mat_exp)
print(sub_mat)