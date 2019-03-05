def sec_smallest(numbers):
    """
    :param numbers: list[int]
    :return: int    
    """
    # YOUR CODE HERE
    total = min(numbers)
    counter = 0
    for i in numbers:
        if i == total:
            counter += 1
    for j in range(counter):
        numbers.remove(total)
    total = min(numbers)
    return(total)
    
print('Sec_smallest:', sec_smallest([1, 2, -8, -8, -2, 0]))




