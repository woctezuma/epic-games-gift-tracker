from src.parse_store_data import get_store_elements
from src.query_store_data import to_store_data


def download_gifts(verbose=True):
    store_data = to_store_data(verbose=verbose)
    return get_store_elements(store_data)
