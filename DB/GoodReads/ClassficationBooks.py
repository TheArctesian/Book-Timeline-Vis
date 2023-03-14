import requests

# Fetch Data
urlEnd = "https://openlibrary.org/isbn/"

testISBN = ["0872863298", "0872863298", "0872863298"]
for i in testISBN:
    response = requests.get(urlEnd + i+ ".json")
    print(response.content)

