from flask import Flask, request, render_template
from earthquakes import get_data

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def searchTopic():
    output = get_data()
    return render_template('index.html', title=output[0], count=output[1], events=output[2])

if __name__ == '__main__':
    app.run()
