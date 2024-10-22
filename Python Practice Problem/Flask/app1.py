## Building URL Dynamically
## Variable Rules and URL Building

from flask import Flask

app = Flask (__name__)

@app.route('/')
def welcome():
    return "welcome to my youtube channel"

@app.route('/success/<int:score>')
def success(score):
    return "person is passed and marks is " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "person is failed and the marks is" + str(score)
## result checker
@app.route('/results/<int:score>')
def results(score):
    results = ""
    if score < 50:
        reuslts = "Fail"
    else:
        results = "success"
    return results

if __name__ == '__main__':
    app.run(debug=True)