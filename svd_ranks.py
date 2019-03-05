import numpy as np

def svd_ranks(Z): 
    """
    :param Z: numpy.ndarray[list[list[int]]]
    :return: list  
    """
    # YOUR CODE HERE
    P, D, Q = np.linalg.svd(Z, full_matrices=False)
    a = np.linalg.matrix_rank(P)
    b = np.linalg.matrix_rank(D)
    c = np.linalg.matrix_rank(Q)

    return(a,b,c)
print('Svd ranks:',svd_ranks(np.arange(9).reshape((3,3))))




