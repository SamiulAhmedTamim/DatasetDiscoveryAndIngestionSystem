from database.database import Base, engine
from database import models
from database.models import Dataset
Base.metadata.create_all(bind=engine)

print("Database created successfully!")