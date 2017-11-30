# Key Learning points for assigment 1



## Table of contents

1.  HTML Syntax
2. CSS Syntax
3. Sixing
4. Positioning
5. Floats

## 1. HTML Syntax
- **h1-h6** represent headers. h1 header has the biggest size font and h6 the smallest.
- **< div >** is a division element
- **< p >** represents paragraph
- **< ul >** stands for unordered list and is used to contain the list. The list elements, **< li >**, are children of the unordered list. Each bullet point is its own **< li >** and the **< li >** elements must be children of the **< ul >** they can't be placed on their own.
- **< ol >** stands for ordered list.
- The relative path is similar to the absolute path, but it describes how to find to a file from a directory that is not the root directory. **< a href="http://labs.udacity.com/fend/example/hello-world.html">Hello, world!< /a>**
- In order to write a relative path from sciences.html to relativity.html, I only need to include the part of the path that describes how to get from science/ to relativity.html: **< a href="physics/relativity.html">Einstein's Special Relativity</a >**
- adding image to the website: **< img src="http://somewebsite.com/image.jpg" alt="short description" >**
- **Forms** allow users to interact with your site. Example of syntax:
**< form action="" method="">**
** <!-- stuff goes here --> </ form >**
The  **< input >** tag lets you add form fields for the user to enter their information.

## CSS Syntax
## Sixing
## Positioning

## Floats
- Floats are **not a positioning value**. They are a wholly different flow on the page created by a new property, float.
- Floats are commonly used to create grid-based layouts,


## Why Responsive
## Starting small

## Building up
- Responsive website changes based on the characteristic of the device.
- Media queries provide logic for applying different styles depending on the device characteristics. In order to use media query you need to add additional stylesheet on your page with media query.
```
<link rel="stylesheet href="styles.css">

```
