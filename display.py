import data_pipeline as pipe
import os
import webbrowser

def display_database():

    data_pipe = pipe.Data_procure()
    movieList, movieList_df = data_pipe.load_movie_list()
    html_table = movieList_df.to_html(index=False)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DataFrame Display</title>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
            }}
            th {{
                background-color: #f2f2f2;
                text-align: left;
            }}
        </style>
    </head>
    <body>
        <h1>DataFrame Display</h1>
        {html_table}
    </body>
    </html>
    """

    with open("index.html", 'w') as file:
        file.write(html_content)
    
    file_path = os.path.abspath("index.html")
    webbrowser.open(f'file://{file_path}')