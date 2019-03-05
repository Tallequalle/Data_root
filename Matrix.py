import random
m = 5
n = 5
matrix = [[random.randint(0,10) for i in range(m)] for j in range(n)]
for i in matrix:
    print(i)
start = [0][0]
i = 0
j = 0
while (j != m) and (i != n):
    if j == m - 1 and i == n - 1:
        break
    else:
        if j == n - 1:
            start = matrix[j][i + 1]
            i += 1
            print(start)
        elif i == m - 1:
            start = matrix[j + 1][i]
            j += 1
            print(start)
        else:
            if matrix[j + 1][i + 1] < matrix[j + 1][i] and matrix[j + 1][i + 1] < matrix[j][i + 1]:
                start = matrix[j + 1][i + 1]
                i += 1
                j += 1
                print(start)
            elif matrix[j + 1][i] < matrix[j][i + 1] and matrix[j + 1][i] < matrix[j + 1][i + 1]:
                start = matrix[j + 1][i]
                j += 1
                print(start)
            elif matrix[j][i + 1] < matrix[j + 1][i] and matrix[j][i + 1] < matrix[j + 1][i + 1]:
                start = matrix[j][i + 1]
                i += 1
                print(start)
                
            else:
                if matrix[j][i + 1] == matrix[j + 1][i] and matrix[j][i + 1] < matrix[j + 1][i + 1]:
                    start = matrix[j][i + 1]
                    i += 1
                    print(start)
                else:
                    start = matrix[j + 1][i + 1]
                    j += 1
                    i += 1
                    print(start)






