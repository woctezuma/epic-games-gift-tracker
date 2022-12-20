from src.discord_utils import post_message_to_discord_using_keyword
from src.message_utils import to_message
from src.webhook_utils import WEBHOOK_KEYWORD_GIFT

SORTING_FIELD = "urlSlug"
IDENTITY_FIELD = "title"


def sort_gifts(gifts):
    return sorted(gifts, key=lambda x: x[SORTING_FIELD])


def is_a_new_gift(gift, previous_gifts):
    return all(gift[IDENTITY_FIELD] != e[IDENTITY_FIELD] for e in previous_gifts)


def post_new_gifts_to_discord(gifts, previous_gifts):
    for gift in gifts:
        if is_a_new_gift(gift, previous_gifts):
            message = to_message(gift, webhook_keyword=WEBHOOK_KEYWORD_GIFT)
            post_message_to_discord_using_keyword(message, webhook_keyword=WEBHOOK_KEYWORD_GIFT)
