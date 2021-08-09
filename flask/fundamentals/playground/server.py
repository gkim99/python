from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/play')
def index():
    return render_template('index.html')

@app.route('/play/<int:num>')
def index1(num):
    return render_template('index1.html', num=num)

@app.route('/play/<int:num>/<color>')
def index2(num, color):
    return render_template('index2.html', num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)