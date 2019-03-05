class Conv:
    def to_roman(self, num):    
        """
        :param self:
        :param n: int
        :return: str    
        """
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        syb = [
            'M', 'CM', 'D', 'CD',
            'C', 'XC', 'L', 'XL',
            'X', 'IX', 'V', 'IV',
            'I'
        ]
        # YOUR CODE HERE
        list_val = []
        i = 0
        while num != 0:
            while i < len(val):
                if num//val[i] == 1:
                    break
                i += 1
            list_val.append(syb[i])
            num = num - val[i]
        answer = ''
        for i in list_val:
            answer += i
        return(answer)
print('Converted:', Conv().to_roman(44))



