from datetime import datetime, timezone

FIRST_SEEN_FIELD = "firstSeenDate"
THRESHOLD_IN_SECONDS = 3600


def get_time_now():
    return datetime.now(timezone.utc)


def add_timestamp_to_gifts(gifts):
    for gift in gifts:
        if FIRST_SEEN_FIELD not in gift:
            gift[FIRST_SEEN_FIELD] = get_time_now().isoformat()


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
