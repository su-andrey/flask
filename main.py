from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return 'Nothing to show here, choose another url'

@app.route('/index/<name>')
def name(name):
    return render_template('index.html', title=name)

@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        return render_template('training.html', name='tex.png')
    else:
        return render_template('training.html', name='science.png')
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')