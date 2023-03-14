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
