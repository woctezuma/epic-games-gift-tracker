from src.comparison_utils import is_among_gifts
from src.discord_utils import post_message_to_discord_using_keyword
from src.message_utils import to_message
from src.parse_gift import get_image_urls_of_intact_wrappings, get_image_urls_of_all_wrappings
from src.utils import unique
from src.webhook_utils import WEBHOOK_KEYWORD_GIFT, WEBHOOK_KEYWORD_WRAPPING


def is_a_new_gift(gift, previous_gifts):
    return not is_among_gifts(gift, previous_gifts)


def post_new_gifts_to_discord(gifts, previous_gifts):
    for gift in gifts:
        if is_a_new_gift(gift, previous_gifts):
            message = to_message(gift, webhook_keyword=WEBHOOK_KEYWORD_GIFT)
            post_message_to_discord_using_keyword(message, webhook_keyword=WEBHOOK_KEYWORD_GIFT)


def post_new_gift_wrapping_images_to_discord(gifts, previous_gifts):
    current_image_urls = get_image_urls_of_intact_wrappings(gifts)
    previous_image_urls = get_image_urls_of_all_wrappings(previous_gifts)

    image_urls = set(current_image_urls).difference(previous_image_urls)

    for image_url in unique(image_urls):
        if image_url is not None:
            post_message_to_discord_using_keyword(image_url, webhook_keyword=WEBHOOK_KEYWORD_WRAPPING)
