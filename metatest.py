#All of this... for a mere metadata scrap.

#Needed for cloudflare
import httpx
import asyncio


import sqlite3
import re
import zipfile
import os
import sys

#Needed for proper header order
from collections import OrderedDict

#Browser info

with httpx.Client(http2=True) as client:
                            #Put accept string here exmple: text/html,application/xhtml+xml....
    headers = OrderedDict({'Accept' : 'ACCEPTEDSTRING',
'Accept-Encoding' : 'gzip, deflate, br',
'Accept-Language' : 'en-US,en;q=0.5',
#May come up, will look like example.com 
'Alt-Used' : 'myreadingmanga.info',
'Cache-Control' : 'max-age=0',
'Connection' : 'keep-alive',
#Only works with one cookie, so wont function if it's attempting to send multiple of cookies like in http2, I am working on that.
'Cookie' : 'cf_clearance=COOKIE',
#Put host here example: example.com
'Host' : 'HOST',
#Get referal string here, example: https://example.com/
'Referer' : 'REFERER',
'Sec-Fetch-Dest' : 'document',
'Sec-Fetch-Mode' : 'navigate',
'Sec-Fetch-Site' : 'same-origin',
'Upgrade-Insecure-Requests' : '1',
'User-Agent' : 'USERAGENT'})
    linktodo = "URLTODOWNLOAD"
#Request webpage passing cookies and user agent to avoid cloudflare.
    print(headers)
    #proxies is from mitmproxy so I could view the header info, not required
    r = httpx.get(linktodo, headers=headers, proxies='http://localhost:8080', verify=False)
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
