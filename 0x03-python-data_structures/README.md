New section read me

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for item in row:
            if item == row[-1]:
                print("{:d}".format(item), end="")
            else:
                print("{:d}".format(item), end=" ")
        print('')

This is a function called print_matrix_integer() that takes in a matrix as an argument and prints it to the console in a specific format. Here's how the function works:

The function takes a single argument called matrix, which is a list of lists containing integer values. The default value of this argument is an empty matrix.

The function uses two nested for loops to iterate over each row and column of the matrix.

For each item in the matrix, the function uses an if statement to check whether it is the last item in the row. If it is, the function prints the item without a trailing space character. Otherwise, the function prints the item with a trailing space character.

After printing all the items in a row, the function uses a print() function without any arguments to add a newline character and move to the next row.

Overall, this function can be used to print any matrix of integers in a specific format where each item is separated by a space and each row is printed on a separate line.

To use this function, you can call it with a matrix as an argument. For example:

python
Copy code
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix_integer(matrix)
This code will produce the following output:

Copy code
1 2 3
4 5 6
7 8 9


print a list in reverse order with 1 number per line in python

To print a list in reverse order with one number per line in Python, you can use the following code:

python
Copy code
my_list = [1, 2, 3, 4, 5]
for num in reversed(my_list):
    print(num)
Here, we have defined a list called my_list with some numbers. We are then using a for loop with the reversed() function to iterate over the list in reverse order. For each element in the reversed list, we are using the print() function to output it to the console on a separate line.

This code will produce the following output:

Copy code
5
4
3
2
1
You can replace the my_list variable with your own list to print it in reverse order with one number per line.




nathan94pillay@gmail.com
without using the reverse loop

You can also print a list in reverse order without using a loop by using slicing. Here's an example:

python
Copy code
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
for num in reversed_list:
    print(num)
Here, we are using the slice notation [::-1] to create a new list called reversed_list that contains the elements of my_list in reverse order. We are then using a for loop to iterate over reversed_list and print each element on a separate line using the print() function.

This code will produce the same output as the previous example:

Copy code
5
4
3
2
1
You can replace the my_list variable with your own list to print it in reverse order with one number per line.




