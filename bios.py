from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "vai corinthians🏴‍☠️7️⃣"

@app.route("/perfil")
def perfil():
    # aqui pedimos para acessar o index.html que deve estar dentro da pasta 'templates'
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)  # debug=True para recarregar automaticamente ao salvar
