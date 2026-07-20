from services.search_service import search


def recommend(task):

    results = search(task, top_k=20)

    ranked = sorted(
        results,
        key=lambda x: (
            x[1].trust_score,
            x[1].quality_score
        ),
        reverse=True
    )

    return ranked[:10]