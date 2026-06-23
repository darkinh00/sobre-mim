# Importar
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Conteúdo da página
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades Dinâmicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_bd = request.form.get('button_db')
    
    return render_template('index.html', button_python=button_python)
    return render_template('index.html', button_discord=button_discord)
    return render_template('index.html', button_discord=button_html)
    return render_template('index.html', button_discord=button_db)
if __name__ == "__main__":
    app.run(debug=True)
