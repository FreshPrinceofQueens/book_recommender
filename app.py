import pickle
import streamlit as st
import numpy as np


st.header("Book Recommender System Using Machine Learning")
model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/book_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_ratings.pkl', 'rb'))
books_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

selected_books = st.selectbox(
    "Type or select a book", books_name
)