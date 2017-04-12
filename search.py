import os, pprint
from googleapiclient.discovery import build

# Searches the web for a term and returns JSON
def search(term):
    # Builds a Google Service request object
    service = build("customsearch", "v1",
           developerKey=os.environ["GOOGLE_API_KEY"])

    results = service.cse().list(
        q=term,
        cx="017283978921110466818:dwblrst0kxk",
    ).execute()
    return results

def main():
    results = search("dog")
    pprint.pprint(results)

main()
