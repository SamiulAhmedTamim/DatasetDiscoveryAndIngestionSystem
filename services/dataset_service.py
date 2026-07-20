from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base


class Dataset(Base):

    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True)

    title = Column(String, unique=True)

    source = Column(String)

    url = Column(String)

    updated = Column(String)

    description = Column(String)

    downloaded = Column(Boolean, default=False)