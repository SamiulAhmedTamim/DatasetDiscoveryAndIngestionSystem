import pandas as pd

from database.database import SessionLocal
from database.models import Dataset


def export():

    db = SessionLocal()

    datasets = db.query(Dataset).all()

    rows = []

    for d in datasets:

        rows.append({

            "Title": d.title,

            "Source": d.source,

            "Trust": d.trust_score,

            "Quality": d.quality_score,

            "Task": d.task,

            "Modality": d.modality,

            "Size": d.dataset_size

        })

    pd.DataFrame(rows).to_csv("datasets.csv",index=False)

    db.close()

    print("CSV exported.")