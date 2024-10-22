from flask import Flask
### WSGI Application
app = Flask(__name__)

## Decorator
@app.route('/')
def welcome():
    return "Welcome to my youtube channel."

@app.route('/members')
def membrs():
    return "shivanshu gaurav is good"

if __name__=='__main__':
    app.run(debug=True)