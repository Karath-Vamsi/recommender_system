import requests
import os
import zipfile

class Data_procure:
    def download(self):
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

    def extract(self):
        downloads_folder = r'C:\Users\karat\OneDrive\Documents\machine learning\datasets\movies_recom_sys'
        zip_file = os.path.join(downloads_folder, 'movies_data.zip')
        output_folder = os.path.join(downloads_folder, 'movies_data')

        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(output_folder)
        print(f"Files extracted to {output_folder}")

    
