import requests

from utils.config import SEARCH_TERMS, HF_API


def search_huggingface():

    datasets = []

    print("=" * 70)
    print("Searching HuggingFace...")
    print("=" * 70)

    for query in SEARCH_TERMS:

        print(f"Searching: {query}")

        url = f"{HF_API}?search={query}"

        try:

            response = requests.get(url, timeout=15)

            if response.status_code != 200:
                continue

            results = response.json()

            for item in results:

                datasets.append({

                    "title": item.get("id"),

                    "source": "HuggingFace",

                    "url": f"https://huggingface.co/datasets/{item.get('id')}",

                    "updated": item.get("lastModified"),

                    "description": item.get("description", "")

                })

        except Exception as e:

            print(e)

    return datasets