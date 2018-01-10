# Hasura Product Development Fellowship

# ------
# Week 1
# ------

Firstly, we need to have python installed on our local machine. Python 2.6 or higher is required for installation of Flask.

Installing a virtual Python environment builder like virtualenv allows user to create multiple Python environments side-by-side. This allows the user to manage dependencies easily. We can then install Flask using a Python package managemment sytstem like pip.

Alternatively we could use Conda which also builds a virtual environment like virtualenv besides allowing user to manage Python packages. 

Now to install any python packages or modules we could use conda install or pip install.

For developers using a text editor like Atom or PyCharm IDE is helpful.

'week1' folder contains flask_app.py and 'templates' folder.

flask_app.py is the python file that is run. 'templates' folder contains all the html files to be rendered using render_template module. IMPORTANT : By default, when render_template is used, the system looks for the file in the folder with name 'templates' only. So, it is important to name the folder 'templates' only and not anything else. However, the default name can be changed.

In flask_app.py, we first import the various classes needed like Flask, render_template etc. These classes are used in our Python code.
We then create an instance of the Flask class.

    app = Flask(__name__)

Task 1
------

The following portion of code in flask_app.py

    if __name__ == '__main__':
        app.debug = True
        app.run()
 
 is to run the local Flask server with debugging mode turned on.
 By default, the server runs on port 5000
 We use route() decorator to tell FLask that the path '/' to trigger the hello() function which returns the string - Hello World - Sai.
 
 Task 2
 ------
 
 We now link the path '/authors' to the function req_data()
 We obtain authors' list and posts' list from the two sources, 'https://jsonplaceholder.typicode.com/users' and 'https://jsonplaceholder.typicode.com/posts' respectively. 
 We now modify the objects as dictionaries and pass them to the function person_extract(). An empty list person is created. We now start appending dictionaries with keys 'name' and 'counts' to the list. 'counts' for each author is incremented by comparing the id of author to the userId of a post.
 We now return html code.
 
 Task 3
 ------
 
 The function setcookie() is called when we route to the path '/setcookie'
 We set the values of cookies with names 'name' and 'age' as 'Sai' and '19' respectively using the set_cookie() method.
 We return the response 'res'.
 
 Task 4
 ------
 
The function getcookie() is called when we route to the path '/getcookies'
We return the most recently set values of cookies with names 'name' and 'age'. This is done using the cookies.get() methid of the request module.

Task 5
------

When we make a request to '/robots.txt' path, deny function is called and a string displaying access denial is returned. Further, we can configure robots.txt in such a way so as to prevent access to the server contents to certain clients.

Task 6
------

The path '/html' triggers the function show_html() which renders the html file 'robots_txt.html' present in the templates folder.

Task 7
------

The path '/input' triggers the form1() function which renders 'input.html' file. It contains a form with textbox and submit button. On clicking submit, data is sent to the '/welcome' endpoint by POST http method. We log the string on to stdout and also return the same string.

---------------------------------------------------------------------------------------------------------------------------------

We run flask_app.py.
Now in the browser, we can verify the functionalities by visiting various paths in http://localhost:5000.
