from chatgpt import chat_gpt
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.get('/')
@app.get('/index')
@app.get('/home')
def home():
    return render_template('home.html', text="")


history = ""


@app.post('/home')
def home_2():
    global history
    inp = request.form.get('text')
    history = history + " " + inp
    text = chat_gpt(history)
    return render_template('home.html', text=text)


@app.get('/newchat')
def newChat():
    global history
    history = ""
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
