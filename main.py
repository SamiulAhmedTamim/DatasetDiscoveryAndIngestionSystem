import os

from discovery.manager import discover_all
from database.database import Base, engine
from database.models import Dataset
from 
def main():
    Base.metadata.create_all(bind=engine)
    datasets = discover_all()

    print("\nFound", len(datasets), "results\n")

    for i, item in enumerate(datasets, start=1):

        print("=" * 60)

        print(item["title"])

        print(item["source"])

        print(item["url"])

        print(item["updated"])

        print(item["description"])

        print()

if __name__ == "__main__":
    main()
    
    print("\nGenerating Statistics...\n")

    os.system("python experiments/dataset_statistics.py")