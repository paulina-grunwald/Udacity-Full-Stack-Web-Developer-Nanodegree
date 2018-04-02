# Key Learning points for The Frontend: JavasSript & Ajax course

## Table of contents

1. Requests and APIS
2. Building the Move Planner App
3. Changing Expectations
4. Refractoring with Separation of Concepts
5. Using an Organization Library
6. Learning a New Codebase
7. Getting Started with the APIs
8. Understanding API Services
9. Using the APIs in Practice
10. References


# 1. Requests and APIS
``GET Request`` - An internet request for data. Sent from a client to a server.

``Response`` -  A server's response to a request. Sent from a server to a client. A response to a GET request will usually include data that the client needs to load the page's content.

- ``AJAX`` - Asynchronous Java And XML
- AJAX requests allow for content retrieval and display without reloading of the webpage.
- Asynchronous in AJAX means that the request doesn't block other request from happening.
- ``Get Request`` - an internet request for data send from client to server.
- ``Response`` - a server's response for request.
- Data:
  - XML <entry></entry>
  - JSON {property: data}
  - HTML >div></div>

- ``An asynchronous request`` can be fired off at any time (before or after a page has loaded) and the response to an asynchronous request often includes HTML that can be dynamically inserted into a page.
- AJAX - Asynchronous JavaScript And XML
- AJAX Response:
  - XML <entry></entry>
  - JSON {property: data}
  - HTML <div></div>

# 2. Building the Move Planner App

In order to use jQuery we need to use jQuery object. To select an object with jQuery we can use $ sign and in () we will pass string of the element we want (# sign is an ID)  e.g
```
var $wikiElem = $('#wikipedia-links');
```
We will be using two methods for AJAX requests:
- ``.ajax( url [, settings ] )`` - performs an asynchronous HTTP (Ajax) request. Accepts two parameters url and settings. Settings are a set of key/value pairs that configure the Ajax request. All settings are optional.
- ``.getJSON( url [, data ] [, success ] )`` - loads JSON-encoded data from the server using a GET HTTP request. Accepts three parameters url, data and success. Data are a plain object or string that is sent to the server with the request. Success is callback function that is executed if the request succeeds.

Now my task is to create Google Streetview request. Google Streetview image requests must include the size and location parameters.
I will be working with file set provided for the course. All files are located in minicourse-ajax-project folder. The folder includes index.html, folder containing css and js files.

Index.html include a form in which user inputs street name and city and submit the query. My task will be collect user input and to find Google Street image of the location inputted by the user. The ``form`` is constructed with following html code:

```HTML
<form id="form-container" class="form-container">
    <label for="street">Street: </label><input type="text" id="street" value="">
    <label for="city">City: </label><input type="text" id="city" value="">
    <button id="submit-btn">Submit</button>
</form>
```
The documentation for Google Street API can be found [here](https://developers.google.com/maps/documentation/streetview/).

We can observe that Street has id of ```id="street"``` and city has ``id="city"``. Now i will create new variables for street, city, address (city+street).
I will also create greeting for the user. Next, I will add url for the Google Streeview image.

```JavaScript
var streetStr = $('#street').val();
var cityStr  = $('#city').val();
var address = streetStr + ', ' + cityStr;

$greeting.text('Do you want to live in ' + address + '?');

//create URL
var streetviewUrl = 'http://maps.googleapis.com/maps/api/streetview?size=600x300&location=' + address + '';
$body.append('<img class="bgimg" src="' + streetviewUrl + '"/>');

```

Now using NY Times API key I will try to find articles regarding selected by user location and view them on the page together with the photo of the location.
For this I will use [NY Times ``API Key``](http://developer.nytimes.com/). My task will be to fire off AJAX request, iterate through response and present articles on the page inside <ul id="nytimes-articles"></ul>.


# 3. Changing Expectations

__Cat Clicker App:__

The goal of the exercise in this chapter is to create cat-clicker. The application should display few cats. Each cat includes the cat's name, a picture of the cat, text showing the number of clicks The specifics of the layout do not matter, so style it however you'd like. The number of clicks should increment when each cat picture is clicked.

 I used here .addEventListener to

 __Cat Clicker Premium:__
 The application should display:
 -  a list of at least 5 cats, listed by name,
 - an area to display the selected cat.

In the cat display area, the following should be displayed:
- the cat's name,
- a picture of the cat,
- text showing the number of clicks.

The specifics of the layout do not matter, so style it however you'd like.


# 4. Refactoring with Separation of Concepts
# 5. Using an Organization Library
# 6. Learning a New Codebase
# 7. Getting Started with the APIs
# 8. Understanding API Services
# 9. Using the APIs in Practice



# References

- [jQuery's AJAX Documentation](http://api.jquery.com/jquery.ajax/)
- http://api.jquery.com/jquery.ajax/
