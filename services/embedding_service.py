import json
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(item):

    text = item.get("title", "") + " " + item.get("description", "")

    vector = model.encode(text, normalize_embeddings=True)

    return json.dumps(vector.tolist())