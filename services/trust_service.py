import math
import re
from datetime import datetime


SOURCE_REPUTATION = {
    "HuggingFace": 1.0,
    "Zenodo": 0.95,
    "PapersWithCode": 0.95,
    "Github": 0.80,
    "GitHub": 0.80,
    "Kaggle": 0.75,
    "Arxiv": 0.70,
}


GOOD_WORDS = [
    "benchmark",
    "dataset",
    "citation",
    "license",
    "readme",
    "quick start",
    "documentation",
]


def metadata_score(item):

    fields = [
        item.get("title"),
        item.get("description"),
        item.get("url"),
        item.get("updated"),
        item.get("source"),
    ]

    filled = sum(1 for x in fields if x)

    return filled / len(fields)


def description_score(item):

    desc = item.get("description", "").lower()

    score = 0

    if len(desc) > 100:
        score += 0.3

    if len(desc) > 300:
        score += 0.2

    for word in GOOD_WORDS:

        if word in desc:
            score += 0.1

    return min(score, 1.0)


def source_score(item):

    source = item.get("source", "")

    return SOURCE_REPUTATION.get(source, 0.5)


def freshness_score(item):

    updated = item.get("updated", "")

    m = re.search(r"(20\d\d)", updated)

    if not m:
        return 0.5

    year = int(m.group(1))

    current = datetime.now().year

    age = current - year

    return math.exp(-0.25 * age)


def trust_score(item):

    m = metadata_score(item)

    d = description_score(item)

    s = source_score(item)

    f = freshness_score(item)

    trust = (
        0.30 * m +
        0.25 * d +
        0.25 * s +
        0.20 * f
    )

    return round(trust * 100, 2)