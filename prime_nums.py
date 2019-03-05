
def prime_nums(n):
    """
    :param n: int
    :return: list[int]
    """
    # YOUR CODE HERE
    list = []
    for i in range(2,n):
        if (i < 6):
            if (i / 2 == 1) or (i / 3 == 1) or (i / 5 == 1):
                list.append(i)
        else: 
            if ((i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0)):
                continue
            else:
                list.append(i)
    return(list)
print('Prime numbers:', prime_nums(30))





