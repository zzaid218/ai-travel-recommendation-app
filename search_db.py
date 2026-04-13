import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from db import engine
from sqlalchemy.orm import sessionmaker
from models import Destination
from embeddings import get_embedding

Session = sessionmaker(bind=engine)
session = Session()

def search(query, country=None, category=None, top_n=3):
    query_embedding = get_embedding(query).reshape(1, -1)

    results = session.query(Destination)

    if country:
        results = results.filter(Destination.country.ilike(f"%{country}%"))

    if category:
        results = results.filter(Destination.category.ilike(f"%{category}%"))

    results = results.all()

    scores = []

    for r in results:
        emb = pickle.loads(r.embedding)
        emb = np.array(emb).reshape(1, -1)

        score = cosine_similarity(query_embedding, emb)[0][0]
        scores.append((r.name, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    seen = set()
    top_results = []

    for name, score in scores:
        if name not in seen:
            top_results.append((name, score))
            seen.add(name)
        if len(top_results) == top_n:
            break

    return top_results