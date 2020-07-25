import requests
import json
from datetime import datetime
def URLShort(APIKey, originalURL, workspaceID = None):
    linkRequest = {
    "destination": str(originalURL),
    "domain": { "fullName": "rebrand.ly" }
    }

    requestHeaders = {
    "Content-type": "application/json",
    "apikey": str(APIKey),
    }

    if workspaceID:
        requestHeaders["workspace"] = workspaceID

    r = requests.post("https://api.rebrandly.com/v1/links", 
        data = json.dumps(linkRequest),
        headers=requestHeaders)


    if (r.status_code == requests.codes.ok):
        link = r.json()
        return (link["destination"], link["shortUrl"])

def shortURLFromFile(filepath, APIKey, workspaceID = None):
    exFilename = f"{int(datetime.utcnow().timestamp())}.csv"
    with open(filepath, "rt") as baseFile:
        while True:
            URL = baseFile.readline().rstrip()
            try:
                URL[0]
            except:
                break
            shortURL = URLShort(APIKey, URL, workspaceID)
            with open(exFilename, "a") as export:
                export.write(f"{shortURL[0]}, {shortURL[1]}\n")


shortURLFromFile(r"C:\Users\vsrme\Desktop\NewTextDocument.txt", "c7e346907f8248bf82e1200d19b7f35d")
# myAPIKey = "c7e346907f8248bf82e1200d19b7f35d"
# workspace = "c692ec9e06204f10adf073b9bca0e577"
# C:\Users\vsrme\Desktop\NewTextDocument.txt