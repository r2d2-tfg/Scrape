from html.entities import html5
from urllib.request import urlopen
import re
from sitemapper import getPagesFromSitemap, sortURL

#array containing relevant CWE numbers
cwe_numbers = [20, 119, 120, 130, 131, 184, 190, 180, 807, 350, 784, 302, 330, 697, 680, 256, 502, 369, 835, 311, 312, 922, 642, 73, 15, 565,
328, 22, 23, 41, 59, 427, 74, 94, 95, 96, 78, 88, 89, 319, 362, 833, 93, 79, 80, 602, 1004, 352, 219, 539, 918, 618, 267, 285, 302, 732, 284, 290,
288, 276, 778, 170, 248]

#blank array to append to
patterns = []

#looping through all numbers
for z in cwe_numbers:
    #appending to create array of strings in format CWE-###
    patterns.append("cwe-"+str(z))

#blank array to fill
url_list = []
#calls function to map site and return URL's
url_list = getPagesFromSitemap("https://rules.sonarsource.com/")
#sorts URL that contain specific language
cleanList = sortURL(url_list, "python")


#for all returned URL's
for x in cleanList:
    #open, read, and decode page
    page = urlopen(x)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    
    #tries to match each CWE number to text on page
    for y in patterns:
        match = re.search(y, html, re.IGNORECASE)
        #prints CWE and url if successful
        if match:
            print(x,y)
        #else indicate running
        else:
            print("Continuing")

