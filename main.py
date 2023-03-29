import requests
from send_email import send_email


topic = "palantir"
api_key = "ac8bcd9c0c454bc886e75a9c172fa9a4"

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=ac8bcd9c0c454bc886e75a9c172fa9a4&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Check if articles key exists
if "articles" in content:
    # Access the article titles and description
    body = ""
    for article in content["articles"][:30]:
        if article["title"] is not None:
            body = "Subject: Today's News" + "\n"\
                   + body + article["title"] + "\n" \
                   + article["description"] + "\n" \
                   + article["url"] + 2 * "\n"

    body = body.encode("utf-8")
    send_email(message=body)
else:
    print("No articles found.")
