NEW READ

class Person {
  // define the Person class

  name; // declare a property called "name"

  constructor(name) {
    // define the constructor method that takes a "name" parameter
    this.name = name; // assign the "name" parameter to the "name" property of the object
  }

  introduceSelf() {
    // define a method called "introduceSelf"
    console.log(`Hi! I'm ${this.name}`); // log a message to the console that includes the "name" property of the object
  }
}

This is a JavaScript class called Person that has a constructor method and an instance method.

The constructor method takes in a name parameter and assigns it to the name property of the Person object being created.

The introduceSelf() method logs a message to the console that includes the name property of the Person object.

=========================================================================

In the constructor method of the Person class, there is a parameter named name. When a new Person object is created, the value passed as an argument to the constructor will be assigned to the name parameter.

The this keyword refers to the object being created, so this.name refers to the name property of that object. By assigning the name parameter to this.name in the constructor, we are setting the value of the name property of the object to the value passed as an argument to the constructor.

In other words, when a new Person object is created with new Person("John"), the name parameter will be set to "John", and the name property of the Person object will also be set to "John". This property can be accessed and modified later by other methods of the Person class or by external code that has a reference to the Person object.


After declaring constructor method and assigning the name parameter to this this.name in the constructor 

- we can use a new person called giles

const giles = new Person('Giles');

giles.introduceSelf(); // Hi! I'm Gilesi

==========================================



Omitting constructors
If you don't need to do any special initialization, you can omit the constructor, and a default constructor will be generated for you:

class Animal {

  sleep() {
    console.log('zzzzzzz');
  }

}

const spot = new Animal();

spot.sleep(); // 'zzzzzzz'
Copy to ClipboardCopy to Clipboard
Inheritance
Given our Person class above, let's define the Professor subclass.

=========================================

class Professor extends Person {

  teaches;

  constructor(name, teaches) {
    super(name);
    this.teaches = teaches;
  }

  introduceSelf() {
    console.log(`My name is ${this.name}, and I will be your ${this.teaches} professor.`);
  }

  grade(paper) {
    const grade = Math.floor(Math.random() * (5 - 1) + 1);
    console.log(grade);
  }

}


The professor class adds a new property teaches, so we declare that.

Since we want to set teaches when a new Professor is created, we define a constructor, which takes the name and teaches as arguments. The first thing this constructor does is call the superclass constructor using super(), passing up the name parameter. The superclass constructor takes care of setting name. After that, the Professor constructor sets the teaches property.

Note: If a subclass has any of its own initialization to do, it must first call the superclass constructor using super(), passing up any parameters that the superclass constructor is expecting.



With this declaration we can now create and use professors:

const walsh = new Professor('Walsh', 'Psychology');
walsh.introduceSelf();  // 'My name is Walsh, and I will be your Psychology professor'

walsh.grade('my paper'); // some random grade


============================================

In JavaScript, the Math object provides a set of built-in methods that allow you to perform mathematical operations. You can use the Math object and its methods directly in your JavaScript code by calling them with the dot notation.

Here are some examples of using the Math object in JavaScript:

Using Math.random() to generate a random number between 0 and 1:
javascript
Copy code
const randomNumber = Math.random();
console.log(randomNumber); // Output: a random number between 0 and 1

Using Math.floor() to round down a number to the nearest integer:
javascript
Copy code
const number = 5.7;
const roundedDownNumber = Math.floor(number);
console.log(roundedDownNumber); // Output: 5

Using Math.ceil() to round up a number to the nearest integer:
javascript
Copy code
const number = 5.1;
const roundedUpNumber = Math.ceil(number);
console.log(roundedUpNumber); // Output: 6

Using Math.abs() to get the absolute value of a number:
javascript
Copy code
const number = -5;
const absoluteValue = Math.abs(number);
console.log(absoluteValue); // Output: 5

These are just a few examples of the many methods available in the Math object. You can refer to the JavaScript documentation to learn more about the different methods and how to use them.




=========================================


Here's a declaration of the Student class that does just that:

class Student extends Person {

  #year;

  constructor(name, year) {
    super(name);
    this.#year = year;
  }


  introduceSelf() {
    console.log(`Hi! I'm ${this.name}, and I'm in year ${this.#year}.`);
  }

  canStudyArchery() {
    return this.#year > 1;
  }

}
Copy to ClipboardCopy to Clipboard
In this class declaration, #year is a private data property. We can construct a Student object, and it can use #year internally, but if code outside the object tries to access #year the browser throws an error:

const summers = new Student('Summers', 2);

summers.introduceSelf(); // Hi! I'm Summers, and I'm in year 2.
summers.canStudyArchery(); // true

