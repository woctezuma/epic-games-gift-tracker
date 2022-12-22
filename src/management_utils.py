from src.time_utils import is_a_reliable_gift

SORTING_FIELD = "urlSlug"
IDENTITY_FIELD = "title"


def sort_gifts(gifts):
    return sorted(gifts, key=lambda x: x[SORTING_FIELD])


def is_the_same_gift(first_gift, second_gift):
    return first_gift[IDENTITY_FIELD] == second_gift[IDENTITY_FIELD]


def is_among_gifts(gift, gifts):
    return any(is_the_same_gift(gift, e) for e in gifts)


def smart_merge_of_gifts(gifts, previous_gifts):
    for gift in previous_gifts:
        if not is_among_gifts(gift, gifts) and not is_a_reliable_gift(gift):
            # We are unsure whether the deletion of the previous gift is due to
            # a bug on Epic Games' side, so we prefer to keep the gift for now.
            gifts.append(gift)

    return sort_gifts(gifts)
