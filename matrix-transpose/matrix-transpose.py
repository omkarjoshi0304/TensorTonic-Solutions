import numpy as np

def matrix_transpose(A):

    A = np.array(A)
    n_rows, n_cols = A.shape

    transpose_A = np.zeros((n_cols, n_rows))
    
    for i in range(n_rows):
        for j in range(n_cols):

            transpose_A[j, i] = A[i, j]
            
    return transpose_A