from chatgpt import chat_gpt
from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
@app.get('/index')
@app.get('/home')
def home():
    return render_template('home.html', text="")


@app.post('/home')
def home_2():
    inp = request.form.get('text')
    text = chat_gpt(inp)
    return render_template('home.html', text=text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
