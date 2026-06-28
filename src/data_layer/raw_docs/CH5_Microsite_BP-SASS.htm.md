

# Working with SASS

The following best practices deal with SASS (Syntactically Awesome Style Sheets) implementation.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Structure Your Sass](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-SASS.htm\#)

It is very important to ensure that the site structure is correct from the beginning of the project.

Use ‘partials’ to break the CSS up into smaller more manageable blocks of code that are easier to maintain and develop. Partial files are created using an underscore and are not outputted as separate CSS files. Each partial should be imported using a master Sass file (global.scss) in the root of the Sass folder.

Copy

```
vendor/
base/
|
|-- _variables.scss
|-- _mixins.scss
|-- _placeholders.scss

framework/
modules/
global.scss
```

The following example shows a sample global.scss file:

Copy

```
/* VENDOR - Default fall-backs and external files.
========================================================================== */

@import 'vendor/_normalize.scss';

/* BASE - Base Variable file along with starting point Mixins and Placeholders.
========================================================================== */

@import 'base/_variables.scss';
@import 'base/_mixins.scss';
@import 'base/_placeholders.scss';

/* FRAMEWORK - Structure and layout files.
========================================================================== */

@import 'framework/_grid.scss';
@import 'framework/_breakpoints.scss';
@import 'framework/_layout.scss';

/* MODULES - Re-usable site elements.
========================================================================== */

@import 'modules/_buttons.scss';
@import 'modules/_lists.scss';
@import 'modules/_tabs.scss';
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Use Sass Variables More Effectively](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-SASS.htm\#)

Variables are one of the more straightforward features of Sass but are still on occasion used incorrectly. Creating a site-wide naming convention is essential when working with variables.

Here are some tips for creating useful variables:

- Don’t be vague when naming your variables.
- Have and stick to a naming convention (Modular, BEM, etc.)
- Ensure the variable use is justified.

Copy

```
$orange: #ffa600;
$grey: #f3f3f3;
$blue: #82d2e5;

$link-primary: $orange;
$link-secondary: $blue;
$link-tertiary: $grey;

$radius-button: 5px;
$radius-tab: 5px;
```

Avoid the following code:

Copy

```
$link: #ffa600;
$listStyle: none;
$radius: 5px;
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Reduce Mixin Usage](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-SASS.htm\#)

A mixin is a great way to include sections of code multiple times within a site. However, including a mixin is the same as copying and pasting the styles throughout the CSS file: It creates a mass of duplicate code and can bloat your CSS file.

A mixin, therefore, should only be used if an argument is present, to quickly create modified styles.

Copy

```
@mixin rounded-corner($arc) {
    -moz-border-radius: $arc;
    -webkit-border-radius: $arc;
    border-radius: $arc;
}
```

This rounded-corner mixin can be used in any situation simply by changing the value of $arc, making it a worthwhile mixin:

Copy

```
.tab-button {
    @include rounded-corner(5px);
}
.cta-button {
    @include rounded-corner(8px);
}
```

An example with suboptimal formatting might look like this:

Copy

```
@mixin cta-button {
    padding: 10px;
    color: #fff;
    background-color: red;
    font-size: 14px;
    width: 150px;
    margin: 5px 0;
    text-align: center;
    display: block;
}
```

This mixin has no argument and would therefore be better written as a placeholder. Placeholders are described in the following section.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Embrace Placeholders](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-SASS.htm\#)

Unlike mixins, placeholders can be used multiple times without adding any duplicate code. This makes them a much friendlier option for outputting DRY CSS:

Copy

```
%bg-image {
    width: 100%;
    background-position: center center;
    background-size: cover;
    background-repeat: no-repeat;
}
.image-one {
    @extend %bg-image;
    background-image:url("/img/image-one.jpg");
}
.image-two {
    @extend %bg-image;
    background-image:url("/img/image-two.jpg");
}
```

And the compiled CSS:

Copy

```
.image-one, .image-two {
    width: 100%;
    background-position: center center;
    background-size: cover;
    background-repeat: no-repeat;
}
.image-one {
    background-image:url("/img/image-one.jpg");
}
.image-two {
    background-image:url("/img/image-two.jpg");
}
```

The repeated code in the placeholder is output only once with only the unique styles being applied to the individual selectors. If unused, the placeholder styles are not output at all.

Placeholders can be used alongside mixins to reduce duplicate code and still keep the flexibility of a mixin.

Copy

```
/* PLACEHOLDER
============================================= */

%btn {
    padding: 10px;
    color:#fff;
    cursor: pointer;
    border: none;
    shadow: none;
    font-size: 14px;
    width: 150px;
    margin: 5px 0;
    text-align: center;
    display: block;
}

/* BUTTON MIXIN
============================================= */

@mixin btn-background($btn-background) {
    @extend %btn;
    background-color: $btn-background;
    &:hover {
        background-color: lighten($btn-background,10%);
    }
}

/* BUTTONS
============================================= */

.cta-btn {
    @include btn-background(green);
}
.main-btn {
    @include btn-background(orange);
}
.info-btn {
    @include btn-background(blue);
}
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Use Functions for Calculations](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-SASS.htm\#)

Functions are used to perform calculations. A Sass function does not output any CSS. Instead, it returns a value that can be used in the CSS. This is useful for calculations that will be made throughout the site.

For example, functions are useful for calculating the percentage width of a given element:

Copy

```
@function calculate-width ($col-span) {
    @return 100% / $col-span
}
.span-two {
    width: calculate-width(2); // spans 2 columns, width = 50%
}
.span-three {
    width: calculate-width(3); // spans 3 columns, width = 33.3%
}
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Order Work](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-SASS.htm\#)

Place all mixins, functions, placeholders, and variables in their relevant partial file. Keeping blocks of code together will ensure they are easy to edit and reuse in the future.

Site-wide elements should be kept together in a base folder. The base folder should contain global variables such as fonts and color schemes:

Copy

```
$font-primary: 'Roboto', sans-serif;
$font-secondary: Arial, Helvetica, sans-serif;

$color-primary: $orange;
$color-secondary: $blue;
$color-tertiary: $grey;
```

Module-specific mixins, functions, and variables should be kept within the correct module’s partial file:

Copy

```
$tab-radius: 5px;
$tab-color: $grey;
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Limit Nesting](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-SASS.htm\#)

Overusing nested rules in Sass can cause numerous issues, from complex code to over-specificity and too much reliance on the HTML structure of a page. These can cause issues further down the line and potentially increase the need for the inclusion of !important, which should generally be avoided.

Here are some key rules for nesting:

- Never go more than 3 levels deep.
- Ensure the CSS output is clean and reusable.
- Use nesting when it makes sense to, not as a default option.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Keep Code Simple](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-SASS.htm\#)

Keep your code as simple as possible. The purpose of Sass is to write cleaner more manageable CSS. Before creating any new mixins, variables, or functions, ensure that their presence will enhance development and not complicate things. All Sass features are useful when used in the correct situations and in moderation.