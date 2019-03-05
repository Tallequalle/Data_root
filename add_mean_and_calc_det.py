
import numpy as np
def add_mean_and_calc_det(matrix):
    """
    :matrix: numpy.ndarray[list[list[int]]]
    :return: numpy.float64
    """
    # YOUR CODE HERE
    array_mean = np.mean(matrix, axis = 1)
    for i in range(len(matrix)):
        matrix[i] += int(array_mean[i])
    result = np.linalg.det(matrix)
    return(int(result))
print('Result:', add_mean_and_calc_det(np.array([[5, 3, 4], [7, 9, 8], [6, 7, 8]])))





