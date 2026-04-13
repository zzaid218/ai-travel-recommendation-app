from search_db import search

while True:
    query = input("\nEnter travel idea (or exit): ")

    if query.lower() == "exit":
        break

    country = input("Filter by country (press enter to skip): ")
    category = input("Filter by category (press enter to skip): ")

    country = country if country.strip() else None
    category = category if category.strip() else None

    results = search(query, country, category)

    if not results:
        print("\nSorry, no matching destinations found.")
        continue

    print("\nTop recommendations:")
    for name, score in results:
        print(f"- {name} ({score:.4f})")