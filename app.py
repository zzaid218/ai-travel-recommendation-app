import streamlit as st
from search_db import search

st.title("AI Travel Recommender")

query = st.text_input("What kind of trip do you want?")

country = st.text_input("Filter by country (optional)")
category = st.text_input("Filter by category (optional)")

if st.button("Search"):
    results = search(
        query,
        country if country else None,
        category if category else None
    )

    if not results:
        st.warning("No results found. Try different input.")
    else:
        st.subheader("Top Recommendations")
        for name, score in results:
            st.write(f"**{name}** ({score:.2f})")