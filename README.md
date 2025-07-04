
# 🛡️ Demonstração: Mass Assignment Vulnerability em Flask

Este projeto demonstra como uma aplicação web pode ser vulnerável a um ataque de **Atribuição em Massa (Mass Assignment)** e como mitigar esse risco com boas práticas de programação.

## 📚 Sobre o Projeto

Um cenário simples foi criado usando o microframework **Flask** em Python. A aplicação possui duas versões:

- `app_vulneravel.py`: versão com **falha de segurança**
- `app_corrigido.py`: versão **corrigida**, utilizando whitelisting

O objetivo é mostrar na prática como um usuário malicioso pode alterar atributos sensíveis (`is_admin`) manipulando os dados enviados ao servidor.

---

## 🧰 Pré-requisitos

- Python 3.8+
- pip

---

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/mass-assignment-flask-demo.git
cd mass-assignment-flask-demo
