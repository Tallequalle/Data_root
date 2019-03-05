import numpy as np
import pandas as pd
def kittens(data, labels):    
    """
    :param data: dict
    :param labels: list[str]
    :return: pandas.core.frame.DataFrame 
    """
    # YOUR CODE HERE
    dataframe = pd.DataFrame(data,index = labels)
    columns = dataframe.columns
    mean_cat = 0
    quantity_cat = 0
    mean_dog = 0
    quantity_dog = 0
    for i in labels:
        if dataframe['animal'][i] != 'cat' or dataframe['age'][i] > 3 or np.isnan(dataframe['age'][i]) == True:
            dataframe.drop(i,axis = 0,inplace = True)
    return(dataframe)
    
data = {'animal': ['cat', 'cat', 'dog', 'dog', 'cat', 'cat', 'dog', 'cat', 'dog', 'dog'],
        'age': [2.5, 1, 0.5, np.nan, 5, 2, 3.5, np.nan, 7, 3],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no'],
        'weight': [1, 3, 6, 8, 4, 3, 10, 2, 7, 3]}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
kittens(data, labels)

