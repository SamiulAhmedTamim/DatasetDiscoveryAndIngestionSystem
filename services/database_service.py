from database.database import SessionLocal
from database.models import Dataset
from services.quality_service import quality_score
from services.validator import is_valid
from services.metadata_service import extract_metadata
from services.embedding_service import create_embedding
from services.trust_service import trust_score
from services.ranking_service import final_score

def save_dataset(item):
    score = quality_score(item)
    item["quality_score"] = score

    trust = trust_score(item)
    item["trust_score"] = trust

    if not is_valid(item):
        print("Invalid dataset.")
        return False

    metadata = extract_metadata(item)
    embedding = create_embedding(item)

    db = SessionLocal()

    existing = db.query(Dataset).filter(
        Dataset.title == item["title"]
    ).first()

    if existing:
        db.close()
        return False

    score = quality_score(item)
    trust = trust_score(item)
    print("Trust Score:", trust)
    ranking = final_score(item)
    dataset = Dataset(
        title=item["title"],
        source=item["source"],
        url=item["url"],
        updated=item["updated"],
        description=item["description"],
        downloaded=False,
        quality_score=score,
        modality=metadata["modality"],
        task=metadata["task"],
        dataset_size=metadata["dataset_size"],
        embedding=embedding,
        trust_score=trust,
        ranking_score=ranking,
    )

    db.add(dataset)
    db.commit()
    db.close()

    return True