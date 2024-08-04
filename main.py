import data_pipeline as pipe
from display import display_database
import model as sys
import numpy as np
import tensorflow as tf

def create_ratings(movieList):

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

    return my_ratings, my_rated

def main():

    # activate the data pipeline
    data_pipe = pipe.Data_procure()

    data_pipe.load_extract()
    movieList, movieList_df = data_pipe.load_movie_list()

    # Rate some movies
    my_ratings, my_rated = create_ratings(movieList)

    Y, R = data_pipe.load_ratings()

    Y = np.c_[my_ratings, Y]
    R = np.c_[(my_ratings != 0).astype(int), R]

    # Train the model
    model = sys.Model_builder()
    X, W, b, Ymean = model.model(Y, R, 1)

    predictions = model.predict(X, W, b, Ymean)

    my_predictions = predictions[:,0]

    ix = tf.argsort(my_predictions, direction='DESCENDING')

    print('\nTop recommendations for you:\n')
    for i in range(15):
        j = ix[i]
        if j not in my_rated:
            print(f'{i+1}. {movieList[j]}')

    test = input("Would you like to test the model? (y/n): ")   
    if test.lower() == 'y':
        model.test_model(my_ratings, my_predictions, movieList)

if __name__ == '__main__':
    display_database()
    action = input("Would you like rate some movies? (y/n): ")

    if action.lower() == 'y':
        main()