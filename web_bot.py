import requests
from bs4 import BeautifulSoup

def get_website_title(url):
    """Obtém o título de qualquer site informado."""
    try:
        if not url.startswith('http'):
            url = 'https://' + url
            
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "Título não encontrado"
        return f"Título do site: {title.strip()}"
    except Exception as e:
        return f"Erro ao acessar o site: {str(e)}"

def search_news(topic):
    """Exemplo simples de scraping de notícias (usando um placeholder)."""
    # Aqui poderíamos implementar uma busca real em sites de notícias
    return f"Buscando notícias sobre: {topic}... (Funcionalidade pronta para expansão)"

if __name__ == "__main__":
    print(get_website_title("https://www.google.com"))
