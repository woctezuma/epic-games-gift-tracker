from src.json_utils import load_json_failsafe, save_json

DATA_FOLDER = "data"
GIFT_DATA_FNAME = f"{DATA_FOLDER}/gift_data.json"
DISCORD_WEBHOOK_FNAME = f"{DATA_FOLDER}/discord_webhook.json"


def load_gifts():
    return load_json_failsafe(GIFT_DATA_FNAME)


def save_gifts(data, prettify=True):
    return save_json(data, GIFT_DATA_FNAME, prettify=prettify)


def load_discord_webhook():
    return load_json_failsafe(DISCORD_WEBHOOK_FNAME)
