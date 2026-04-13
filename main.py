import pandas as pd
from search import find_similar
from embeddings import get_embedding

df = pd.read_csv("data.csv")

df["embedding"] = df["description"].apply(lambda x: get_embedding(x).flatten())

while True:
    query = input("\nEnter what kind of place you want (or 'exit'): ")

    if query.lower() == "exit":
        break

    results = find_similar(query, df)

    print("\nTop recommendations:")
    for name, score in results:
        print(f"- {name} ({score:.4f})")