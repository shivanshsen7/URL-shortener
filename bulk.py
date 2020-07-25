from app import URLShort, shortURLFromFile 
import os, time
API = input("Enter Your API Key: ")
workspace = input("Enter Workspace if needed or press [Enter] Key: ")

print("Choose method via File [F] or Console [C]")
_method = True if input().lower() == "f" else False

if _method:
    filepath = input("Input FileName if not in same folder \nalso enter with absolute path :\n")
    try:
        filename = shortURLFromFile(filepath, API, workspace)
    except:
        print("Workspace Key might be Broken, Trying for Default workspace")
        filename = shortURLFromFile(filepath, API)
    finally:
        print(f"{os.getcwd()} is your Directory and {filename}.csv")
        print("is the filename for Short URLs in your Directory.")

while not _method:
    oURL  = input("Long URL: ")
    if not oURL:
        break
    short = URLShort(API, oURL, workspace)
    print(short) 
    time.sleep(2)
