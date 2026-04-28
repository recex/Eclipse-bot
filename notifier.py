import requests
import json

def send_discord_webhook(webhook_url, message, title="Eclipse Notification"):
    """Envia uma notificação para um Webhook do Discord."""
    if not webhook_url or "discord.com" not in webhook_url:
        return "Erro: URL do Webhook do Discord inválida."

    payload = {
        "embeds": [{
            "title": title,
            "description": message,
            "color": 0x3498db # Azul Eclipse
        }]
    }
    
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        return "Notificação enviada ao Discord com sucesso!"
    except Exception as e:
        return f"Erro ao enviar notificação: {str(e)}"

def send_telegram_msg(bot_token, chat_id, message):
    """Envia uma mensagem via Bot do Telegram."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": f"🌑 *Eclipse Automation*\n\n{message}",
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return "Mensagem enviada ao Telegram com sucesso!"
    except Exception as e:
        return f"Erro ao enviar ao Telegram: {str(e)}"
