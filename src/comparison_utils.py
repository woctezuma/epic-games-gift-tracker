SORTING_FIELD = "urlSlug"
IDENTITY_FIELD = "title"


def sort_gifts(gifts):
    return sorted(gifts, key=lambda x: x[SORTING_FIELD])


def is_the_same_gift(first_gift, second_gift):
    return first_gift[IDENTITY_FIELD] == second_gift[IDENTITY_FIELD]


def is_among_gifts(gift, gifts):
    return any(is_the_same_gift(gift, e) for e in gifts)
