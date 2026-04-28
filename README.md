# 🌑 Eclipse Automation Framework v2.0

O **Eclipse** evoluiu de um simples bot para um framework de automação modular e inteligente. Projetado para ser executado no **Termux** ou qualquer ambiente Python, ele combina ferramentas de sistema, IA e notificações em uma interface elegante.

## 🚀 Funcionalidades de Elite

### 🤖 Inteligência Artificial (Gemini)
Integração direta com o Google Gemini para análise de dados, resumos e assistência inteligente via linha de comando.

### 🔔 Notificações Multicanal
Módulo pronto para enviar alertas e relatórios de automação para **Discord** e **Telegram** via Webhooks e Bots.

### 📂 Gestão Inteligente de Arquivos
Organizador automático que mantém seu ambiente limpo, movendo arquivos por tipo e extensão.

### 📊 Ferramentas de Dados & Web
- Conversão instantânea de formatos (CSV para JSON).
- Cálculos estatísticos automatizados.
- Web Scraping para extração de dados de sites.

### 🎨 Interface TUI (Terminal User Interface)
Interface visual rica construída com a biblioteca `Rich`, oferecendo painéis, cores e uma experiência de usuário superior.

## 🛠️ Instalação e Configuração

1. **Instale as dependências profissionais**:
   ```bash
   pip install requests beautifulsoup4 rich google-generativeai
   ```

2. **Configure suas chaves**:
   - Renomeie o arquivo `.env.example` para `.env`.
   - Adicione sua `GEMINI_API_KEY` e URLs de Webhook.

3. **Inicie o Framework**:
   ```bash
   python main.py
   ```

## 📂 Estrutura do Projeto

- `main.py`: Interface TUI central.
- `ai_module.py`: Cérebro do projeto (Gemini).
- `notifier.py`: Sistema de alertas (Discord/Telegram).
- `organizer.py`: Gestão de arquivos.
- `tools.py`: Utilitários de dados.
- `web_bot.py`: Automação web.

---
*Transformando o terminal em uma central de comando inteligente.*
