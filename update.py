from src.data_utils import load_gifts, save_gifts
from src.download_utils import download_gifts
from src.gift_utils import post_new_gifts_to_discord, sort_gifts


def main():
    previous_gifts = load_gifts()

    gifts = sort_gifts(download_gifts())
    save_gifts(gifts)

    post_new_gifts_to_discord(gifts, previous_gifts)


if __name__ == "__main__":
    main()
