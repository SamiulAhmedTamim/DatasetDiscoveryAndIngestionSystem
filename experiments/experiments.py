from database.database import SessionLocal
from database.models import Dataset


def top_datasets():

    db = SessionLocal()

    datasets = db.query(Dataset).order_by(
        Dataset.trust_score.desc()
    ).limit(20)

    print("="*60)
    print("TOP TRUSTED DATASETS")
    print("="*60)

    for d in datasets:

        print()

        print(d.title)

        print("Source :", d.source)

        print("Trust :", d.trust_score)

        print("Quality :", d.quality_score)

    db.close()