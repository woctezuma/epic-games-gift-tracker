WEBHOOK_KEYWORD_NEW = "new"
WEBHOOK_KEYWORD_FREE = "free"
WEBHOOK_KEYWORD_TROPHY = "trophy"
WEBHOOK_KEYWORD_GIFT = "gift"
DISCORD_NEW_HEADER = "🆕👀"
DISCORD_FREE_HEADER = "🆓👀"
DISCORD_TROPHY_HEADER = "🏆👀"
DISCORD_GIFT_HEADER = "🎁👀"


def to_discord_header(webhook_keyword):
    if webhook_keyword == WEBHOOK_KEYWORD_FREE:
        discord_header = DISCORD_FREE_HEADER
    elif webhook_keyword == WEBHOOK_KEYWORD_NEW:
        discord_header = DISCORD_NEW_HEADER
    elif webhook_keyword == WEBHOOK_KEYWORD_TROPHY:
        discord_header = DISCORD_TROPHY_HEADER
    elif webhook_keyword == WEBHOOK_KEYWORD_GIFT:
        discord_header = DISCORD_GIFT_HEADER
    else:
        discord_header = ""

    return discord_header
