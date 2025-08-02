from flask import Flask, render_template
import requests
import json
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo config.env
load_dotenv('config.env')

app = Flask(__name__)

# Configurações obtidas das variáveis de ambiente para maior segurança
DEVICE_IP = os.getenv('DEVICE_IP', '10.43.153.110')
DEVICE_LOGIN = os.getenv('DEVICE_LOGIN', 'admin')
DEVICE_PASSWORD = os.getenv('DEVICE_PASSWORD', 'telecom2022')
FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
FLASK_PORT = int(os.getenv('FLASK_PORT', '80'))
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True') == 'True'

@app.route("/")
@app.route("/biometria")
def index():
    return render_template("index.html")

@app.route("/mostrar", methods=["POST"])
def mostrar():
    mensagem = "sucesso"
    urla = f"http://{DEVICE_IP}/login.fcgi"

    payloadd = json.dumps({
        "login": DEVICE_LOGIN,
        "password": DEVICE_PASSWORD
    })
    headerss = {
        'Content-Type': 'application/json'
    }

    # Bloco try-except é uma boa prática para lidar com falhas de rede
    try:
        response1 = requests.request("POST", urla, headers=headerss, data=payloadd, timeout=5) # Adicionado timeout
        response1.raise_for_status() # Lança um erro se a requisição falhar (status 4xx ou 5xx)

        teste1 = response1.json()

        session_id = teste1.get("session")
        if not session_id:
            print("Erro: 'session' não encontrado na resposta do login.")
            return "Erro de autenticação", 500

        url = f"http://{DEVICE_IP}/execute_actions.fcgi?session={session_id}"

        payload = json.dumps({
            "actions": [
                {
                    "action": "sec_box",
                    "parameters": "id=65793,reason=3"
                }
            ]
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload, timeout=5) # Adicionado timeout
        response.raise_for_status()

        print(response.text)
        return render_template("sucesso.html")

    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro na requisição: {e}")
        return render_template("erro.html", ip_do_dispositivo=DEVICE_IP)
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Ocorreu um erro ao processar a resposta JSON: {e}")
        return render_template("erro.html", ip_do_dispositivo=DEVICE_IP)


# Handler global de erros para páginas de erro profissionais
@app.errorhandler(404)
def page_not_found(e):
    return render_template("erro.html", ip_do_dispositivo=DEVICE_IP), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template("erro.html", ip_do_dispositivo=DEVICE_IP), 500

@app.errorhandler(Exception)
def handle_exception(e):
    # Log do erro para debugging
    print(f"Erro não tratado: {e}")
    return render_template("erro.html", ip_do_dispositivo=DEVICE_IP), 500


if __name__ == '__main__':
    # Configurações carregadas das variáveis de ambiente
    # Se der erro de "Permission Denied" na porta 80, altere FLASK_PORT no config.env para 5000 ou 8080
    app.run(port=FLASK_PORT, host=FLASK_HOST, debug=FLASK_DEBUG, threaded=True)