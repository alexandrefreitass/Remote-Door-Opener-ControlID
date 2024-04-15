from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

@app.route("/biometria")
def index():
    return render_template("index.html")

@app.route("/mostrar", methods=["POST"])
def mostrar():
    mensagem = "sucesso"
    urla = "http://10.43.153.110/login.fcgi"
    ##urla = "192.168.200.101"

    payloadd = json.dumps({
    "login": "admin",
    "password": "telecom2022"
    })
    headerss = {
    'Content-Type': 'application/json'
    }

    response1 = requests.request("POST", urla, headers=headerss, data=payloadd)

    print(response1.text)
    teste1= json.loads(response1.text)


    url = "http://10.43.153.110/execute_actions.fcgi?session="+teste1["session"]
    ##url = "192.168.200.113?session="+teste1["session"]

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

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    ##print(response1)
    ##teste1= json.loads(response1.text)
    ##print(teste1["session"])
    return render_template("sucesso.html")

if __name__ == '__main__':
    app.run(port=80, host='10.43.153.252', debug=True, threaded=True)
    ##app.run(port=80, host='192.168.200.101', debug=True, threaded=True)
    

