const person = {
  name: ["Bob", "Smith"],
  age: 32,
  bio: function () {
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
  },
  introduceSelf: function () {
    console.log(`Hi! I'm ${this.name[0]}.`);
  },
};


Dot notation
Above, you accessed the object's properties and methods using dot notation. The object name (person) acts as the namespace — it must be entered first to access anything inside the object. Next you write a dot, then the item you want to access — this can be the name of a simple property, an item of an array property, or a call to one of the object's methods, for example:

person.age;
person.bio();
Copy to Clipboard
Objects as object properties
An object property can itself be an object. For example, try changing the name member from

const person = {
  name: ["Bob", "Smith"],
};
Copy to Clipboard
to

const person = {
  name: {
    first: "Bob",
    last: "Smith",
  },
  // …
};
Copy to Clipboard
To access these items you just need to chain the extra step onto the end with another dot. Try these in the JS console:

person.name.first;
person.name.last;
Copy to Clipboard
If you do this, you'll also need to go through your method code and change any instances of

name[0];
name[1];
Copy to Clipboard
to

name.first;
name.last;
Copy to Clipboard
Otherwise, your methods will no longer work.

Bracket notation
Bracket notation provides an alternative way to access object properties. Instead of using dot notation like this:

person.age;
person.name.first;
Copy to Clipboard
You can instead use brackets:

person["age"];
person["name"]["first"];
Copy to Clipboard
This looks very similar to how you access the items in an array, and it is basically the same thing — instead of using an index number to select an item, you are using the name associated with each member's value. It is no wonder that objects are sometimes called associative arrays — they map strings to values in the same way that arrays map numbers to values.

Dot notation is generally preferred over bracket notation because it is more succinct and easier to read. However there are some cases where you have to use brackets. For example, if an object property name is held in a variable, then you can't use dot notation to access the value, but you can access the value using bracket notation.

In the example below, the logProperty() function can use person[propertyName] to retrieve the value of the property named in propertyName.

const person = {
  name: ["Bob", "Smith"],
  age: 32,
};

function logProperty(propertyName) {
  console.log(person[propertyName]);
}

logProperty("name");
// ["Bob", "Smith"]
logProperty("age");
// 32





Setting object members
So far we've only looked at retrieving (or getting) object members — you can also set (update) the value of object members by declaring the member you want to set (using dot or bracket notation), like this:

person.age = 45;
person["name"]["last"] = "Cratchit";
Copy to Clipboard
Try entering the above lines, and then getting the members again to see how they've changed, like so:

person.age;
person["name"]["last"];
Copy to Clipboard
Setting members doesn't just stop at updating the values of existing properties and methods; you can also create completely new members. Try these in the JS console:

person["eyes"] = "hazel";
person.farewell = function () {
  console.log("Bye everybody!");
};
Copy to Clipboard
You can now test out your new members:

person["eyes"];
person.farewell();
// "Bye everybody!"
Copy to Clipboard
One useful aspect of bracket notation is that it can be used to set not only member values dynamically, but member names too. Let's say we wanted users to be able to store custom value types in their people data, by typing the member name and value into two text inputs. We could get those values like this:

const myDataName = nameInput.value;
const myDataValue = nameValue.value;
