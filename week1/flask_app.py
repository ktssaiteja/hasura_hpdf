from flask import Flask, make_response, request, render_template#, jsonify "for returnig lists, dictionaries"
import requests
import json

app = Flask(__name__)


def person_extract(author, post):
    person = []
    for pers in author:
        temp = {'name': '', 'counts': 0}
        for p in post:
            if pers['id'] == p['userId']:
                temp['counts'] += 1
        temp['name'] = pers['name']
        person.append(temp)
    html_out = '''
    <html>
        <head>
        <title>Authors</title>
        </head>
        <body>'''
    for i in person:
        html_out += ('''<p>''' + (i['name'] + " --> " + str(i["counts"]) + " posts") + '''</p>''')
    html_out += '''
        </body>
    </html>'''
    return html_out


@app.route("/")
def hello():
    return "Hello World - Sai"


@app.route("/authors")
def req_data():
    src1 = 'https://jsonplaceholder.typicode.com/users'
    src2 = 'https://jsonplaceholder.typicode.com/posts'
    authors_list = requests.get(src1)
    posts_list = requests.get(src2)
    post = json.loads(posts_list.text)
    author = json.loads(authors_list.text)
    return person_extract(author, post)


@app.route("/setcookie")
def setcookie():
    res = make_response("Want a cookie?")
    res.set_cookie('name', value='Sai')
    res.set_cookie('age', value='19')

    return res


@app.route("/getcookies")
def getcookie():
    data1 = request.cookies.get("name")
    data2 = request.cookies.get("age")
    return data1 + '''</br>''' + data2


@app.route("/robots.txt")
def deny():
    return '''
    <html>
        <body>
            <pre style="word-wrap: break-word; white-space: pre-wrap;">
    
      .-""""""-.
    .' _      _ '.
   (   O      O   )
  (                )
  |                |
  :       __       :
   \  .-"`  `"-.  /
    '.          .'
      '-......-'
 YOU SHOULDN'T BE HERE
            </pre>
        </body>
    </html>
    '''


@app.route("/html")
def show_html():
    return render_template('robots_txt.html')


@app.route("/input")
def form1():
    return render_template('input.html')


@app.route("/welcome", methods=['POST'])
def welcome():
    user = request.form['nm']
    return "Welcome " + user + "!"


if __name__ == '__main__':
    app.debug = True
    app.run()
