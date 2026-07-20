from services.trust_service import trust_score
from services.quality_service import quality_score


def final_score(item):
    """
    Final ranking score:
    60% Trust + 40% Quality
    """

    trust = trust_score(item)
    quality = quality_score(item)

    return round(0.6 * trust + 0.4 * quality, 2)


def rank_datasets(items):

    for item in items:
        item["trust_score"] = trust_score(item)
        item["quality_score"] = quality_score(item)
        item["ranking_score"] = final_score(item)

    items.sort(
        key=lambda x: x["ranking_score"],
        reverse=True
    )

    return items


def top_datasets(items, n=20):
    return rank_datasets(items)[:n]