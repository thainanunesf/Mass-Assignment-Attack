from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Simulação de um banco de dados em memória
db = {
    'user123': {
        'nome': 'Thainá Cassiano',  # Nome do usuário
        'email': 'Thaina@exemplo.com',
        'is_admin': False  # O usuário NÃO é um administrador
    }
}

# Template HTML minimalista para a página
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Editar Perfil</title>
    <style>
        body { font-family: sans-serif; max-width: 600px; margin: 50px auto; }
        .user-data { background-color: #f0f0f0; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
        form > div { margin-bottom: 10px; }
        label { display: block; }
    </style>
</head>
<body>
    <h1>Perfil do Usuário</h1>
    <div class="user-data">
        <pre>{{ user_data | tojson(indent=4) }}</pre>
    </div>

    <h2>Editar Informações</h2>
    <form action="/update" method="POST">
        <div>
            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome" value="{{ user_data.nome }}">
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" value="{{ user_data.email }}">
        </div>
        <button type="submit">Atualizar</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    user_data = db['user123']
    return render_template_string(HTML_TEMPLATE, user_data=user_data)

@app.route('/update', methods=['POST'])
def update_user():
    user_data = db['user123']
    
    # --- A VULNERABILIDADE ESTÁ AQUI ---
    # O código aceita cegamente TODOS os dados do formulário e atualiza o objeto do usuário.
    # A função `to_dict()` converte os dados do formulário em um dicionário.
    form_data = request.form.to_dict()
    user_data.update(form_data) 
    # ------------------------------------

    print(f"Dados atualizados do usuário: {user_data}")
    return f"<h1>Dados Atualizados com Sucesso!</h1><pre>{jsonify(user_data).get_data(as_text=True)}</pre><a href='/'>Voltar</a>"

if __name__ == '__main__':
    app.run(debug=True)
