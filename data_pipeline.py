import requests
import os
import zipfile
import numpy as np
import pandas as pd
from numpy import loadtxt

class Data_procure:
    def __download(self):

        url = 'https://files.grouplens.org/datasets/movielens/ml-latest-small.zip'
        downloads_folder = r'C:\Users\karat\OneDrive\Documents\machine learning\datasets\movies_recom_sys'
        os.makedirs(downloads_folder, exist_ok=True)
        output_file = os.path.join(downloads_folder, 'movies_data.zip')

        try:
            response = requests.get(url)
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                with open(output_file, 'wb') as f:
                    f.write(response.content)
                print(f"File downloaded to {output_file}")
            else:
                print(f"Failed to download file: HTTP status code {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error downloading file: {e}")

    def __extract(self):

        downloads_folder = r'C:\Users\karat\OneDrive\Documents\machine learning\datasets\movies_recom_sys'
        zip_file = os.path.join(downloads_folder, 'movies_data.zip')
        output_folder = os.path.join(downloads_folder, 'movies_data')

        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(output_folder)
        print(f"Files extracted to {output_folder}")

    def load_extract(self):
        self.__download()
        self.__extract()

    def load_precalc_params(self):

        data_directory = r'C:\Users\karat\OneDrive\Documents\machine learning\datasets\movies_recom_sys\movies_data'

        x_file = os.path.join(data_directory, 'small_movies_X.csv')
        w_file = os.path.join(data_directory, 'small_movies_W.csv')
        b_file = os.path.join(data_directory, 'small_movies_b.csv')
        
        with open(x_file, 'rb') as file:
            X = np.loadtxt(file, delimiter=",")
        
        with open(w_file, 'rb') as file:
            W = np.loadtxt(file, delimiter=",")
        
        with open(b_file, 'rb') as file:
            b = np.loadtxt(file, delimiter=",")
        
        b = b.reshape(1, -1)
        
        num_movies, num_features = X.shape
        num_users, _ = W.shape
        
        return X, W, b, num_movies, num_features, num_users
    
    def load_ratings(self):

        data_directory = r'C:\Users\karat\OneDrive\Documents\machine learning\datasets\movies_recom_sys\movies_data'

        r_file = os.path.join(data_directory, 'small_movies_R.csv')
        y_file = os.path.join(data_directory, 'small_movies_Y.csv')
        
        with open(r_file, 'rb') as file:
            R = np.loadtxt(file, delimiter=",")
        
        with open(y_file, 'rb') as file:
            Y = np.loadtxt(file, delimiter=",")

        return Y, R
    
    def load_movie_list(self):

        data_directory = r'C:\Users\karat\OneDrive\Documents\machine learning\datasets\movies_recom_sys\movies_data'

        movie_list_file = os.path.join(data_directory, 'small_movie_list.csv')
        
        df = pd.read_csv(movie_list_file, header=0, index_col=0, delimiter=',', quotechar='"')
        mlist = df["title"].to_list()

        return mlist, df