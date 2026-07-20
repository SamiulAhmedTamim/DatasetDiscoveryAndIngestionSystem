from database.database import Base, engine
from database.models import Dataset

print("Tables before:", Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)

print("Done")