from src.comparison_utils import is_among_gifts
from src.time_utils import is_a_reliable_gift, copy_timestamps


def smart_merge_of_gifts(gifts, previous_gifts):
    for gift in previous_gifts:
        if is_among_gifts(gift, gifts):
            copy_timestamps(gift, gifts)
        elif not is_a_reliable_gift(gift):
            # We are unsure whether the deletion of the previous gift is due to
            # a bug on Epic Games' side, so we prefer to keep the gift for now.
            gifts.append(gift)
