README for new task

Write a function that computes the square value of all integers of a matrix.

Prototype: def square_matrix_simple(matrix=[]):
matrix is a 2 dimensional array
Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
Initial matrix should not be modified
You are not allowed to import any module
You are allowed to use regular loops, map, 

Sure, here's an implementation of the requested function:

python
Copy code
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    result_matrix = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
    
    # Square each integer in the input matrix and store the result in the corresponding cell of the result matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2
    
    return result_matrix
This function takes a matrix as input and returns a new matrix where each value is the square of the corresponding value in the input matrix. The function creates a new matrix with the same dimensions as the input matrix and then uses nested loops to square each integer in the input matrix and store the result in the corresponding cell of the new matrix. Finally, the function returns the new matrix.




nathan94pillay@gmail.com
#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x ** 2, row)) for row in matrix]

Yes, that implementation works as well! It uses a list comprehension to iterate through each row in the input matrix and applies a lambda function that squares each value in the row using the map() function. The resulting list of squared values is converted to a list using the list() function and added to a new matrix using another list comprehension. Finally, the new matrix is returned.

This implementation has the advantage of being more concise than the previous one I provided, as it uses list comprehensions and map() to perform the necessary operations. However, it may be less clear to readers who are not familiar with these constructs, so it's always a good idea to write code that is easy to read and understand.




nathan94pillay@gmail.com
please explain the map and list functions

Certainly!

map() is a built-in Python function that applies a given function to each element of an iterable (such as a list, tuple, or dictionary) and returns an iterator of the results. The syntax for map() is as follows:

python
Copy code
map(function, iterable)
The function parameter is the function to apply to each element of the iterable, and the iterable parameter is the iterable to apply the function to. The map() function returns an iterator of the results, which can be converted to a list or other data structure if desired.

For example, consider the following code:

python
Copy code
my_list = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x ** 2, my_list))
print(squared_list)
In this code, map() is used to apply a lambda function that squares each element of the my_list list. The resulting iterator is then converted to a list using the list() function and stored in the squared_list variable. The output of the code is [1, 4, 9, 16, 25], which is the list of squared values.

list() is a built-in Python function that converts an iterable (such as a tuple or iterator) to a list. The syntax for list() is simply:

python
Copy code
list(iterable)
For example, consider the following code:

python
Copy code
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)
In this code, list() is used to convert the my_tuple tuple to a list. The resulting list is then printed, and the output is [1, 2, 3, 4, 5].


Write a function that adds all unique integers in a list (only once for each integer).

Prototype: def uniq_add(my_list=[]):
You are not allowed to import any module

Sure, here's an implementation of the requested function:

python
Copy code
def uniq_add(my_list=[]):
    # Use a set to keep track of unique integers
    unique_integers = set()
    
    # Iterate through each element of the input list
    for element in my_list:
        # If the element is an integer and not already in the set, add it to the set
        if isinstance(element, int) and element not in unique_integers:
            unique_integers.add(element)
    
    # Compute the sum of the unique integers in the set
    sum_unique_integers = sum(unique_integers)
    
    return sum_unique_integers
This function takes a list as input and returns the sum of all unique integers in the list (that is, integers that appear only once in the list). The function uses a set to keep track of the unique integers and iterates through each element of the input list. If the element is an integer and not already in the set, it is added to the set. Finally, the function computes the sum of the unique integers in the set and returns the result.

Note that the function checks if each element is an integer using the isinstance() function, which returns True if the element is an instance of the specified class. This is necessary to avoid adding non-integer elements (such as strings or other objects) to the set.




nathan94pillay@gmail.com
explain set

Certainly!

In Python, a set is an unordered collection of unique elements. A set can contain any hashable object, such as integers, strings, or tuples (as long as the tuples contain only hashable objects). Sets are similar to lists and tuples, but they have two key differences:

Sets are unordered: unlike lists and tuples, sets do not have a defined order, which means that the elements of a set cannot be accessed by their position in the set.

Sets contain only unique elements: a set can contain each element only once, so if an element is already in the set, adding it again has no effect.

Sets are defined using curly braces {} or the set() function. For example, the following code creates a set containing three integers:

python
Copy code
my_set = {1, 2, 3}
or

python
Copy code
my_set = set([1, 2, 3])
The set() function can also be used to convert an iterable (such as a list or tuple) to a set.

Once a set is created, you can add and remove elements using the add() and remove() methods, respectively. For example:

python
Copy code
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
In this example, the add() method is used to add the integer 4 to the set, and the remove() method is used to remove the integer 2 from the set.

Sets also support various set operations such as union (|), intersection (&), and difference (-), which allow you to combine or compare sets in various ways.

In the implementation of the uniq_add() function I provided earlier, a set is used to keep track of the unique integers in the input list. The add() method is used to add each integer to the set, and the sum() function is used to compute the sum of the unique integers in the set.





Write a function that returns a set of common elements in two sets.

Prototype: def common_elements(set_1, set_2):
You are not allowed to import any module

Sure, here's an implementation of the requested function:

python
Copy code
def common_elements(set_1, set_2):
    # Use the & operator to compute the intersection of the two sets
    common_set = set_1 & set_2
    
    return common_set
This function takes two sets as input and returns a new set containing the common elements of the two sets (that is, elements that appear in both sets). The function uses the & operator to compute the intersection of the two sets, which returns a new set containing the elements that are common to both sets. Finally, the function returns the new set.

Note that sets in Python automatically remove duplicates, so the resulting set will not contain any duplicate elements. Also note that sets in Python are unordered, so the order of the elements in the resulting set may be different from the order of the elements in the input sets.




nathan94pillay@gmail.com
what is the operator to return unique elements in 2 sets

To return the unique elements in two sets (that is, elements that are in one set but not the other), you can use the symmetric difference operator ^. The ^ operator returns a new set containing the elements that are unique to each set, that is, the elements that are in one set or the other, but not in both.

Here's an example of how to use the ^ operator:

python
Copy code
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
unique_set = set_1 ^ set_2
print(unique_set)
In this example, the two input sets are set_1 and set_2. The ^ operator is used to compute the symmetric difference of the two sets, which returns a new set containing the elements that are unique to each set: {1, 4}. The resulting set unique_set is then printed to the console.

Note that, as with the intersection operator &, the ^ operator returns a new set and does not modify the original sets. Also note that sets in Python are unordered, so the order of the elements in the resulting set may be different from the order of the elements in the input sets.
