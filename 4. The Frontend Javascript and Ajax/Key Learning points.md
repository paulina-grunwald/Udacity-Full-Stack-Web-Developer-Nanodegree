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
In order to use jQuery we need to use jQuery object. To select an object with jQuery we can use $ sign and in () we will pass string of the element we want.  e.g
```
var $wikiElem = $('#wikipedia-links');
```

# References

- [jQuery's AJAX Documentation](http://api.jquery.com/jquery.ajax/)
