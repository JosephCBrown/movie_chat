import requests
import csv
import os
from dotenv import load_dotenv
import csv


API_KEY =(os.environ["API_KEY"])
BEARER =(os.environ["BEARER"])

url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

headers = {
    "accept": "application/json",
    "api_key": API_KEY,
    "Authorization": f"Bearer {BEARER}"
}

response = requests.get(url, headers=headers)
#code to test ouput
#print(response.text)
data = response.json()
# 'genres' is the key in the JSON response containing the genres list
genres = data.get('genres', [])

# Write to CSV file
with open('genres.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name'])  # Writing header

    for genre in genres:
        writer.writerow([genre['id'], genre['name']])

print("Data exported to genres.csv")
