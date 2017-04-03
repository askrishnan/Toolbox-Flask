from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    age = request.form['age']
    ninja = request.form['ninja']
    if (name != ''and age != '' and ninja != ''):
        return render_template('profile.html', name=name, age=age, ninja=ninja)
    else:
        return render_template('error.html')


if __name__ == '__main__':
    app.run()
