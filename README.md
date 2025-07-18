
# 🛡️ Demonstração: Mass Assignment Vulnerability em Flask

Este projeto demonstra como uma aplicação web pode ser vulnerável a um ataque de **Atribuição em Massa (Mass Assignment)** e como mitigar esse risco com boas práticas de programação.

## 📚 Sobre o Projeto

Um cenário simples foi criado usando o microframework **Flask** em Python. A aplicação possui duas versões:

- `ataque.py`: versão com **falha de segurança**
- `correção.py`: versão **corrigida**, utilizando whitelisting

O objetivo é mostrar na prática como um usuário malicioso pode alterar atributos sensíveis (`is_admin`) manipulando os dados enviados ao servidor.

---

## 🧰 Pré-requisitos

- Python 3.8+
- pip

---

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/thainanunesf/Mass-Assignment-Attack.git
cd mass-assignment-flask-demo

```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```
5. Instale as dependências:
```bash
 pip install flask
````

## 🚀 Como Executar
Você pode testar tanto a versão vulnerável quanto a corrigida separadamente.

🔓 Versão Vulnerável
```bash
python ataque.py
```
Acesse: http://127.0.0.1:5000

---

Teste o ataque com postman:
1- Abra o Postman.
---
2-Crie uma nova requisição POST para:

http://127.0.0.1:5000/update

3- Vá até a aba Body > x-www-form-urlencoded

````bash
nome: Atacante
email: atacante@hack.com
is_admin: true

`````
📌 Resultado: o usuário se torna admin (is_admin: true)

---
🔐 Versão Corrigida:
```bash
python correção.py
```
Acesse: http://127.0.0.1:5000

---
Teste o ataque com postman da mesma forma como foi testado o ataque no arquivo vulnerável.

````bash
nome: Atacante
email: atacante@hack.com
is_admin: true
````
📌 Resultado: is_admin permanece False — tentativa de ataque fracassada

---
## Pablo Miranda - Thainá Cassiano - Thiago Amancio - Vinicius Rodrigues










