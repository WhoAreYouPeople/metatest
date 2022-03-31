#All of this... for a mere metadata scrap.

#Needed for cloudflare
import httpx
import asyncio


import sqlite3
import re
import zipfile
import os
import sys



with httpx.Client(http2=True) as client:
    #Only these two are needed, the progress made by adding additional information wasn't actually needed. Who'd have thunk it?
    headers ={'Cookie' : 'cf_clearance=COOKIE',
'User-Agent' : 'USERAGENT'}
    linktodo = "URLTODOWNLOAD"
#Request webpage passing cookies and user agent to avoid cloudflare.
    print(headers)
    r = httpx.get(linktodo, headers=headers)
#I am positive this isn't need, but I'm tired.
#If holding file is found remove it, if not, then dont.
if os.path.exists("holding"):
    os.remove("holding")
else:
    None
print("Downloading html for extraction.")
#Save webpage, probably could have been a string.... I may fix that
file = open('holding', 'wb')
file.write(r.content)
file.close()
