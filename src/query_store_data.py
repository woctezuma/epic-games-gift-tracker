from src.api import send_get_request_to_api


def to_store_data(verbose=True):
    data = send_get_request_to_api(verbose=verbose)
    try:
        store_data = data["data"]["Catalog"]["searchStore"]
    except (TypeError, KeyError):
        store_data = None
    return store_data
