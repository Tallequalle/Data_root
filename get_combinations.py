
import itertools
class MyList:
     def get_combinations(self, my_list):
        """
        :param self:
        :param my_list: list
        :return: list[list]
        """
        # YOUR CODE HERE
        list1= []
        for L in range(0, len(my_list) + 1):
            for subset in itertools.combinations(my_list, L):
                subset = list(subset)
                list1.append(subset)
        return(list1)

print('Combinations:', MyList().get_combinations([1, 2, 'a']))





