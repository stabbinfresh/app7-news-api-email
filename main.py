import requests
from send_email import send_email

api_key = "ac8bcd9c0c454bc886e75a9c172fa9a4"

# put the date back a few weeks before
# the current date for this url to work
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-03-10&sortBy=publishedAt&apiKey=" \
      "ac8bcd9c0c454bc886e75a9c172fa9a4"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
