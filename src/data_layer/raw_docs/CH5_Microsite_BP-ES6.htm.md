

# Working with ES6

The following topics describe best practices for working with ES6.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Default Parameters in ES6](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-ES6.htm\#)

In ES6, you can put the default values right in the signature of the functions.

Copy

```
var link = function(height = 50, color = 'red', url = 'http://azat.co') {
    ...
}
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Template Literals in ES6](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-ES6.htm\#)

Template literals or interpolation in other languages is a way to output variables in the string. In ES5, the string had to be broken as follows:

Copy

```
var name = 'Your name is ' + first + ' ' + last + '.';
var url = 'http://localhost:3000/api/messages/' + id;
```

In ES6, a new syntax ${NAME} can be used inside of the back-ticked string:

Copy

```
var name = `Your name is ${first} ${last}.`
var url = `http://localhost:3000/api/messages/${id}`
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Multiline Strings in ES6](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-ES6.htm\#)

In ES5, the following approaches had to be used:

Copy

```
var roadPoem = 'Then took the other, as just as fair,\n\t'
+ 'And having perhaps the better claim\n\t'
+ 'Because it was grassy and wanted wear,\n\t'
+ 'Though as for that the passing there\n\t'
+ 'Had worn them really about the same,\n\t'

var fourAgreements = 'You have the right to be you.\n\
You can only be you when you do your best.'
```

While in ES6, simply utilize the backticks:

Copy

```
var roadPoem = `Then took the other, as just as fair,
And having perhaps the better claim
Because it was grassy and wanted wear,
Though as for that the passing there
Had worn them really about the same,`

var fourAgreements = `You have the right to be you.
You can only be you when you do your best.`
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Arrow Functions in ES6](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-ES6.htm\#)

Using arrows functions in ES6 allows one to stop using that = this or self = this or \_this = this or .bind(this). For example, this code in ES5 is hard to read:

Copy

```
var _this = this
$('.btn').click(function(event){
    _this.sendData()
})
```

This is the ES6 code without \_this = this:

Copy

```
$('.btn').click((event) =>{
    this.sendData()
})
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Block-Scoped Constructs Let and Const](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-ES6.htm\#)

In ES6, let is used to restrict the scope to the blocks. Vars are function scoped.

Copy

```
function calculateTotalAmount (vip) {
    var amount = 0 // probably should also be let, but you can mix var and let
    if (vip) {
        let amount = 1 // first amount is still 0
    }
    return amount;
}
```

Const is immutable, and it’s also block-scoped like let.