import pickle
import streamlit as st
import numpy as np


st.header("Book Recommender System Using Machine Learning")

# Load our artifacts 
model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/book_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_ratings.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

selected_book = st.selectbox(
    "Type or select a book", books_name
)
def fetch_poster(suggestion):
    book_url = []

    for i in suggestion:
        # Grab the book name
        book_name = book_pivot.index[i]

        #Grab the index in the original dataframe, used to grab url 
        ids = np.where(final_rating['book_title'] == book_name)[0][0]
        url = final_rating.iloc[ids]['image_url_l']

        book_url.append(url)
    return book_url

def recommend_books(book_name):
    recommended_books = []
    # Grab the index of the book passed to the function 
    book_id = np.where(book_pivot.index == book_name)[0][0]

    # Pass this book we want to get similar books for to the model
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1,-1), n_neighbors=6)
    books_index = suggestion[0]

    book_url = fetch_poster(books_index)

    for i in books_index:
        recommended_books.append(book_pivot.index[i])
        
    return recommended_books, book_url


print(recommend_books('A Bend in the Road'))

if st.button('Show Recommendation'):
    recommendation_books, image_url = recommend_books(selected_book)
    print(image_url[5])
    
    col0, col1, col2, col3, col4 = st.columns(5)

    with col0:
        st.text(recommendation_books[1])
        st.image(image_url[1])
    with col1:
        st.text(recommendation_books[2])
        st.image(image_url[2])
    with col2:
        st.text(recommendation_books[3])
        st.image(image_url[3])
    with col3:
        st.text(recommendation_books[4])
        st.image(image_url[4])
    with col4:
        st.text(recommendation_books[5])
        st.image(image_url[5])