
from flask import Flask, render_template

app = Flask(__name__)

@app.get('/aula')
def home():
    a = 18
    b = 20
    c = a + b
    return f"A soma é {c}"

if __name__ == '__main__':
    app.run(debug=True)