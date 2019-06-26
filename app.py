from flask import Flask, request, render_template
from earthquakes import get_data

app = Flask(__name__)


@app.route('/')
def displayByDate():
    output = get_data("date")
    return render_template('index.html', title=output[0], count=output[1], events=output[2])

@app.route('/fetch')
def fetchData():
    output = get_data("date")
    return render_template('index.html', title=output[0], count=output[1], events=output[2])

@app.route('/mag')
def displayByMag():
    output = get_data("mag")
    return render_template('index.html', title=output[0], count=output[1], events=output[2])

if __name__ == '__main__':
    app.run()
