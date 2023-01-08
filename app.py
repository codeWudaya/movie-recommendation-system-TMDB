import streamlit as st
import pickle
import pandas as pd
import requests

# 8265bd1679663a7ea12ac168da84d2e8&language=en-US API KEY
# 'https://api.themoviedb.org/3/movie/{movie_id}?api_key={}'
#"https://image.tmdb.org/t/p/w500/" + data['poster_path'] whole path
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    # st.text(data)
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    # print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

#5.2 creating recomend function
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    # sort
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movie_posters=[]

    for i in movie_list:
        #6.fetch posters
        # movie_id=i[0]
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        #6. fetch posters
        recommended_movie_posters.append(fetch_poster(movie_id))
    return  recommended_movies,recommended_movie_posters


#showing movie list (3)
movies_Dict=pickle.load(open('movies_dict.pkl','rb')) #3.1
movies=pd.DataFrame(movies_Dict) #3.2

#reading similarity
similarity=pickle.load(open('similarity.pkl','rb'))

#1.showing title
st.title('😍 Movie Recomender System 🤞'
         'By Udaya 👌')

#2.select box
selected_movies_name =st.selectbox(
'Select movie to get Recommendation 😒 ?',
movies['title'].values)#4.showing movie list inside


#5.  create button with "recommend"(text)
if st.button('Recommend'):
    #5.3
    names,posters =recommend(selected_movies_name)#5.1
    # for i in recommendations:
    #
    #     st.write(i)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])