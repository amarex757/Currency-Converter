### Conceptual Exercise - Ammaar Janjua 
*Answer questions below*

- What are important differences between Python and JavaScript?

##### Python is a strongly-typed language which supports strong and dynamic typing. It is mainly used for backend situations. Javascript is a weakly-typed programming language in terms of implicit conversion. It is mainly used for front-end language purposes.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

##### Either using key, get(), or the setdefault() method. 

- What is a unit test?
  
##### A way of testing a unit - the smallest piece of code that can be logically isolated in a system. They test "one" unit of functionality. 

- What is an integration test?
  
##### Integration testing exercises two or more parts of an application at once, including the interactions between the parts, to determine if they function as intended. Test that components work together. 

- What is the role of web application framework, like Flask?
  
##### A web server is a digital tool that can process requests and issue responses via HTTP, a protocol used to distribute information on the world wide web. Flask is a Python module that lets you develop web applications easily. Flask is a type of web framework. Flask is capable of running HTTP requests on the public world wide web, private LAN, and private WANs and accepts GET and POST requests.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

##### /foods/pretzel would be predefined as /foods/X/ could be any food. This is better for the subject matter of the page. 'foods?type=pretzel' is better suited for search-based routing. This often is used with form data.

- How do you collect data from a URL placeholder parameter using Flask?

##### Flask lets you 'route' a URL to a function. For example in `@app.route('authors/<username>')` '<username>' is the  variable that will be replaced with the actual username of the author. It is passed to the show_author() function as a parameter. Further, this value allows us to review the author data from the database and generate a response based on the information we get from the database. Another example is `@app.route('/posts/<int:post_id>/<slug>')` It incorporates a converter for the `post_id` in the form of `<int:post_id>` indicating that an integer is expected to the variable. We also have the `<slug>` which will capture a slug string for this variable.

- How do you collect data from the query string using Flask?
  
##### Flask makes it easy to access parsed query statements either through the query parameters itself or by accessing the `query_string` property of the request object.

- How do you collect data from the body of the request using Flask?

##### You can use the request object through `request.data`. To get the data received in a Flask request, you need to access the request object in the view function that handles the request. The request object contains a dictionary like object called form that contains the data sent in the request body.

- What is a cookie and what kinds of things are they commonly used for?

##### A cookie is information that a website puts on a user's computer. Cookies store limited information from a web browser session on a website that is later retrieved. 

- What is the session object in Flask?

##### A session object is used to track the session data which is a dictionary object that contains a key-value pair of the session variables and their associated values.

- What does Flask's `jsonify()` do?

##### The jsonify() function returns a Response object. Flask serializes your data as JSON and adds it to this response object. 