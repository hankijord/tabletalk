import sys, os, pprint, urllib, json, webbrowser

# Used to determin file extension
from mimetypes import guess_extension

# Google Custom Search API
from googleapiclient.discovery import build

class Searcher:
    # Initialisation
    def __init__(self):
        # initialise stuff now
        self.directory = "visualisation/images/" 

    # Searches the web for a term and returns JSON
    def searchImages(self, term):
        # Builds a Google Service request object
        service = build("customsearch", "v1",
               developerKey=os.environ["GOOGLE_API_KEY"])

        # Retrives the search results as json and puts in list
        results = service.cse().list(
            q=term,
            cx="017283978921110466818:dwblrst0kxk",
            searchType="image",
            imgType="photo",
            imgSize="xlarge"
        ).execute()

        # Retrieve img links from the json list data
        imgLinks = []
        for item in results["items"]:
            imgLinks.append(item["link"])
        return imgLinks

    # Download the image to img folder
    def downloadImages(self, imageLink, term):
        # Create img directory if if doesn't exist
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        # Determine the file extension
        source = urllib.urlopen(imageLink)
        extension = guess_extension(source.info()['Content-Type'], strict=True)

        # Download images from imageLink, put in img/
        # urllib.urlretrieve(imageLink, self.directory + term + "." + imageLink.split(".")[-1])
        urllib.urlretrieve(imageLink, self.directory + term + extension)

def main():
    searcher = Searcher()
    # Looks for the search term from command line argument
    for term in sys.argv[1:]:
        print("Searching for " + term + " images.")

        # Search for images
        results = searcher.searchImages(term)

        # Downloads the images to the img folder
        searcher.downloadImages(results[0], term)

if __name__ == '__main__':
    main()
