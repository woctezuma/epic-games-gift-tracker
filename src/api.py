import requests

EPIC_GAMES_API_URL = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"


def send_get_request_to_api(verbose=True):
    response = requests.get(url=EPIC_GAMES_API_URL)
    return to_data(response, verbose=verbose)


def to_data(response, verbose=True):
    if response.ok:
        data = response.json()
    else:
        data = None
        if verbose:
            print(f"Status code = {response.status_code}")
    return data
