

# Working with JavaScript

The following best practices deal with JavaScript implementation.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Strictly ‘use strict’](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

The “use strict” mode helps in a variety of ways. This directive imposes helps to control JavaScript programming by enforcing such things as declared variables, disallowing preserved keywords and preventing the use of with statements. The strict directive can be applied to an entire script or contained within the scope of a function.

When implementing use strict, it’s important to wrap it inside an anonymous function to avoid setting it globally, which can cause unexpected behaviors.

Copy

```
//myGreatApp.js
"use strict"; // could have unforeseen effects
(function (){
    "use strict";
    // do incredible things
})();
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Use === to Test Equality](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

When testing equality, a lot of languages with syntax similar to JavaScript use the double equals operator (==). However, in JavaScript you should always use triple equals (===). The difference is in how equality is determined. A triple equals operator evaluates the two items based upon their type and value; it makes no interpretations.

Copy

```
if(1 === '1') //Returns false
if(1 == '1') //Returns true

if(0 === '') //Returns false
if(0 == '') //Returns true
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Include All Necessary Semicolons](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

Always add the proper semicolons. A browser will usually put in semicolons where it thinks they are necessary. In some instances, the compiler might assume that a semicolon is not needed, which can introduce hard-to-find bugs into your code. Avoid this by always adding the proper semicolons. A good tool to help you check your JavaScript for forgotten semicolons is JSLint.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Use JSLint](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

As mentioned in the previous section, JSLint is a great tool for helping identify common problems in your JavaScript code. Visual Code has an add-in for JSLint that will allow you to check for errors at compile-time (or manually).

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Use a Namespace](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

When you first start using JavaScript, the temptation is to just declare everything and use it as needed. This places all of your functions and variables into the global scope. The problem with this, besides it being sloppy, is that it makes your code extremely vulnerable to being affected by other code. The solution to this is namespacing. To create a namespace, you simply declare a variable and then attach the properties and methods you want to it.

Copy

```
var MyNamespace = {};
MyNamespace.cost = 5;
//...time goes by...
console.log(MyNamespace.cost);
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Avoid Using Eval](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

The Eval function allows us to pass a string to the JavaScript compiler and have it execute as JavaScript. In simple terms, anything you pass in at runtime gets executed as if it were added at design time.

Copy

```
eval("alert('Hi');");
```

This code would cause an alert box to appear with the message "Hi" in it. The text inside the eval could have been passed in by the user or it could have been pulled from a database or other location.

There are a couple of reasons why the eval function should be avoided. First, it is significantly slower than design time code. Second, it is a security risk. When code is acquired and executed at runtime, it opens a potential threat vector for malicious programmers to exploit. Regardless, this function should be avoided at all costs.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Use Decimals Cautiously](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

When is 0.1 + 0.2 not equal to 0.3? When you do the calculation in JavaScript. The actual value of 0.1 + 0.2 comes out to be something like 0.30000000000000004. The reason for this is because JavaScript uses Binary Floating Point numbers. To get around this issue, you can multiply your numbers to remove the decimal portion. For instance, if you were to be adding up the cost of two items, you could multiply each price by 100 and then divide the sum by 100. Here is an example:

Copy

```
var hamburger = 8.20;
var fries = 2.10;
var total = hamburger + fries;
console.log(total); //Outputs 10.299999999999999

hamburger = hamburger * 100;
fries = fries * 100;
total = hamburger + fries;
total = total / 100;
console.log(total); //Outputs 10.3
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Start Blocks on the Same Line](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

JavaScript is designed in such a way that following the K&R style of formatting for blocks is a better idea. This format starts the opening curly brace on the same line as the preceding line of code.

Copy

```
if(myState === 'testing') {
    console.log('You are in testing');
}
else {
    console.log('You are in production');
}
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Use Explicit Blocks](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

Instead of using the shortcut, take the time necessary to turn this into the full notation. The final notation would look like this:

Copy

```
if (i > 3) {
    doSomething();
}
```

Now when anyone goes in to add additional logic, it becomes readily apparent where to put the code and what will happen when you do.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Declare All Variables First](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

JavaScript utilizes function-level scoping of variables and functions. When a variable is declared, the declaration statement gets hoisted to the top of the function. The same is true for functions.

Always declare your variables at the top of your function and declare your functions next, before you need to use them.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Do Not Use With](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

It is possible to shorten a long namespace using the with statement:

Copy

```
with (myNamespace.parent.child.person) {
    firstName = 'Jon';
    lastName = 'Smith';
}
```

That is equivalent to typing the following:

Copy

```
myNamespace.parent.child.person.firstName = 'Jon';
myNamespace.parent.child.person.lastName = 'Smith';
```

The problem is that there are times when this does not work as expected. Like many of the other common pitfalls of JavaScript, this will work fine in most circumstances. The better method of handling this issue is to assign the object to a variable and then reference the variable like so:

Copy

```
var p = myNamespace.parent.child.person;
p.firstName = 'Jon';
p.lastName = 'Smith';
```

This method works every time, which is what is desirable in a coding practice.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Be Careful Using typeof](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

Normally, typeof returns the string representation of the value type ('number', 'string', etc.) The problem comes in when evaluating NaN ('number'), null ('object'), and other odd cases. For example, here are a couple of comparisons that might be unexpected:

Copy

```
var i = 10;
i = i - 'taxi'; //Here i becomes NaN

if (typeof(i) === 'number') {
    console.log('i is a number');
}
else {
    console.log('You subtracted a bad value from i');
}
```

The resulting alert message would be "i is a number", even though clearly it is NaN (or "Not a Number"). If you were attempting to ensure the passed in value (here it is represented by 'taxi') subtracted from i was a valid number, you would get unexpected results.

While there are times when it is necessary to try to determine the type of a particular value, be sure to understand these (and other) peculiarities about typeof that could lead to undesirable results.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Treat parseInt With Care](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

Just like the typeof function, the parseInt function has quirks that need to be understood before it is used. If the first character is a number, parseInt will return all of the number characters it finds until it hits a nonnumeric character. Here is an example:

Copy

```
parseInt("56");    //Returns 56
parseInt("Joe");   //Returns NaN
parseInt("Joe56"); //Returns NaN
parseInt("56Joe"); //Returns 56
parseInt("21.95"); //Returns 21
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Use a Break in a Switch Statement](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

When you execute a switch statement, each case statement should be concluded by a break statement.

Copy

```
switch(i) {
    case 1:
    console.log('One');
    break;
    case 2:
    console.log('Two');
    break;
    case 3:console.log('Three');
    break;
    default:
    console.log('Unknown');
    break;
}
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Avoid For...In Loops](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

The For...In loop works as it is intended to work, but how it works can cause certain issues. The basic overview is that it loops through the attached, enumeration-visible members on an object. It does not simply walk down the index list like a basic for loop does. The following two examples are NOT equivalent:

Copy

```
// The standard for loop
for (var i = 0; i < arr.length; i++) {}
```

Copy

```
// The for...in loop
for(var i in arr) {}
```

In some cases, the output will act the same in the above two cases. That does not mean they work the same way. There are three major ways that for...in is different than a standard for loop. These are:

- It loops through all of the enumeration-visible members, which means it will pick up functions or other items attached to the object or its prototype.
- The order is not predictable (especially cross-browser).
- It is slower than a standard for loop.

If you fully understand for...in and know that it is the right choice for your specific situation, it can be a good solution. However, for the other 99% of situations, you should use a standard for loop instead. It will be quicker, easier to understand, and less likely to cause bugs that are hard to diagnose.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Declare Variables](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

Always be sure to declare variables.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Avoid Reserved or Special Words](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-JavaScript.htm\#)

JavaScript is rather flexible with what it allows you to do. This isn't always a good thing. For instance, when you create a function, you can specify that one of the parameters be named arguments. This will overwrite the arguments object that every function is given by inheritance.

There are also reserved words that will cause you issues when you attempt to run your application. Avoid using reserved words. Instead, use keywords that won't conflict with current or potential future reserved or special words.