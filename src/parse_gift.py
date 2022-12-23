MAX_LENGTH = 200
MAIN_FIELDS = ["title", "urlSlug"]
IMAGE_FIELD = "keyImages"
ATTRIBUTE_FIELD = "customAttributes"
PRODUCT_SLUG_FIELD = "productSlug"
GIFT_WRAPPING_IMAGE_FIELD = "VaultClosed"


def is_dummy_entry(str_value):
    return str_value is None or len(str_value) == 0 or str_value == "[]"


def parse_meta_data(gift, max_length=MAX_LENGTH):
    return {field: gift[field][:max_length] for field in MAIN_FIELDS if not is_dummy_entry(gift.get(field))}


def parse_key_images(gift):
    image_data = gift[IMAGE_FIELD]
    return {e["type"]: e["url"] for e in image_data}


def parse_custom_attributes(gift):
    attribute_data = gift[ATTRIBUTE_FIELD]
    return {e["key"]: e["value"] for e in attribute_data if not is_dummy_entry(e["value"])}


def parse_gift_wrapping_image_url(gift):
    key_images = parse_key_images(gift)
    return key_images.get(GIFT_WRAPPING_IMAGE_FIELD)


def parse_gift_wrapping_image_url_if_still_wrapped(gift):
    product_slug = gift.get(PRODUCT_SLUG_FIELD)

    if is_dummy_entry(product_slug):
        image_url = None
    else:
        image_url = parse_gift_wrapping_image_url(gift)

    return image_url
