import pandas as pd
import pickle
from db import engine
from models import Destination, Base  
from sqlalchemy.orm import sessionmaker
from embeddings import get_embedding


Base.metadata.create_all(engine)

df = pd.read_csv("data.csv")

Session = sessionmaker(bind=engine)
session = Session()

for _, row in df.iterrows():
    embedding = get_embedding(row["description"]).flatten()

    dest = Destination(
        name=row["name"],
        country=row["country"],
        description=row["description"],
        category=row["category"],
        embedding=pickle.dumps(embedding)
    )

    session.add(dest)

session.commit()
session.close()

print("Data inserted successfully!")