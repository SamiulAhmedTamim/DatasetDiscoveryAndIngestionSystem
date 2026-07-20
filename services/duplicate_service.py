import re
import numpy as np
from sentence_transformers import SentenceTransformer
import time

start = time.time()

model = SentenceTransformer("all-MiniLM-L6-v2")

print(f"Model loaded in {time.time()-start:.2f} seconds")


# ----------------------------
# NORMALIZATION
# ----------------------------
def normalize(text):
    text = text.lower()

    text = re.sub(r"[-_]", " ", text)

    text = re.sub(r"\bv\d+(\.\d+)?\b", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ----------------------------
# STRONG IDENTIFIER
# ----------------------------
def dataset_key(item):

    title = item.get("title", "")

    url = item.get("url", "")

    if "huggingface.co" in url:
        return "hf:" + url.rstrip("/").split("/")[-1]

    if "github.com" in url:
        parts = url.rstrip("/").split("/")
        return "gh:" + "/".join(parts[-2:])

    if "/" in title:
        title = title.split("/")[-1]

    return normalize(title)


# ----------------------------
# EMBEDDING
# ----------------------------
def get_embedding(text):
    return model.encode(text, normalize_embeddings=True)


# ----------------------------
# MERGE
# ----------------------------
def merge(base, new):

    # Keep longest description
    if len(new.get("description", "")) > len(base.get("description", "")):
        base["description"] = new["description"]

    # Keep latest update
    if new.get("updated", "") > base.get("updated", ""):
        base["updated"] = new["updated"]

    # Store all URLs
    urls = set(base.get("urls", []))
    urls.add(base.get("url"))

    if new.get("url"):
        urls.add(new["url"])

    base["urls"] = list(urls)

    # Store all sources
    sources = set(base.get("sources", []))
    sources.add(base.get("source"))

    if new.get("source"):
        sources.add(new["source"])

    base["sources"] = list(sources)

    return base


# ----------------------------
# REMOVE DUPLICATES
# ----------------------------
def remove_duplicates(items, threshold=0.92):

    start = time.time()

    titles = [
        normalize(item.get("title", ""))
        for item in items
    ]

    # Encode every title in one batch
    embeddings = model.encode(
        titles,
        normalize_embeddings=True,
        show_progress_bar=True,
        batch_size=64
    )

    key_index = {}
    results = []
    result_embeddings = []

    for item, emb in zip(items, embeddings):

        key = dataset_key(item)

        # Exact duplicate
        if key in key_index:

            idx = key_index[key]
            results[idx] = merge(results[idx], item)
            continue

        matched = False

        for i, existing in enumerate(result_embeddings):

            if float(np.dot(emb, existing)) >= threshold:

                results[i] = merge(results[i], item)
                matched = True
                break

        if matched:
            continue

        key_index[key] = len(results)

        result_embeddings.append(emb)

        results.append(item)

    print(f"Dedup finished in {time.time()-start:.2f} seconds")

    return results