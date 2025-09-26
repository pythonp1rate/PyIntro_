import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.imdb.com/chart/top/'

try:
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the JSON-LD script tag
    script_tag = soup.find('script', type='application/ld+json')
    if script_tag:
        data = json.loads(script_tag.string)
        movies = data.get('itemListElement', [])
        for movie in movies[:50]:
            item = movie.get('item', {})
            title = item.get('name', 'N/A')
            rating = item.get('aggregateRating', {}).get('ratingValue', 'N/A')
            print(f"Title: {title}, Rating: {rating}")
    else:
        print("Could not find JSON-LD data.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")