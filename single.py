from app import URLShort

myAPIKey = "c7e346907f8248bf82e1200d19b7f35d"
oURL  = "https://app.rebrandly.com/workspaces"
workspace = "c692ec9e06204f10adf073b9bca0e577"


short = URLShort(myAPIKey, oURL, workspace)
print(short)