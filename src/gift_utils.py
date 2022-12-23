from src.comparison_utils import is_among_gifts
from src.discord_utils import post_message_to_discord_using_keyword
from src.message_utils import to_message
from src.parse_gift import parse_gift_wrapping_image_url_if_still_wrapped
from src.utils import unique
from src.webhook_utils import WEBHOOK_KEYWORD_GIFT, WEBHOOK_KEYWORD_WRAPPING


def is_a_new_gift(gift, previous_gifts):
    return not is_among_gifts(gift, previous_gifts)


def post_new_gifts_to_discord(gifts, previous_gifts):
    image_urls = []
    for gift in gifts:
        if is_a_new_gift(gift, previous_gifts):
            message = to_message(gift, webhook_keyword=WEBHOOK_KEYWORD_GIFT)
            post_message_to_discord_using_keyword(message, webhook_keyword=WEBHOOK_KEYWORD_GIFT)

            image_url = parse_gift_wrapping_image_url_if_still_wrapped(gift)
            if image_url is not None:
                image_urls.append(image_url)

    for image_url in unique(image_urls):
        post_message_to_discord_using_keyword(image_url, webhook_keyword=WEBHOOK_KEYWORD_WRAPPING)
