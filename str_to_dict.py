def str_to_dict(some_str):  
    """
    :param some_str: str
    :return: dict
    """
    length = len(some_str)
    save = 0
    counter = 0
    dict = {}
    while counter < length:
        save = some_str[0]
        total = 0
        counter2 = 0
        while counter2 < len(some_str):
            if save == some_str[counter2]:
                total += 1
            counter2 += 1
        dict[save] = total
        some_str = some_str.replace(save,'')
        counter += 1
        if (len(some_str) == 0):
            break
    return(dict)
        
            
print('Str to dict:', str_to_dict('dataroot_university'))



