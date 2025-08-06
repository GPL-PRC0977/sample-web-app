from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    getTime = datetime.datetime.now()
    current_time = getTime.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('home.html', time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
