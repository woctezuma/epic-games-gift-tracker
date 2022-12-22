from src.data_utils import load_gifts, save_gifts
from src.download_utils import download_gifts
from src.gift_utils import post_new_gifts_to_discord
from src.management_utils import smart_merge_of_gifts
from src.comparison_utils import sort_gifts


def main():
    previous_gifts = load_gifts()

    gifts = sort_gifts(download_gifts())

    post_new_gifts_to_discord(gifts, previous_gifts)

    smart_merge_of_gifts(gifts, previous_gifts)
    save_gifts(sort_gifts(gifts))


if __name__ == "__main__":
    main()
