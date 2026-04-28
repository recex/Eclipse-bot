import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import print as rprint

# Importando módulos locais
from organizer import organize_files
from tools import csv_to_json, calculate_stats
from web_bot import get_website_title
from ai_module import ask_gemini
from notifier import send_discord_webhook

console = Console()

def show_menu():
    table = Table(title="🌑 [bold blue]Eclipse Automation Framework[/bold blue] v2.0", show_header=False, box=None)
    table.add_row("[cyan]1.[/cyan] 📂 Organizar Arquivos")
    table.add_row("[cyan]2.[/cyan] 📊 Conversor & Estatísticas")
    table.add_row("[cyan]3.[/cyan] 🌐 Web Scraping (Título)")
    table.add_row("[cyan]4.[/cyan] 🤖 Consultar IA (Gemini)")
    table.add_row("[cyan]5.[/cyan] 🔔 Enviar Notificação (Discord)")
    table.add_row("[cyan]0.[/cyan] [red]Sair[/red]")
    
    console.print(Panel(table, border_style="blue", title="Menu Principal", subtitle="Selecione uma opção"))

def main():
    # Tenta carregar variáveis de ambiente (simulação simplificada)
    # Em uso real, usaria python-dotenv
    gemini_key = os.getenv("GEMINI_API_KEY", "SUA_CHAVE_AQUI")
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL", "SUA_URL_AQUI")

    while True:
        console.clear()
        show_menu()
        
        choice = Prompt.ask("Escolha", choices=["1", "2", "3", "4", "5", "0"])
        
        if choice == '1':
            path = Prompt.ask("Digite o caminho da pasta")
            with console.status("[bold green]Organizando..."):
                result = organize_files(path)
            rprint(f"[green]{result}[/green]")
        
        elif choice == '2':
            sub_choice = Prompt.ask("2.1 Converter CSV | 2.2 Estatísticas", choices=["2.1", "2.2"])
            if sub_choice == "2.1":
                csv_p = Prompt.ask("Caminho CSV")
                json_p = Prompt.ask("Caminho JSON")
                rprint(csv_to_json(csv_p, json_p))
            else:
                data = Prompt.ask("Digite os números")
                rprint(calculate_stats(data.split()))
            
        elif choice == '3':
            url = Prompt.ask("Digite a URL")
            with console.status("[bold cyan]Acessando site..."):
                rprint(get_website_title(url))
            
        elif choice == '4':
            if gemini_key == "SUA_CHAVE_AQUI":
                rprint("[yellow]Aviso: Configure sua GEMINI_API_KEY no arquivo .env[/yellow]")
            prompt = Prompt.ask("O que deseja perguntar à IA?")
            with console.status("[bold magenta]IA pensando..."):
                response = ask_gemini(prompt, gemini_key)
            console.print(Panel(response, title="Resposta do Gemini", border_style="magenta"))
            
        elif choice == '5':
            msg = Prompt.ask("Mensagem para o Discord")
            with console.status("[bold blue]Enviando..."):
                rprint(send_discord_webhook(webhook_url, msg))
            
        elif choice == '0':
            rprint("[bold red]Eclipse encerrado. Até logo![/bold red]")
            break
        
        Prompt.ask("\nPressione Enter para voltar ao menu")

if __name__ == "__main__":
    main()
