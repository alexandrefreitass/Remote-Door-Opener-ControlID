# Remote Door Opener (Control ID)

<div align="center">
  <img src="https://github.com/user-attachments/assets/d8a2c283-c018-47d1-8531-353becf035d2" alt="Tela inicial do painel de controle" width="700">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11">
  <img src="https://img.shields.io/badge/Flask-2.x-black?style=for-the-badge&logo=flask" alt="Flask 2.x">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="MIT License">
</div>

## 📋 Visão Geral
Aplicação web em **Python + Flask** que substitui o botão físico de um controlador **Control ID** e permite abrir a porta via navegador ou dispositivo móvel.  
Foi criada após a quebra do botão original, oferecendo uma solução elegante, segura e responsiva. :contentReference[oaicite:0]{index=0}

---

## ✨ Principais Funcionalidades
- **Painel “command-center”** com tema _dark_, glassmorphism e gradientes  
- **Abertura instantânea** da porta via API do Control ID  
- **Configuração por variáveis de ambiente** (IP, login, porta etc.)  
- **UX aprimorada**: animações, loading, partículas e confetti de sucesso  
- **Tratamento de erros profissional** com página de troubleshooting dedicada  
- **Design mobile-first** e totalmente responsivo :contentReference[oaicite:1]{index=1}  

---

## ⚙️ Tecnologias Utilizadas
- **Python 3.11** + **Flask 2.x**  
- **Requests** para chamadas HTTP  
- **python-dotenv** para gestão de credenciais  
- **HTML / CSS / JS Vanilla** (design system, partículas, confetti)  
- **Control ID REST API** para comandos de abertura  

---

## 🚀 Primeiros Passos

### 1 · Clonar o repositório
```
git clone https://github.com/alexandrefreitass/Remote-Door-Opener-ControlID.git
cd Remote-Door-Opener-ControlID
```
### 2 · Instalar dependências
```
pip install -r requirements.txt
```
### 3 · Configurar variáveis de ambiente
Copie **`config.env.example`** para **`config.env`** e ajuste:
```
DEVICE_IP=10.43.153.110
DEVICE_LOGIN=admin
DEVICE_PASSWORD=SuaSenhaAqui
FLASK_PORT=5000
```
### 4 · Executar a aplicação
```
python main.py
```
Acesse `http://localhost:5000` ou a porta que você definiu.

---

## 🗂️ Estrutura do Projeto
```
Remote-Door-Opener-ControlID/
├── main.py
├── config.env # NÃO versionar em produção
├── requirements.txt
├── templates/ # HTML (index, sucesso, erro)
├── static/
│ ├── css/ # style.css, sucesso.css, erro.css
│ └── js/ # partículas, confetti
├── docs/ # imagens e documentação
└── README.md
```
---

## 🔒 Boas Práticas de Segurança
- Credenciais mantidas fora do código-fonte (`config.env`)  
- `.gitignore` impede o commit de dados sensíveis  
- Recomendado rodar atrás de **Nginx** ou **Apache** com HTTPS em produção.

---

## 🤝 Contribuições
1. *Fork* do projeto  
2. Crie uma *branch*: `git checkout -b feature/NovaFuncionalidade`  
3. *Commit* das alterações  
4. *Push* para o seu fork  
5. Abra um **Pull Request**

---

## 📄 Licença
Distribuído sob a licença **MIT**. Veja o arquivo **LICENSE** para detalhes.