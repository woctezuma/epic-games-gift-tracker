from src.formatting_utils import concatenate_values, concatenate_items
from src.parse_gift import parse_meta_data, parse_key_images, parse_custom_attributes
from src.webhook_utils import to_discord_header


def to_message(gift, webhook_keyword=None):
    header = to_discord_header(webhook_keyword)

    meta_data = parse_meta_data(gift)
    key_images = parse_key_images(gift)
    custom_attributes = parse_custom_attributes(gift)

    message = header + concatenate_items(meta_data | custom_attributes) + concatenate_values(key_images)

    return message
