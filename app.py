import streamlit as st
import pickle

movies = pickle.load(open('movies.pkl', 'rb'))

similarity_vector = pickle.load(open('similarity_vector.pkl', 'rb'))

st.header(body="Movie Recommender System based on ImDb best 10 000 movies", divider='rainbow')
st.subheader(body="based on ImDb best 10 000 movies", anchor=None, help=None, divider=False)

selected_movie = st.selectbox("Select a movie", movies)

movies_list = movies["title"]

class Retrieve_data():
    def __init__(self, dataset, title):
        self.dataset = dataset
        self.title = title

    def get_index_from_title(self):
        try:
            return self.dataset[self.dataset["title"]==self.title].index[0]
        except:
            print("Either the movie or the dataset doesn't exist")

    def recommended_movies(self, index, number):

        recommended_movies = []

        self.distance = sorted(list(enumerate(similarity_vector[index])), reverse=True, key=lambda vector:vector[1])

        for movie in self.distance[1:number+1]:
            recommended_movies.append(movies.iloc[movie[0]].title)
        
        return recommended_movies

if st.button("Show recommended movies"):

    data_retrieved = Retrieve_data(movies, selected_movie)
    index = data_retrieved.get_index_from_title()
    recommendations = data_retrieved.recommended_movies(index, 5)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
    with col2:
        st.text(recommendations[1])
    with col3:
        st.text(recommendations[2])
    with col4:
        st.text(recommendations[3])
    with col5:
        st.text(recommendations[4])

