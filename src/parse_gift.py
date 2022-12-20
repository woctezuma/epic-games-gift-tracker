MAX_LENGTH = 200
MAIN_FIELDS = ["title", "urlSlug"]
IMAGE_FIELD = "keyImages"
ATTRIBUTE_FIELD = "customAttributes"


def parse_meta_data(gift, max_length=MAX_LENGTH):
    return {
        field: gift[field][:max_length]
        for field in MAIN_FIELDS
        if field in gift and gift[field] is not None and gift[field] != "[]"
    }


def parse_key_images(gift):
    image_data = gift[IMAGE_FIELD]
    return {e["type"]: e["url"] for e in image_data}


def parse_custom_attributes(gift):
    attribute_data = gift[ATTRIBUTE_FIELD]
    return {e["key"]: e["value"] for e in attribute_data if e["value"] != "[]"}
