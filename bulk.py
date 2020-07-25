from app import URLShort
from datetime import datetime
import time
API = input("Enter Your API Key: ")
workspace = input("Enter Workspace if or needed press [Enter] Key: ")

print("Choose method via File [F] or Console [C]")
_method = True if input().lower() == "f" else False

# if _method:
#     filepath = input("Input FileName if not in same folder \nalso enter with absolute path :\n")
#     with open(filepath, 'r') as file:
#         allURLs = file.readlines()
#         allURLs = [x.rstrip() for x in allURLs]
#         exportFilename = int(datetime.utcnow().timestamp())
#         with open(f"{exportFilename}.csv", 'a') as file:
#                 file.write("Original URL, Short URL\n")
#         for URL in allURLs:
#             newURL = URLShort(API, URL, workspace)
#             with open(f"{exportFilename}.csv", 'a') as file:
#                 file.write(f"{newURL[0]}, {newURL[1]}\n")

while not _method:
    oURL  = input("Long URL: ")
    if not oURL:
        break
    short = URLShort(API, oURL, workspace)
    print(short) 
    time.sleep(2)
