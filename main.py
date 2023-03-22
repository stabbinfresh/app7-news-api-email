import requests

api_key = "ac8bcd9c0c454bc886e75a9c172fa9a4"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-02-22&sortBy=publishedAt&apiKey=" \
      "ac8bcd9c0c454bc886e75a9c172fa9a4"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
