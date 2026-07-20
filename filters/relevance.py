IMPORTANT_KEYWORDS = [

    # Deepfake
    "deepfake",
    "deep fake",
    "face swap",
    "face forgery",
    "face manipulation",
    "forgery",
    "forensic",

    # AI Images
    "ai generated",
    "generated image",
    "synthetic face",
    "real vs fake",
    "fake image",

    # Videos
    "fake video",
    "video",
    "video frames",

    # Detection
    "detection",
    "benchmark",
    "fakeavceleb",
    "celebdf",
    "faceforensics",
    "dfdc"
]


def is_relevant(item):

    text = (
        str(item.get("title", "")) + " " +
        str(item.get("description", ""))
    ).lower()

    score = 0

    for keyword in IMPORTANT_KEYWORDS:

        if keyword in text:
            score += 1

    return score >= 2