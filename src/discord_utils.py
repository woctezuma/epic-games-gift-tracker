import requests

from src.data_utils import load_discord_webhook

DISCORD_API_URL = "https://discord.com/api/webhooks/"


def get_webhook_id(webhook_keyword="id"):
    webhook = load_discord_webhook()
    return webhook.get(webhook_keyword)


def get_webhook_url(webhook_id):
    return f"{DISCORD_API_URL}{webhook_id}"


def post_message_to_discord(message, webhook_id):
    if webhook_id is None or len(message) == 0:
        response = None
    else:
        json_data = {"content": message}
        response = requests.post(url=get_webhook_url(webhook_id), json=json_data)

    return response


def post_message_to_discord_using_keyword(message, webhook_keyword):
    return post_message_to_discord(message, get_webhook_id(webhook_keyword))
