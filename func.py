import numpy as np
def func(m, s, k):   
    """
    :param x: int
    :param y: int
    :param z: int
    :return: float
    """
    # YOUR CODE HERE
    array = np.random.normal(loc = m,scale = s, size = 100)
    counter = 0
    for i in array:
        if i > k:
            counter += 1
    return(counter/100)
print('Result:', func(25, 3, 27))

