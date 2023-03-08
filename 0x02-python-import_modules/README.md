Modules read me

nathan94pillay@gmail.com
what does sys do args = len(sys.argv)

The sys module in Python provides access to some variables and functions that interact with the Python interpreter. The sys.argv variable is a list in Python that contains the command-line arguments passed to the script. The first element of this list (sys.argv[0]) is the name of the script itself, and the following elements contain any additional arguments passed to the script.

The code args = len(sys.argv) assigns the number of command-line arguments passed to the script (excluding the script name itself) to the variable args. The len() function is used to determine the length of the list sys.argv, which corresponds to the number of arguments passed. Therefore, args will contain an integer representing the number of command-line arguments passed to the script.




nathan94pillay@gmail.com
if __name__ == "__main__":

In Python, the if __name__ == "__main__": condition is commonly used at the end of a script to specify code that should only be executed when the script is run directly (i.e., not imported as a module).

Here's how it works:

When a Python script is run, Python sets the special __name__ variable to the string "__main__".
When a script is imported as a module into another script, the __name__ variable is set to the name of the module (i.e., the name of the script file without the .py extension).
Therefore, by including the if __name__ == "__main__": condition at the end of a script, you can ensure that certain code is only executed when the script is run directly, and not when it's imported as a module into another script.

For example, you might use this condition to define and run some tests for your script, or to execute some demo code that showcases the functionality of your script.




nathan94pillay@gmail.com
Write a program that prints #pythoniscool, followed by a new line, in the standard output.

Your program should be maximum 2 lines long
You are not allowed to use print or eval or open or import sys in your file 101-easy_print.py

Here's a one-liner Python code that will print the required string:

python
Copy code
import os; os.write(1, b"#pythoniscool\n")
Here, we are importing the os module and using its write() function to write the string #pythoniscool\n to standard output (represented by file descriptor 1). The string is encoded as bytes using the b prefix. Finally, we end the string with a newline character (\n) to ensure that the output is on a new line.




nathan94pillay@gmail.com
Write a program that prints the alphabet in uppercase, followed by a new line.

Your program should be maximum 3 lines long
You are not allowed to use:
any loops
any conditional statements
str.join()
any string literal
any system calls

Here's a one-liner Python code that will print the uppercase alphabet:

python
Copy code
import string; print(string.ascii_uppercase)
Here, we are importing the string module and using its ascii_uppercase attribute, which is a pre-defined string that contains all the uppercase ASCII letters in alphabetical order. We are then using the print() function to output the string to the console, which will automatically add a newline character at the end.
