from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Clinstok - Sistema de Estoque</h1><p>Página inicial em construção.</p>"

if __name__ == '__main__':
    app.run(debug=True)
