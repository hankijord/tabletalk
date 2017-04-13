import sys, os, pprint, urllib, json, webbrowser

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

# Download the image to img folder
def downloadImages(imageLink, term):
    # Create img directory if if doesn't exist
    if not os.path.exists("img/"):
        os.makedirs("img/")

    # Download images from imageLink, put in img/
    urllib.urlretrieve(imageLink, "img/" + term + "." + imageLink.split('.')[-1])

def main():
    # Looks for the search term from command line argument
    for term in sys.argv[1:]:
        print("Searching for " + term + " images.")

        # Search for images
        results = searchImages(term)

        # Downloads the images to the img folder
        downloadImages(results[0], term)

if __name__ == '__main__':
    main()
