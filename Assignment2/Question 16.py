#Write a program that takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#Code

row_number = int(input("Input number of rows: "))
col_number = int(input("Input number of columns: "))

array = [[0 for column in range(col_number)] for row in range(row_number)]
for row in range(row_number):
    for column in range(col_number):
        array[row][column]= row*column
print(array)