summers.#year; // SyntaxError
Copy to ClipboardCopy to Clipboard
Private data properties must be declared in the class declaration, and their names start with #.


===========================================

Private methods
You can have private methods as well as private data properties. Just like private data properties, their names start with #, and they can only be called by the object's own methods:

class Example {
  somePublicMethod() {
    this.#somePrivateMethod();
  }

  #somePrivateMethod() {
    console.log('You called me?');
  }
}

const myExample = new Example();

myExample.somePublicMethod(); // 'You called me?'

myExample.#somePrivateMethod(); // SyntaxError

===================================
Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h

module.exports = class Rectangle {
constructor(w, h) {
this.width = w;
this.height = h;
}}



Sure, here's an example of a Rectangle class that defines a rectangle:

javascript
Copy code
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // If w or h is equal to 0 or not a positive integer, create an empty object
      return {};
    }
    this.width = w; // Initialize the instance attribute width with the value of w
    this.height = h; // Initialize the instance attribute height with the value of h
  }
}




Create an instance method called rotate() that exchanges the width and the height of the rectangle

Sure! Here's an example implementation of the rotate() method for a Rectangle class that exchanges the width and height:

ruby
Copy code
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def rotate(self):
        self.width, self.height = self.height, self.width
In this implementation, we define a Rectangle class with a constructor that takes a width and height parameter. We also define an instance method called rotate() that swaps the width and height values using tuple unpacking. The method doesn't return anything, but it modifies the width and height attributes of the rectangle instance.

Here's an example usage of this implementation:

python
Copy code
# Create a new rectangle with width=10 and height=5
rect = Rectangle(10, 5)

# Print the original width and height
print(f"Width: {rect.width}, Height: {rect.height}")  # Output: Width: 10, Height: 5

# Rotate the rectangle
rect.rotate()

# Print the new width and height
print(f"Width: {rect.width}, Height: {rect.height}")  # Output: Width: 5, Height: 10
In this example, we create a new rectangle with a width of 10 and a height of 5. We print the original width and height using an f-string, and then we call the rotate() method to swap the values. Finally, we print the new width and height using another f-string to confirm that the rotate() method worked correctly.




nathan94pillay@gmail.com
in java script

Sure! Here's an example implementation of the rotate() method for a Rectangle class in JavaScript that exchanges the width and height:

kotlin
Copy code
class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  rotate() {
    [this.width, this.height] = [this.height, this.width];
  }
}
In this implementation, we define a Rectangle class with a constructor that takes a width and height parameter. We also define an instance method called rotate() that swaps the width and height values using array destructuring. The method doesn't return anything, but it modifies the width and height attributes of the rectangle instance.

Here's an example usage of this implementation:

javascript
Copy code
// Create a new rectangle with width=10 and height=5
const rect = new Rectangle(10, 5);

// Print the original width and height
console.log(`Width: ${rect.width}, Height: ${rect.height}`);  // Output: Width: 10, Height: 5

// Rotate the rectangle
rect.rotate();

// Print the new width and height
console.log(`Width: ${rect.width}, Height: ${rect.height}`);  // Output: Width: 5, Height: 10
In this example, we create a new rectangle with a width of 10 and a height of 5. We print the original width and height using a template literal, and then we call the rotate() method to swap the values. Finally, we print the new width and height using another template literal to confirm that the rotate() method worked correctly.




nathan94pillay@gmail.com
Create an instance method called double() that multiples the width and the height of the rectangle by 2 in java script

Sure! Here's an example implementation of the double() method for a Rectangle class in JavaScript that multiplies the width and height by 2:

kotlin
Copy code
class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}
In this implementation, we define a Rectangle class with a constructor that takes a width and height parameter. We also define an instance method called double() that multiplies the width and height values by 2. The method doesn't return anything, but it modifies the width and height attributes of the rectangle instance.

Here's an example usage of this implementation:

javascript
Copy code
// Create a new rectangle with width=10 and height=5
const rect = new Rectangle(10, 5);

// Print the original width and height
console.log(`Width: ${rect.width}, Height: ${rect.height}`);  // Output: Width: 10, Height: 5

// Double the rectangle
rect.double();

// Print the new width and height
console.log(`Width: ${rect.width}, Height: ${rect.height}`);  // Output: Width: 20, Height: 10
In this example, we create a new rectangle with a width of 10 and a height of 5. We print the original width and height using a template literal, and then we call the double() method to multiply the values by 2. Finally, we print the new width and height using another template literal to confirm that the double() method worked correctly.




nathan94pillay@gmail.com
#!/usr/bin/node

const parentSquare = require('./5-square');

module.exports = class Square extends parentSquare {
  charPrint (c) {
    if (!c) {
      this.print();
      return;
    }
    for (let row = 0; row < this.height; row++) console.log(c.repeat(this.width));
  }
};

