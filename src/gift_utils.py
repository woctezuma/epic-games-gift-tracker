from src.discord_utils import post_message_to_discord_using_keyword
from src.management_utils import is_among_gifts
from src.message_utils import to_message
from src.webhook_utils import WEBHOOK_KEYWORD_GIFT


def is_a_new_gift(gift, previous_gifts):
    return not is_among_gifts(gift, previous_gifts)


def post_new_gifts_to_discord(gifts, previous_gifts):
    for gift in gifts:
        if is_a_new_gift(gift, previous_gifts):
            message = to_message(gift, webhook_keyword=WEBHOOK_KEYWORD_GIFT)
            post_message_to_discord_using_keyword(message, webhook_keyword=WEBHOOK_KEYWORD_GIFT)
