from flask import Flask, request, jsonify, render_template_string, redirect, url_for

app = Flask(__name__)

# Simulação de um banco de dados em memória (resetado para o estado inicial)
db = {
    'user123': {
        'nome': 'Thainá Cassiano',
        'email': 'Thaina@exemplo.com',
        'is_admin': False
    }
}


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang=\"pt-br\">
<head>
    <meta charset=\"UTF-8\">
    <title>Editar Perfil</title>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <link href=\"https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        body {
            font-family: 'Roboto', Arial, sans-serif;
            background: linear-gradient(120deg, #f8fafc 0%, #e0e7ef 100%);
            min-height: 100vh;
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
        }
        .container {
            background: #fff;
            margin-top: 40px;
            padding: 32px 28px 24px 28px;
            border-radius: 16px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.08);
            max-width: 420px;
            width: 100%;
            position: relative;
        }
        .header {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-bottom: 8px;
        }
        .header i {
            color: #2563eb;
            font-size: 2.1rem;
        }
        h1 {
            color: #2d3748;
            font-size: 2rem;
            margin: 0;
            text-align: center;
            font-weight: 700;
        }
        .alert {
            background: #d1fae5;
            color: #065f46;
            border: 1px solid #34d399;
            border-radius: 6px;
            padding: 12px 16px;
            margin-bottom: 18px;
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 1rem;
            animation: fadeIn 0.7s;
        }
        .alert i {
            font-size: 1.2rem;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .user-data {
            background-color: #f1f5f9;
            padding: 16px;
            border-radius: 8px;
            margin-bottom: 24px;
            font-size: 1rem;
            color: #374151;
            box-shadow: 0 1px 2px rgba(0,0,0,0.03);
            border-left: 4px solid #2563eb;
        }
        h2 {
            color: #2563eb;
            font-size: 1.2rem;
            margin-bottom: 10px;
            text-align: center;
        }
        form {
            background: #f8fafc;
            border-radius: 8px;
            padding: 18px 12px 10px 12px;
            box-shadow: 0 1px 4px rgba(37,99,235,0.04);
        }
        form > div {
            margin-bottom: 16px;
        }
        label {
            display: block;
            margin-bottom: 4px;
            color: #475569;
            font-weight: 500;
        }
        input[type=\"text\"], input[type=\"email\"] {
            width: 100%;
            padding: 10px 12px;
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            font-size: 1rem;
            background: #f8fafc;
            transition: border 0.2s, box-shadow 0.2s;
        }
        input[type=\"text\"]:focus, input[type=\"email\"]:focus {
            border: 1.5px solid #2563eb;
            outline: none;
            background: #fff;
            box-shadow: 0 0 0 2px #93c5fd44;
        }
        button[type=submit] {
            background: linear-gradient(90deg, #2563eb 0%, #60a5fa 100%);
            color: #fff;
            border: none;
            border-radius: 6px;
            padding: 12px 0;
            width: 100%;
            font-size: 1.1rem;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(37,99,235,0.08);
            transition: background 0.2s, transform 0.1s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        button[type=submit]:hover {
            background: linear-gradient(90deg, #1d4ed8 0%, #3b82f6 100%);
            transform: translateY(-2px) scale(1.03);
        }
        .footer {
            margin-top: 32px;
            text-align: center;
            color: #a0aec0;
            font-size: 0.95rem;
        }
        @media (max-width: 500px) {
            .container {
                padding: 16px 6px 12px 6px;
            }
            form {
                padding: 10px 2px 6px 2px;
            }
        }
    </style>
</head>
<body>
    <div class=\"container\">
        <div class=\"header\">
            <i class=\"fa-solid fa-user-shield\"></i>
            <h1>Perfil do Usuário</h1>
        </div>
        {% if sucesso %}
        <div class=\"alert\"><i class=\"fa-solid fa-circle-check\"></i> Dados atualizados com sucesso!</div>
        {% endif %}
        <div class=\"user-data\">
            <strong>Dados atuais:</strong>
            <pre style=\"margin: 8px 0 0 0; background: none; border: none; padding: 0;\">{{ user_data | tojson(indent=4) }}</pre>
        </div>
        <h2>Editar Informações</h2>
        <form action=\"/update\" method=\"POST\">
            <div>
                <label for=\"nome\">Nome:</label>
                <input type=\"text\" id=\"nome\" name=\"nome\" value=\"{{ user_data.nome }}\" required>
            </div>
            <div>
                <label for=\"email\">Email:</label>
                <input type=\"email\" id=\"email\" name=\"email\" value=\"{{ user_data.email }}\" required>
            </div>
            <button type=\"submit\"><i class=\"fa-solid fa-floppy-disk\"></i> Atualizar</button>
        </form>
    </div>
    <div class=\"footer\">&copy; 2025 Mass Assignment Demo</div>
</body>
</html>
"""

@app.route('/')
def home():
    user_data = db['user123']
    sucesso = request.args.get('sucesso') == '1'
    return render_template_string(HTML_TEMPLATE, user_data=user_data, sucesso=sucesso)


@app.route('/update', methods=['POST'])
def update_user_safe():
    user_data = db['user123']
    form_data = request.form

    # --- A CORREÇÃO ESTÁ AQUI (WHITELISTING) ---
    # 1. Definimos explicitamente quais campos são permitidos para atualização.
    allowed_fields = ['nome', 'email']
    
    # 2. Criamos um novo dicionário apenas com os dados permitidos.
    update_data = {}
    for key in allowed_fields:
        if key in form_data:
            update_data[key] = form_data[key]

    # 3. Atualizamos o objeto do usuário apenas com os dados seguros.
    user_data.update(update_data)
    # ---------------------------------------------

    print(f"Dados atualizados do usuário (versão segura): {user_data}")
    return redirect(url_for('home', sucesso=1))

if __name__ == '__main__':
    app.run(debug=True)