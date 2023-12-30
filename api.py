import requests
import pandas
import os
from dotenv import load_dotenv


#loads the .env that contains api keys
load_dotenv()

#assigns the api variable to the key in the .env  file
API_KEY =(os.environ["API_KEY"])
BEARER =(os.environ["BEARER"])
#url + the api key variable to access the data
#url = f"https://api.themoviedb.org/3/movie/550?api_key={API_KEY}"

#Movies Released in 2023
url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&primary_release_year=2023&sort_by=popularity.desc"

# Parameters for the API request
params = {
    "api_key": API_KEY,
    "include_adult": "false",
    "include_video": "false",
    "language": "en-US",
    "primary_release_year": "2023",
    "sort_by": "popularity.desc"
}

#assigns the content type (output request)
header={"Content-Type":"application/json",
        "Accept-Encoding":"deflate",
        "Authorization": "Bearer ={BEARER}"}

response = requests.get(url, headers=header, params=params)
data = response.json()
print(data)  # Add this line to print the entire response

# Initialize variables for pagination
all_results = []
page = 1
max_pages = 500  # Maximum number of pages allowed by the API

# Loop through each page of API results
while page <= max_pages:
    params["page"] = page
    response = requests.get(url, headers=header, params=params)
    data = response.json()

    # Check if 'results' key is in the response
    if 'results' in data:
        all_results.extend(data['results'])
    else:
        print(f"No results or error found on page {page}, response: {data}")
        break  # Exit the loop if 'results' is not found or there's an error

    page += 1

# Create a DataFrame from the results
df = pandas.json_normalize(all_results)
print(df)

csv_file_path = '/Users/josephbrown/Desktop/Business/Data_Freelancer/DataUnity/jb_io/movie_chat_tool/file.csv'
# Export the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"Data exported to {csv_file_path}")

