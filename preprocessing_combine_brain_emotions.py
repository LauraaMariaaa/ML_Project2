import numpy as np
import math
import pandas as pd 



def combine_brain_emotions(movies, emotion, output_path):
    ''' This function combines the preprocessed brain and emotion data 
        in a matrix of format (14*4*l) x (400 + 1 )
        -> 14 movies, 4 watches per movie, l = length after normalizing over several samplings
        -> 400 averages of brain regions, 1 column for emotions
        Input: 
            movies: array of strings with names of movies, preprocessed
            emotion: string, name of preprocessed emotions file
            output_path: string, name of location where the output should be saved
        Output:
            a .csv file combining the preprocessed emotion and brain data'''

    # load emotion data
    emotion_data = np.genfromtxt(emotion)
    l = emotion_data.shape[0]
    
    # putting the movie data together
    count = 0
    for movie in range(movies):
        # load movie data
        movie_data = np.genfromtxt(movie)
        N = movie_data.shape[0] # number of samples
        D = movie_data.shape[1] # number of features, i.e. brain regions, should be 400
        if N != l: 
            print ("Length of movie "+ movie + " = " + N + " doesn't match with length of preprocessed emotion") 
            break
        # no output data yet (1st iteration)
        if count == 0:
            out_movies = movie_data
        # concatenate movies
        else:
            out_movies = np.concatenate(out_movies, movie_data, axis=0)

        count = count + 1
    
    # putting the emotion data together
    out_emotions = np.tile(l, count)

    # putting everything together
    out_combined = np.concatenate(out_movies, out_emotions, axis=1)

    # saving the output
    pd.DataFrame(out_combined).to_csv(output_path,header=None, index=None)
        
    return 0


def main():

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, ...
    movies = ["results/BigBuckBunny_TC_400_averaged.csv"]

    # enter the name of the preprocessed emotion file
    emotion = "results/emotions.csv"

    # enter the output path
    output_path = "results/Brain_Emotions_Combined.csv"

    combine_brain_emotions(movies, emotion, output_path)



if __name__ == "__main__":
    main()


