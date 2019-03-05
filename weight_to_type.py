
import numpy as np
import pandas as pd

def weight_to_type(data, labels):    
    """
    :param data: dict
    :param labels: list[str]
    :return: dict
    """
    # YOUR CODE HERE
    # YOUR CODE HERE
    dataframe = pd.DataFrame(data,index = labels)
    columns = dataframe.columns
    mean_cat = 0
    quantity_cat = 0
    mean_dog = 0
    quantity_dog = 0
    dic = {}
    for i in range(len(dataframe['animal'])):
        if dataframe['animal'][i] == 'cat':
            quantity_cat += 1
            mean_cat += dataframe['weight'][i]
            dic['cat'] = mean_cat/quantity_cat
        elif dataframe['animal'][i] == 'dog':
            quantity_dog += 1
            mean_dog += dataframe['weight'][i]
            dic['dog'] = mean_dog/quantity_dog
    mean_dog = mean_dog/quantity_dog
    mean_cat = mean_cat/quantity_cat 
    return(dic)
    
    
data = {'animal': ['cat', 'cat', 'dog', 'dog', 'cat', 'cat', 'dog', 'cat', 'dog', 'dog'],
        'age': [2.5, 1, 0.5, np.nan, 5, 2, 3.5, np.nan, 7, 3],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no'],
        'weight': [1, 3, 6, 8, 4, 3, 10, 2, 7, 3]}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print('weight_to_type', weight_to_type(data, labels))




