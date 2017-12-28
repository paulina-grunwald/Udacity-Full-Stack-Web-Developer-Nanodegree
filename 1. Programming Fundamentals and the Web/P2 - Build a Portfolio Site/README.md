# Build a Portfolio Site
> by Paulina Grunwald

This project is a part of Udacity's full-stack [nanodegree program](https://www.udacity.com/nanodegree). For this project, I have built a personal portfolio website. I was provided a design mockup as a PDF-file, and had to replicate the design in HTML and CSS. Developing the portfolio website included display of images, adding description and links to completed project through the course  of my Nanodegree programe. I have roughly followed design mockup provided by Udacity but added many additional functionalities especially using Boostrap 4 and jquery.  

## Table of contents

- [Link to the project](#link-to-the-project)
- [Design and used code](#design-and-used-code)
- [References](#references)

## Link to the project

You can find all the files of my project here [downloaded here](https://github.com/paulina-grunwald/Udacity-Full-Stack-Web-Developer-Nanodegree/tree/master/P1%20-%20Movie%20Trailer%20Website).

## Design and used code

Below you can find steps I took to create my portfolio website:
1. Review Udacity  design mockup and decide which additional section can I add to my design.
2. Design high level portfolio on a piece of paper. I have separated the portfolio website in number of sections taking into the consideration that I will use Boostrap 4 grid system. This part was very important as I have discovered it's much easier to start writing code with concert high level design in mind.
3. Create index.html, style.css  and script.js files.
4. Create high level a skeleton of the website including navbar, various sections (main, my skills and experience , projects and contact).
5. Create responsive and collapsible navigation bar. Here I have used Boostrap 4 class navbar-collapse. I split items on my navbar using nav-item class. After that I have added styling in style.css file (that included color of the navbar when static and while hovering and clicking on it).
6. Add header section (htop class). Here I have added text and styled it using h1 and h3 headers. For h3 I have used google font Indie Flower which I have imported in the head using following code(For h4 I have used Domine Google font):
```html
<link href="https://fonts.googleapis.com/css?family=Indie+Flower" rel="stylesheet">
```
5. Add text to main and skills and experience section.
6. Create two rows with 3 images and text sections using Boostrap 4 grid. I made this grid responsive. It resizes with changing window size.
7. Add contact section. I have used E-mail, Facebook, Linkedin, Github icons provided [Font Awesome](http://fontawesome.io/icon/) in the contact section.
8. At the end I have added jquery code in script.js file in order to have smooth scroll transition when clicking on the different sections in the navbar.


## References
- https://www.sitepoint.com/javascript-media-queries/
- https://www.w3schools.com/howto/howto_js_topnav_responsive.asp
- [Mastering Bootstrap 4 by Laurence Svekis](https://www.safaribooksonline.com/library/view/mastering-bootstrap-4/9781787124141/)
- https://tympanus.net/codrops/2010/06/02/smooth-vertical-or-horizontal-page-scrolling-with-jquery/
- https://codepen.io/BuiltBySam/pen/merjWp
- https://designshack.net/images/designs/analytics-icon_1.jpg
- http://www.sveltia.com/wp-content/uploads/2016/04/background_slider_equipos.jpg
- http://www.aym-institute.com/wp-content/uploads/2013/10/Analytics-350x150.jpg
-https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwihnaLJ1qrYAhWGvhQKHX-8A8gQjBwIBA&url=https%3A%2F%2Fdzone.com%2Fstorage%2Ftemp%2F3110735-4-an-effective-leader.jpg&psig=AOvVaw3otyC1fgsDuuwj8Rl5J9Jz&ust=1514480725953829
- https://www.cloudways.com/blog/wp-content/uploads/GItCloudwaysSublime-THumb.jpg
- http://fontawesome.io/icon/facebook-square/
 https://stackoverflow.com/questions/31832227/jquery-smooth-scrolling-anchor-navigation
- https://www.drupal.org/project/bootstrap_agency/issues/2718871
- https://v4-alpha.getbootstrap.com/layout/grid/
- https://udacity.github.io/frontend-nanodegree-styleguide/css.html
