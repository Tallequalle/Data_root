
import numpy as np
import pandas as pd

def sorted_df(data, labels):
    """
    :param data: dict
    :param labels: list[str]
    :return: pandas.core.frame.DataFrame 
    """
    # YOUR CODE HERE
    dataframe = pd.DataFrame(data,index = labels)
    dataframe.sort_values(['age', 'weight'], ascending=[False, True],inplace = True)
    return(dataframe)
data = {'animal': ['cat', 'cat', 'dog', 'dog', 'cat', 'cat', 'dog', 'cat', 'dog', 'dog'],
        'age': [2.5, 1, 0.5, np.nan, 5, 2, 3.5, np.nan, 7, 3],
        'weight': [1, 3, 6, 8, 4, 3, 10, 2, 7, 3],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 

sorted_df(data, labels)






