from flask import Flask

# __name__ = app.py
app = Flask(__name__)

#allows you to run the webserver via : $ python3 app.py
if __name__ == '__main__':
    app.run(debug=True)


@app.rout('/home')
def home():
    return 'Home Page'

#insert variables like this
@app.route('/<name>')
def name(name):
    return '<h1>Home Page {}!</h1>'.format(name)

#you can have 2 routes to the same function like this:
@app.route('/about')
@app.route('/gotoabout')
def about():
    return '<h1>About Page!</h1>'


