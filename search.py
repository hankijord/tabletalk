import os, pprint, json, webbrowser
from googleapiclient.discovery import build

# Searches the web for a term and returns JSON
def searchImages(term):
    # Builds a Google Service request object
    service = build("customsearch", "v1",
           developerKey=os.environ["GOOGLE_API_KEY"])

    # Retrives the search results as json and puts in list
    results = service.cse().list(
        q=term,
        cx="017283978921110466818:dwblrst0kxk",
        searchType="image"
    ).execute()

    # Retrieve img links from the json list data
    imgLinks = []
    for item in results["items"]:
        imgLinks.append(item["link"])

    return imgLinks
