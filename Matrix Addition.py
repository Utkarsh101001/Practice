# Matrix Addition

def matrix_dimension(n):
    while True:
        try:
            value = int(input(f'Enter {n}: '))
            if value < 1:
                print('Number of rows Can\'t be Less Than 1.')
                continue
            return value
        except ValueError:
            print('Invalid Input! Please Try Again')
        
def matrix_input():
    while True:
        try:
            value = float(input('Enter Element: '))
            return value
        except ValueError:
            print('Invalid Input! Please Enter a Real Number') 
            
def matrix(m,n):
    matrix = []
    for i in range (m):
        matrix.append([])
    for i in range (m):
        for j in range (n):
            matrix[i].append(matrix_input())
    return matrix     
def matrix_sum(M,N):
    M_N = []
    if len(M) != len(N):
        return 'Given matrices don\'t have same dimension. Matrix addition is not valid'
    for i in range (len(M)):
        if len(M[i]) != len(N[i]):
            return 'Given matrices don\'t have same dimension. Matrix addition is not valid'
    for i in range (len(M)):
        M_N.append([])
    for i in range (len(M_N)):
        for j in range (len(M[i])):
            M_N[i].append(M[i][j] + N[i][j])
    return M_N                      
print('For Matrix 1:')
matrix_1 = matrix(matrix_dimension('Number of Rows'),matrix_dimension('Number of Columns'))
print('Matrix 1:',matrix_1)
print('For Matrix 2:')
matrix_2 = matrix(matrix_dimension('Number of Rows'),matrix_dimension('Number of Columns'))
print('Matrix 2:',matrix_2)
if type(matrix_sum(matrix_1,matrix_2)) == str:
    print(matrix_sum(matrix_1,matrix_2))
else:
    print(f'{matrix_1} + {matrix_2} = {matrix_sum(matrix_1,matrix_2)}')