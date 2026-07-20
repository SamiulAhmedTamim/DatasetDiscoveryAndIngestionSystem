from database.database import SessionLocal
from database.models import Dataset


def evaluate():

    db = SessionLocal()

    datasets = db.query(Dataset).all()

    total = len(datasets)

    trusted = len([d for d in datasets if d.trust_score >= 80])

    medium = len([d for d in datasets if 60 <= d.trust_score < 80])

    low = len([d for d in datasets if d.trust_score < 60])

    print("="*60)

    print("EVALUATION")

    print("="*60)

    print("Total datasets :", total)

    print("High Trust :", trusted)

    print("Medium Trust :", medium)

    print("Low Trust :", low)

    if total>0:

        print()

        print("High Trust Percentage :", round(trusted/total*100,2),"%")

    db.close()