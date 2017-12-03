# Key Learning points from HTML and CSS SYNTAX


## Table of contents

1. HTML Syntax
2. HTML Syntax Problem Set
3. CSS Syntax
4. CSS Syntax Problem Set


## 1. HTML Syntax
- Paragraph element: __<p>This is paragraph</p>__
- Span ``< span>`` is a line of text.
- Code should be written in the plain text.
- IDE - Integrated Development Enviroment
- To make the text bold we can use ```__<b></b>__```
- To emphasise text we can use ```__<i></i>__```
- __DOCTYPE__: Describes the type of HTML.
- ```<head>``` describes the website and links to other files the browser needs to render website correctly e.g title, associated CSS, JavaScript, charset etc.
- ```<ul>``` is used for unordered lists and ```<ol>``` for unordered.
- To create path referring to another file we use following code: ```<a href="example/filename.html">Example path</a>```
- A image can be added using following code: ```<img src="http://somewebsite.com/image.jpg" alt="short description">```
- A caption can be associated with the <figure> element by inserting a <figcaption> inside it (as the first or the last child).
- The __< form>__  tag contain all of the code for the form. The form fields, the buttons, etc. need to be enclosed inside these tags.
```<form action="" method="">
<!-- stuff goes here -->
</form>
```
- The __< input>__ tag lets you add form fields for the user to enter their information
-  __< textarea>__ tag is similar to ```<input type="text">``` but you can use it to create a multi-line text input box for your user.
- The __< label>__ tag adds text to an __< input>___ field so the user knows what information is being asked for e.g
```<label for="name">What is your name?</label> <input type="text" id="name">
```


## 2. HTML Syntax Problem Set
- To create button we need to use following code: ```<button>Click me</button>```

## 3. CSS Syntax

- All CSS starts with rule set which is made of two parts: selector and declaration block.
- this is the format of CSS comment: ```/* add CSS here */```.
- This is the format for HTML comments: ``` <!-- This is a comment -->```.
- Attributes are very heplful in style adjustment. Attributes help us to describe content of a page inside HTML markup.
- __Id__ can be used only once per page. __Class__ can be used multiple times on one page.
- HTML elements can have mutiple classes assigned to them.
- __Tag Selector__
```
h1 {
  color: green;
}
```

- __class Attribute Selector__
```
.book-summary {
  color: blue;
}
```
- __id attribute Selector__
```
#site-description {
  color: red;
}
```
- CSS Units:
  - Absolute (e.g px, mm, cm)
  - Relative (%, em, vw, vh)
- RGB (red, green, blue -> 0-255)
- The Hexadecimal Numeral System

## 4. CSS Syntax Problem Set
- It is recommended to write your CSS in a file called a stylesheet and then link to that file in your HTML.
- In order to link stylesheet file with your index.html you need add following code in the <head> of your index.html file:
```
<link href="path-to-stylesheet/stylesheet.css" rel="stylesheet">
```
