PROMOTION_MAJOR_FIELD = "promotions"
PROMOTION_SUB_FIELDS = ["promotionalOffers", "upcomingPromotionalOffers"]


def sort_promotions(promos):
    # Caveat: discountPercentage is confusing, this is the ratio between discounted and base prices.
    return sorted(promos, key=lambda x: (x["startDate"], x["discountSetting"]["discountPercentage"]))


def sort_promotions_inside_gifts(gifts):
    for gift in gifts:
        for field in PROMOTION_SUB_FIELDS:
            try:
                promos = gift[PROMOTION_MAJOR_FIELD][field][0]["promotionalOffers"]
            except (KeyError, IndexError, TypeError):
                continue
            gift[PROMOTION_MAJOR_FIELD][field][0]["promotionalOffers"] = sort_promotions(promos)
