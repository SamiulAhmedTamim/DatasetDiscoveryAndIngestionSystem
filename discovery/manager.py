from crawler.github import search_github
from crawler.huggingface import search_huggingface
from crawler.arxiv import search_arxiv
from crawler.kaggle import search_kaggle
from crawler.zenodo import search_zenodo
from crawler.paperswithcode import search_paperswithcode

from filters.relevance import is_relevant
from services.database_service import save_dataset
from services.duplicate_service import remove_duplicates
from services.trust_service import trust_score
from services.ranking_service import rank_datasets
def discover_all():

    results = []

    print("Searching GitHub...")
    results.extend(search_github())
    print("GitHub:", len(results))

    print("Searching HuggingFace...")
    results.extend(search_huggingface())
    print("After HF:", len(results))

    print("Searching Arxiv...")
    results.extend(search_arxiv())
    print("After Arxiv:", len(results))

    print("Searching Kaggle...")
    results.extend(search_kaggle())
    print("After Kaggle:", len(results))

    print("Searching Zenodo...")
    results.extend(search_zenodo())
    print("After Zenodo:", len(results))

    print("Searching PapersWithCode...")
    results.extend(search_paperswithcode())
    print("Total found:", len(results))

    print("Filtering relevance...")

    filtered = []

    for item in results:
        if is_relevant(item):
            filtered.append(item)

    print("Relevant datasets:", len(filtered))

    print("Removing duplicates...")
    filtered = remove_duplicates(filtered)
    print("Ranking datasets...")

    filtered = rank_datasets(filtered)
    print("After dedup:", len(filtered))
    
    print("Saving to database...")

    for i, item in enumerate(filtered):
        print(f"[{i+1}/{len(filtered)}] {item['title']}")

        if save_dataset(item):
            print(" -> Saved")
        else:
            print(" -> Skipped")
    filtered.sort(
    key=lambda x: trust_score(x),
    reverse=True
)
    print("Done!")

    return filtered