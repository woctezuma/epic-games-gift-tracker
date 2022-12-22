from datetime import datetime, timezone

from src.comparison_utils import is_the_same_gift

FIRST_SEEN_FIELD = "firstSeenDate"
THRESHOLD_IN_SECONDS = 3600


def get_time_now():
    return datetime.now(timezone.utc)


def add_timestamp_to_gifts(gifts):
    time_now = get_time_now().isoformat()
    for gift in gifts:
        if FIRST_SEEN_FIELD not in gift:
            gift[FIRST_SEEN_FIELD] = time_now


def get_duration_since_first_seen(gift):
    first_seen_as_str = gift.get(FIRST_SEEN_FIELD)

    if first_seen_as_str is not None:
        first_seen = datetime.fromisoformat(first_seen_as_str)
        duration_since_first_seen = (get_time_now() - first_seen).total_seconds()
    else:
        duration_since_first_seen = 0.0

    return duration_since_first_seen


def is_a_reliable_gift(gift):
    return get_duration_since_first_seen(gift) > THRESHOLD_IN_SECONDS


def copy_timestamps(source_gift, destination_gifts, field=FIRST_SEEN_FIELD):
    for target_gift in destination_gifts:
        if is_the_same_gift(source_gift, target_gift):
            target_gift[field] = source_gift[field]