This is an example implementation of a Square class in Node.js that extends a Square class from another module and adds an instance method called charPrint(c) that prints the square using a specific character:

javascript
Copy code
#!/usr/bin/node

// Import the parentSquare module
const parentSquare = require('./5-square');

// Define the Square class that extends parentSquare
module.exports = class Square extends parentSquare {
  // Define the charPrint method
  charPrint(c) {
    // If no character is provided, call the parent print method
    if (!c) {
      this.print();
      return;
    }
    // Otherwise, print the square using the provided character
    for (let row = 0; row < this.height; row++) {
      console.log(c.repeat(this.width));
    }
  }
};
In this implementation, we first import a Square class from another module using the require() function. Then, we define a new Square class that extends the parent Square class using the extends keyword. We add an instance method called charPrint(c) that takes a character parameter c and prints the square using that character.

If no character is provided, the method calls the parent print() method to print the square using the default character. Otherwise, it uses a for loop to print the square row by row, with each row consisting of c repeated this.width times.

Here's an example usage of this implementation:

scss
Copy code
// Import the Square module
const Square = require('./6-square');

// Create a new square with size 3
const square = new Square(3);

// Print the square using the default character
square.charPrint();  // Output: 
                     // ***
                     // ***
                     // ***

// Print the square using the character "X"
square.charPrint('X');  // Output: 
                        // XXX
                        // XXX
                        // XXX
In this example, we import the Square module that we just defined, create a new Square instance with a size of 3, and call the charPrint() method twice to print the square using the default character and the character "X". The output shows the square printed using the corresponding characters.




nathan94pillay@gmail.com
Write a function that returns the number of occurrences in a list:

Prototype: exports.nbOccurences = function (list, searchElement)

Sure! Here's an example implementation of a function that returns the number of occurrences of a search element in a list:

javascript
Copy code
exports.nbOccurences = function(list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
In this implementation, we define an nbOccurences function that takes two parameters: a list array and a searchElement value. We initialize a count variable to 0, and then loop through each element of the list using a for loop. For each element, we check if it is equal to the searchElement. If it is, we increment the count variable. Finally, we return the count value.

Here's an example usage of this function:

javascript
Copy code
const { nbOccurences } = require('./myModule');

const myList = [1, 2, 3, 4, 5, 2, 2, 3];
const searchValue = 2;

const count = nbOccurences(myList, searchValue);
console.log(`The value ${searchValue} occurs ${count} times in the list.`);
In this example, we first import the nbOccurences function from a module using destructuring assignment. We then define a myList array and a searchValue variable. We call the nbOccurences function with these parameters to get the count of occurrences of the search value in the list. Finally, we print the count using a template literal. The output shows the count of occurrences of the search value in the list.




nathan94pillay@gmail.com
print list in reverse order without using reverse method

Sure! Here's an example implementation of a function that prints a list in reverse order without using the built-in reverse() method:

javascript
Copy code
function printReverse(list) {
  for (let i = list.length - 1; i >= 0; i--) {
    console.log(list[i]);
  }
}
In this implementation, we define a printReverse function that takes a list parameter. We use a for loop to iterate over the elements of the list in reverse order. We start the loop from the last index of the list (list.length - 1) and decrement the index until we reach the first element (0). For each index, we print the corresponding element using the console.log() method.

Here's an example usage of this function:

scss
Copy code
const myList = [1, 2, 3, 4, 5];
printReverse(myList);
In this example, we define a myList array and call the printReverse() function with this array as the parameter. The output shows the elements of the array printed in reverse order:

Copy code
5
4
3
2
1



nathan94pillay@gmail.com
Write a function that prints the number of arguments already printed and the new argument value. (see example below)

Prototype: exports.logMe = function (item)
Output format: <number arguments already printed>: <current argument value>

Sure! Here's an example implementation of a function that prints the number of arguments already printed and the new argument value:

javascript
Copy code
let numArgs = 0;

exports.logMe = function(item) {
  console.log(`${numArgs}: ${item}`);
  numArgs++;
};
In this implementation, we define a numArgs variable to keep track of the number of arguments already printed. We define an logMe function that takes an item parameter. Within the function, we print a message using console.log() that includes the current value of numArgs and the value of the item parameter. We then increment the numArgs variable so that the count is updated for the next call of the function.

Here's an example usage of this function:

scss
Copy code
const { logMe } = require('./myModule');

logMe("Hello");
logMe("world");
logMe("!");

// Output:
// 0: Hello
// 1: world
// 2: !
In this example, we import the logMe function from a module using destructuring assignment. We then call the logMe function three times with different string arguments. The output shows the number of arguments already printed and the value of the current argument for each call of the function.




