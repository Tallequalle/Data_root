import numpy as np
def nearest_to_scalar(matrix, n):
    """
    :param matrix: numpy.ndarray[list[list[int]]]
    :param n: int
    :return: int  
    """
    # YOUR CODE HERE
    while n != 0:
        if n in matrix:
            return(n)
            break
        n -= 1

print('Nearest:', nearest_to_scalar(np.array([[5, 3, 4], [7, 9, 8], [6, 7, 8]]), 11))




