from flask import Flask ,render_template ,request
import pandas as pd
import numpy as np
import pickle

def similar(movie):
    li=[]
    index_value = df[df['title']==movie].index[0]
    similar_movies = sorted(list(enumerate(similarity[index_value])),reverse=True,key= lambda x: x[1])
    for i in similar_movies[1:6]:
        li.append((df.iloc[i[0]].title))
    return li

ml = Flask(__name__)

@ml.route('/')
def index():
    return render_template('web.html')

df = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))



@ml.route("/suggest",methods=['POST'])
def aa():
    movie_name = str(request.form.get('movie_name'))
    sugg = similar(movie_name)

    return str(sugg)
#    return li
#def mafia(movie):
#    index_value = df[df['title'] == movie].index[0]
#    similar_movies = sorted(list(enumerate(similarity[index_value])), reverse=True, key=lambda x: x[1])
#    for i in similar_movies[1:6]:
#        suggetion =  (df.iloc[i[0]].title)
#    return  str(suggetion)

#   movie = str(request.form.get('movie_name'))
    #result = str(movie)
    #return str(result)
if __name__ == '__main__':
    ml.run(debug=True)
