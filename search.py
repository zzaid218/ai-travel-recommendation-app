import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from embeddings import get_embedding

def find_similar(user_input, df, top_n=3):
    input_embedding = get_embedding(user_input)

    scores = []

    for _, row in df.iterrows():
        dest_embedding = np.array(row["embedding"]).reshape(1, -1)

        score = cosine_similarity(input_embedding, dest_embedding)[0][0]
        scores.append((row["name"], score))

    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:top_n]