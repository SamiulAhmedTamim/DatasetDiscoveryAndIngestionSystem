import json
import numpy as np

from database.database import SessionLocal
from database.models import Dataset
from services.embedding_service import model


def search(query, top_k=10):

    db = SessionLocal()

    q = model.encode(query, normalize_embeddings=True)

    scores = []

    for d in db.query(Dataset).all():

        emb = np.array(json.loads(d.embedding))

        sim = float(np.dot(q, emb))

        scores.append((sim, d))

    db.close()

    scores.sort(reverse=True, key=lambda x: x[0])

    return scores[:top_k]