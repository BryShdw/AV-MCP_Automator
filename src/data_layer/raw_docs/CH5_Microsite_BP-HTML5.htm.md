

# Working with HTML5

The following topics describe best practices for working with HTML5.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Declare the DocType](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-HTML5.htm\#)

DocType is an instruction to the web browser (and is not an HTML tag) about the HTML version of a page. Always add the !DOCTYPE tag declaration to HTML documents so that the browser knows what type of document to expect.

Copy

```
<!-- HTML 5 -->
<!DOCTYPE html>
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Tags](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-HTML5.htm\#)

Always close HMTL tags. HTML is case insensitive. However, it is a recommended practice to use lower case for HTML tags.

The following tags cannot be closed: <img>, <input>, <br>, <hr>, and <meta>.

Code with closing tags is much more readable and easy to follow. It is much easier to visually inspect a page with well laid out markup.

Copy

```
<!-- Recommended -->
<h1> Heading</h1>
<p>some text.....</p>
```

Copy

```
<!-- Not Recommended -->
<H1>Heading</h1>
<p>some text.....
```

‘lang’ attribute: For internationalization purposes, always declare the default text language of a page in the <html> tag.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Descriptive Meta Tags](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-HTML5.htm\#)

#### <base> tag

The <base> tag is very useful, especially for developing in local servers. If you declare <base href="http://www.example.com/" />, then every link in the document will be relative, unless explicitly specified.

#### <title> tag

The <title> tag should never be omitted. Besides that the title of your document is not rendered on the browser tab, it is bad practice for accessibility.

#### Declare the Character Encoding

Do not forget the <meta charset='utf-8'> (or the declaration of the character encoding used in your document), as this will ensure that your page is always viewed correctly.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Avoid Inline Styles](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-HTML5.htm\#)

HTML is not a Hypertext styling language; CSS leaves the inline styles as a resource when required.

Copy

```
<h1 style="color:blue;">Is is really necessary?</h1>
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Have CSS Links in the <Head> Tag](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-HTML5.htm\#)

It has been tested and pages render faster when moving style sheet tags to the document head:

Copy

```
<head>
    <title>My Title</title>
    <link rel="stylesheet" type="text/css" media="screen" href="file.css"/>
    <link rel="stylesheet" type="text/css" media="screen" href="anotherFile.css"/>
</head>
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Placement of JavaScript Files](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-HTML5.htm\#)

If you have JavaScript files that are exclusive to add functionality to a page, it is better to place them at the end of the HTML file, right before the closing body tag. This will allow the page to load faster.

Copy

```
<body>
....
....
    <script type="text/javascript" src="path/to/file.js"></script>
</body>
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Use CSS in Place of JavaScript and Sprites](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-HTML5.htm\#)

With HTML5 and CSS3, it is possible to give native support for many components, effects, and techniques that previously could only be achieved through JavaScript. An example is the "css transition", which provides a visual transition between two states.

Copy

```
div.box {
    left: 40px;
    -webkit-transition: all 0.3s ease-out;
    -moz-transition: all 0.3s ease-out;
    -o-transition: all 0.3s ease-out;
    transition: all 0.3s ease-out;
}
div.box.totheleft {
    left: 0px;
}
div.box.totheright {
    left: 80px;
}
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Text Alternatives](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-HTML5.htm\#)

Provide text alternatives for any nontext content so that it can be changed into other forms people need, such as large print, braille, speech, symbols or a simpler language:

Copy

```
<img src="imageX.jpg" alt="A image of X." />
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Browser Support](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-HTML5.htm\#)

There is strong support for most of the new HTML5 tags, especially the block level ones. All you have to do to enable all the modern browsers to understand them is to include the following code in your CSS file.

Copy

```
article, aside, figcaption, figure, footer, header, nav, section
{
    display: block;
}
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Provide Fallbacks for Multimedia](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-HTML5.htm\#)

All browsers have their own limitations on what kind of media they can handle and how. That is why HTML5 allows for fallbacks with these elements through the <source> tag.

**Audio**

Copy

```
<audio controls>
    <source src=sound.ogg type=audio/ogg>
    <source src=sound.mp3 type=audio/mp3>
    <!-- fallback content: -->
    <a href=sound.ogg>Ogg</a>
    <a href=sound.mp3>MP3</a>
</audio>
```

**Video**

Copy

```
<video controls>
    <source src=video.webm type=video/webm>
    <source src=video.mp4 type=video/mp4>
    <!-- fallback content: -->
    <iframe width="480" height="360" src="#" frameborder="0" allowfullscreen></iframe>
</video>
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Simplify Your Forms](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-HTML5.htm\#)

HTML5 simplifies forms by removing the need for a closing slash on any input field and also by using semantic attributes to help form fields make more sense to the browser. At a minimum, an HTML5 form should follow these rules:

- Enclose all label names with the <label> tag.
- Use the new email and url input types to define these common fields.
- Use the placeholder attribute to provide input hints.
- Use the required attribute to request validation.
- Drop the name attribute in favor of an id where needed.

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Use HTML5 Block Level Elements](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-HTML5.htm\#)

Instead of staying with <div> tags for everything, use the new HTML5 elements like <header>, <footer>, <article>, and others. They work the same way but improve readability with less writing.

**Before HTML5**

Copy

```
<body>
    <div id="header">
    ...
    </div>
    <div id="main">
    ...
        <div id="subitem">
        ...
        </div>
    ...
    </div>
    <div id="footer">
    ...
    </div>
</body>
```

**After HTML5**

Copy

```
<body>
    <header>
    ...
    </header>
    <article>
    ...
        <section>
        ...
        </section>
    ...
    </article>
    <footer>
    ...
    </footer>
</body>
```

### [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Use the Appropriate Tags and Attributes](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BP-HTML5.htm\#)

#### Tags that Denote Style are Deprecated in HTML5 (Use CSS instead)

- Do not use <big>, <center>, <strike>, or <blink>, as they are deprecated. <blink> should be avoided regardless of this fact.
- Do not use <hgroup>, as it is obsolete.
- Do not use <i> for text in italics, <b> for bold, and <em> for emphasis.
- In general, it is recommended avoid stylistic elements in markup.
- The <br> element is not for layout. Do not use the <br> to format your document or to add space between elements. A rule of thumb here would be that, if it can be formatted by defining margin or padding in CSS, then you should not use <br>. If, however, you want to add line breaks within the same element, then <br> is appropriate.

Copy

```
<label>Please use the following text area:<br />
        <textarea name="loremipsum"></textarea>
</label>
```

#### Type Attribute is Not Necessary for Stylesheets and JavaScript Scripts

In HTML5, there is no need to define the type for <style> and <script> elements. All modern browsers expect that stylesheets will be CSS and scripts will be JavaScript. It is still a very common practice, since many popular CMS (content management systems) add these attributes automatically, but there’s no reason to do it in manually written code.

Consider using:

Copy

```
<link rel="stylesheet" href="style.css" />
<script src="script.js"></script>
```

Instead of:

Copy

```
<link type="text/css" rel="stylesheet" href="css/styles.css" />
<script type="text/javascript" src="js/scripts.js"></script>
```

#### Use the alt Attribute for Images

It is good practice to always use an alt attribute for your images. It provides an alternate text for when the image loading is disabled on the browser and it is extensively used by screen-readers.

#### Be Cautious with title Attributes

The title attribute is not interchangeable with the alt attribute. Alt is used instead of the image, while title is shown together with the image, usually as a tool tip.

The HTML5.1 recommendation warns against overusing the title attribute, due to lack of compatibility with a big percentage of browsers, like touch-only browsers in tablets and phones.

The following code show an adequate use of the title attribute:

Copy

```
<input type="text" title="search">
<input type="submit" value="search">
```

The following uses should be avoided:

Copy

```
<a href="text.txt" title="Relevant document">txt</a>
<img src="img.jpg" title="My photo" />
```

Instead consider naming your link appropriately and using the alt attribute for your picture:

Copy

```
<a href="text.txt">Relevant document</a>
<img src="img.jpg" alt="My photo" />
```

#### Indentation Consistency

A code with either a complete lack of indentation or inconsistent indentation lacks in readability. Use either spaces or tabs for indentation (recommended 2 tabs).

#### Spaces for class and ID Names

Never use spaces in the id attribute or for a class name.

#### Comments

Comments might affect code readability in a positive manner when used correctly. A good best practice is to create commenting closing tags (especially <div> closing tags) noting the class name of the opening tag. This makes it easy to know which block has been closed in nested tags.

Copy

```
<div class="myclass">
    <div class="nextclass">
    ...
    </div>
    <!-- .nextclass" -->
</div>
<!-- .myclass -->
```