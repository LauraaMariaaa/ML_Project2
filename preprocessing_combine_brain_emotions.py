import numpy as np
import math
import pandas as pd 



def combine_brain_emotions_per_movie(movies, emotion, output_path):
    ''' This function combines the preprocessed brain and emotion data 
        for one movie in a matrix of format (4*l) x (400 + 1 )
        -> 4 watches per movie, l = length after normalizing over several samplings
        -> 400 averages of brain regions, 1 column for emotions
        Input: 
            movies: array of strings with names of movies (should be 4 -> 4 views per movie), preprocessed
            emotion: string, name of preprocessed emotions file, for that specific movie
            output_path: string, name of location where the output should be saved
        Output:
            a .csv file combining the preprocessed emotion and brain data'''

    # load emotion data
    emotion_data = np.genfromtxt(emotion)
    l = emotion_data.shape[0]
    
    # putting the movie data together
    count = 0
    for idx, movie in enumerate(movies):
        # load movie data
        movie_data = np.genfromtxt(movie, delimiter=",")
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
            out_movies = np.concatenate((out_movies, movie_data), axis=0)

        count = count + 1
    
    # putting the emotion data together
 
    out_emotions = np.tile(emotion_data, count)


    # putting everything together

    out_combined = np.concatenate((out_movies, out_emotions[:, None]), axis=1)

    # saving the output
    pd.DataFrame(out_combined).to_csv(output_path,header=None, index=None)
        
    return 0


def combine_brain_emotions(movies, output_path):
    ''' This function puts together the data (brain and emotion) from all movies in one big matrix
    Input: 
        movies: array of strings with names of movies (Combined_...)
        output_path: string, name of location where the output should be saved
    Output:
        a .csv file combining the data for all movies'''
    
    count = 0
    for idx, movie in enumerate(movies):
        # reading the data
        movie_data = np.genfromtxt(movie, delimiter=",")
        # no output data yet (1st iteration)
        if count == 0:
            out_movies = movie_data
        # concatenate movies
        else:
            out_movies = np.concatenate((out_movies, movie_data), axis=0)
        
        count = count + 1
    
    # saving the output
    pd.DataFrame(out_movies).to_csv(output_path,header=None, index=None)




    return 0



def main():

    ########################################
    # TODO: make this for all movies
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_BickBuckBunny = ["datas/BigBuckBunny_TC_400_averaged.csv", 
                "datas/BigBuckBunny_TC_400_averaged.csv",
                "datas/BigBuckBunny_TC_400_averaged.csv",
                "datas/BigBuckBunny_TC_400_averaged.csv"]

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_BickBuckBunny = "datas/Emotions_BigBuckBunny.csv"

    # enter the output path
    output_path_BickBuckBunny = "results/Combined_BickBuckBunny.csv"

    combine_brain_emotions_per_movie(movies_BickBuckBunny, emotion_BickBuckBunny, output_path_BickBuckBunny)

    ########################################
    # TODO: put all output paths names in the list
    ########################################

    all_movies = [output_path_BickBuckBunny]

    final_output = "results/Combined_All.csv"

    combine_brain_emotions(list, final_output)



if __name__ == "__main__":
    main()


