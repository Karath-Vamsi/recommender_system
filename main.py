import data_pipeline as pipe
import numpy as np

def main():

    data_pipe = pipe.Data_procure()

    data_pipe.load_extract()
    movieList, movieList_df = data_pipe.load_Movie_List_pd()

    my_ratings = np.zeros(len(movieList))

    my_ratings[2700] = 5 
    my_ratings[2609] = 2
    my_ratings[929]  = 5   
    my_ratings[246]  = 5   
    my_ratings[2716] = 3   
    my_ratings[1150] = 5   
    my_ratings[382]  = 2   
    my_ratings[366]  = 5   
    my_ratings[622]  = 5   
    my_ratings[988]  = 3   
    my_ratings[2925] = 1   
    my_ratings[2937] = 1   
    my_ratings[793]  = 5   
    my_rated = [i for i in range(len(my_ratings)) if my_ratings[i] > 0]
