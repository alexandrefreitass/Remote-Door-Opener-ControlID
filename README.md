## Aplicativo de Abertura Remota de Portas

<div align="center">
    <img src="https://github.com/alexandrefreitass/abrirporta/assets/109884524/7a6c86ee-2c04-4dee-8892-5fa0ad355151" />
</div>

### Visão Geral
Este projeto é uma aplicação web desenvolvida para interagir com a API do Controlador de Acesso Control ID, permitindo a abertura de uma porta de maneira remota. Esta solução foi criada como alternativa a um botão físico defeituoso, cujo conserto não era viável. O aplicativo foi construído usando Python e Flask.

**🆕 Melhorias Implementadas:**
- ✅ Configurações de segurança com variáveis de ambiente
- ✅ **REDESIGN COMPLETO:** Interface de painel de controle moderna
- ✅ Tema dark com efeitos glassmorphism e gradientes
- ✅ Integração da logo como elemento de design
- ✅ Animações fluidas e feedback visual avançado
- ✅ Sistema de loading e partículas interativas
- ✅ Design totalmente responsivo para mobile
- ✅ Página de sucesso com confetti e status detalhado
- ✅ **Sistema de Erro Profissional:** Página de erro personalizada com troubleshooting

### Funcionalidades
- 🚪 **Painel de Controle Moderno:** Interface centralizada tipo "command center"
- 🔐 Interação segura com o Controlador de Acesso Control ID via API
- ⚙️ Configuração flexível através de variáveis de ambiente
- 🎨 **Design System Avançado:** Tema dark, glassmorphism, gradientes
- 🎯 **UX Aprimorada:** Loading states, animações, feedback visual
- 📱 **Mobile-First:** Design responsivo para todos os dispositivos
- ✨ **Efeitos Visuais:** Partículas flutuantes, confetti de sucesso
- 🖼️ **Branding Integrado:** Logo como watermark e elemento principal
- 🚨 **Tratamento de Erros:** Página de erro profissional com troubleshooting detalhado

### Pré-requisitos
- Python 3
- Flask
- Biblioteca Requests
- python-dotenv (para gerenciamento de configurações)

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone [URL_do_repositório]
   cd [nome_do_repositório]
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente:**
   - Copie o arquivo `config.env` e ajuste as configurações conforme necessário:
   ```bash
   # Edite o arquivo config.env com as configurações do seu dispositivo
   DEVICE_IP=10.43.153.110          # IP do controlador ControlID
   DEVICE_LOGIN=admin               # Login do dispositivo
   DEVICE_PASSWORD=sua_senha_aqui   # Senha do dispositivo
   FLASK_PORT=5000                  # Porta da aplicação (use 5000 se não tiver privilégios para porta 80)
   ```

4. **Execute a aplicação:**
   ```bash
   python main.py
   ```

5. **Acesse a aplicação:**
   - Abra o navegador e vá para: `http://localhost:80` (ou a porta configurada)

### Configurações de Segurança

🔒 **Importante:** As credenciais do dispositivo agora são configuradas através do arquivo `config.env`, mantendo as informações sensíveis fora do código fonte.

- `DEVICE_IP`: Endereço IP do controlador ControlID
- `DEVICE_LOGIN`: Usuário para autenticação na API
- `DEVICE_PASSWORD`: Senha para autenticação na API
- `FLASK_PORT`: Porta onde a aplicação será executada (recomendado: 5000 para ambiente de desenvolvimento)

### Estrutura do Projeto

```
📁 Remote Door ControlID/
├── 📄 main.py              # Aplicação Flask principal
├── 📄 config.env           # Configurações de ambiente (não versionar em produção)
├── 📄 requirements.txt     # Dependências Python
├── 📄 .gitignore           # Arquivos a ignorar no controle de versão
├── 📁 templates/
│   ├── 📄 index.html       # Página principal (aprimorada)
│   ├── 📄 sucesso.html     # Página de confirmação (redesenhada)
│   └── 📄 erro.html        # Página de erro profissional
├── 📁 static/              # Arquivos estáticos (CSS, JS, imagens)
│   ├── 📁 css/
│   │   ├── 📄 style.css    # Estilos da página principal
│   │   ├── 📄 sucesso.css  # Estilos da página de sucesso
│   │   └── 📄 erro.css     # Estilos da página de erro
│   └── 📁 js/
│       └── 📄 pyscript.js  # Scripts JavaScript
├── 📁 docs/                # Documentação e imagens
└── 📄 README.md
```

### ✨ **Melhorias na Organização e Design:**

**📁 Estrutura de Código:**
- **Separação de responsabilidades**: CSS e JS em arquivos dedicados na pasta `static`
- **Estrutura padrão Flask**: Convenção do Flask para arquivos estáticos
- **Manutenibilidade**: Código mais limpo e organizado
- **Performance**: Arquivos CSS podem ser cacheados pelo navegador

**🎨 Sistema de Design:**
- **Design System**: Variáveis CSS centralizadas com tema consistente
- **Tipografia**: Fonte Inter do Google Fonts para legibilidade premium
- **Cores**: Paleta dark com acentos ciano e laranja vibrantes
- **Layout**: Grid/Flexbox moderno com glassmorphism
- **Animações**: Transições suaves e feedback visual em tempo real
- **Responsividade**: Breakpoints mobile-first (480px, 768px)

**🔧 Recursos Técnicos:**
- **CSS Variables**: Sistema de design escalável e customizável
- **Backdrop Filter**: Efeitos de blur para glassmorphism
- **CSS Animations**: Keyframes para entrada, loading e interações
- **JavaScript Vanilla**: Partículas, confetti e interações sem dependências
- **Semantic HTML**: Estrutura acessível e SEO-friendly
