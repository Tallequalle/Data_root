import numpy as np
import pandas as pd

def repl_nan(data, labels):    
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
    for i in range(len(dataframe['animal'])):
        if dataframe['animal'][i] == 'cat' and np.isnan(dataframe['age'][i]) == False:
            quantity_cat += 1
            mean_cat += dataframe['age'][i]
        elif dataframe['animal'][i] == 'dog' and np.isnan(dataframe['age'][i]) == False:
            quantity_dog += 1
            mean_dog += dataframe['age'][i]
    mean_dog = mean_dog/quantity_dog
    mean_cat = mean_cat/quantity_cat 
    for i in range(len(dataframe['animal'])):
        if dataframe['animal'][i] == 'cat' and np.isnan(dataframe['age'][i]) == True:
            dataframe['age'][i] = mean_cat
        elif dataframe['animal'][i] == 'dog' and np.isnan(dataframe['age'][i]) == True:
            dataframe['age'][i] = mean_dog
    return(dataframe)
    
data = {'animal': ['cat', 'cat', 'dog', 'dog', 'cat', 'cat', 'dog', 'cat', 'dog', 'dog'],
        'age': [2.5, 1, 0.5, np.nan, 5, 2, 3.5, np.nan, 7, 3],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no'],
        'weight': [1, 3, 6, 8, 4, 3, 10, 2, 7, 3]}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
repl_nan(data, labels)




