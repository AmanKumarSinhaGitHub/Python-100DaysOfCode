import config
import requests
import json

url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=' + config.API_KEY)

r = requests.get(url)

news = json.loads(r.text)
for article in news["articles"]:
    print("News: ", article["title"])
    print()
    print("Description: ", article["description"])

    print("\n----------------------------------------------------------------------------------------------\n")