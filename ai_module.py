import google.generativeai as genai
import os

def setup_gemini(api_key):
    """Configura a API do Google Gemini."""
    try:
        genai.configure(api_key=api_key)
        return True
    except Exception:
        return False

def ask_gemini(prompt, api_key):
    """Envia um prompt para o Gemini e retorna a resposta."""
    if not api_key or api_key == "SUA_CHAVE_AQUI":
        return "Erro: API Key do Gemini não configurada no arquivo .env"
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao consultar Gemini: {str(e)}"

def summarize_text(text, api_key):
    """Resume um texto usando IA."""
    prompt = f"Por favor, resuma o seguinte texto de forma concisa e clara:\n\n{text}"
    return ask_gemini(prompt, api_key)
