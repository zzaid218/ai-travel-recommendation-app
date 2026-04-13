from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_embedding(text):
    """
    Convert text into a semantic embedding vector.
    Returns a 2D vector (1, 384) for cosine similarity.
    """
    return model.encode(text).reshape(1, -1)