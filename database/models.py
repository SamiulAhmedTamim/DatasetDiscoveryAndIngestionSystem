from sqlalchemy import Column, Integer, String, Boolean, Float, Text
from database.database import Base


class Dataset(Base):

    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True)

    title = Column(String, unique=True)

    source = Column(String)

    url = Column(String)

    updated = Column(String)

    description = Column(Text)

    downloaded = Column(Boolean, default=False)

    quality_score = Column(Integer, default=0)

    trust_score = Column(Float, default=0)

    modality = Column(String)

    task = Column(String)

    dataset_size = Column(String)

    embedding = Column(Text)

    ranking_score = Column(Float, default=0)