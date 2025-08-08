from flask import Flask, request, render_template_string
from core.faq_engine import get_answer

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<title>FAQ Jogos</title>
<h1>FAQ — Jogos</h1>
<form method=post>
  <input name=pergunta placeholder="Digite sua pergunta" style="width:60%">
  <button type=submit>Responder</button>
</form>
{% if resposta %}
  <h2>Resposta</h2>
  <p>{{ resposta }}</p>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    resposta = None
    if request.method == 'POST':
        pergunta = request.form.get('pergunta', '')
        resposta = get_answer(pergunta)
    return render_template_string(TEMPLATE, resposta=resposta)

def start_flask(host='127.0.0.1', port=5000, debug=True):
    app.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
    start_flask()