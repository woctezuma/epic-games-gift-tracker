from src.utils import unique

LINE_SEP = "\n"
BULLET_POINT_SEP = "- "
ITEM_SEP = f"{LINE_SEP}{BULLET_POINT_SEP}"


def concatenate_lines(lines):
    return ITEM_SEP + ITEM_SEP.join(lines) + LINE_SEP


def concatenate_values(dico):
    unique_values = unique(dico.values())
    return concatenate_lines([f"{v}" for v in unique_values])


def concatenate_items(dico):
    return concatenate_lines([f"`{k}:` {v}" for k, v in dico.items()])
