SORTING_FIELD = "urlSlug"
IDENTITY_FIELD = "title"


def sort_gifts(gifts):
    return sorted(gifts, key=lambda x: x[SORTING_FIELD])


def is_among_gifts(gift, gifts):
    return any(gift[IDENTITY_FIELD] == e[IDENTITY_FIELD] for e in gifts)
