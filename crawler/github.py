import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

SEARCH_URL = "https://api.github.com/search/repositories"


def search_github():

    headers = {
        "Accept": "application/vnd.github+json"
    }

    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    params = {
        "q": "deepfake dataset",
        "sort": "updated",
        "order": "desc",
        "per_page": 10
    }
         
    response = requests.get(
        SEARCH_URL,
        headers=headers,
        params=params
    )

    response.raise_for_status()

    repositories = []

    for repo in response.json()["items"]:

        repositories.append({

            "title": repo["full_name"],

            "description": repo["description"],

            "url": repo["html_url"],

            "source": "GitHub",

            "updated": repo["updated_at"],

            "download_url": None

        })

    return repositories