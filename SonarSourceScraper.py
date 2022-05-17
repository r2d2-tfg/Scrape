from datetime import datetime
from html.entities import html5
from urllib.request import urlopen
import re
import psycopg2
from sitemapper import getPagesFromSitemap, sortURL

#define string for table inserts
PyInsert = "INSERT INTO soqupy (cwe, url) VALUES (%s, %s);"
JsInsert = "INSERT INTO soqujs (cwe, url) VALUES (%s, %s);"
CppInsert = "INSERT INTO soqucpp (cwe, url) VALUES (%s, %s);"
CInsert = "INSERT INTO soquc (cwe, url) VALUES (%s, %s);"

#request language to scrape
language = input('python, javascript, cpp, c:\n')


#set table query for right language and exit if invalid
if language == 'python':
    Insert = PyInsert
elif language == 'javascript':
    Insert = JsInsert
elif language == 'cpp':
    Insert = CppInsert
elif language == 'c':
    Insert = CInsert
else:
    print('invalid selection')
    quit()

#array containing relevant CWE numbers
cwe_numbers = [20, 119, 120, 130, 131, 184, 190, 180, 807, 350, 784, 302, 330, 697, 680, 256, 502, 369, 835, 311, 312, 922, 642, 73, 15, 565,
328, 22, 23, 41, 59, 427, 74, 94, 95, 96, 78, 88, 89, 319, 362, 833, 93, 79, 80, 602, 1004, 352, 219, 539, 918, 618, 267, 285, 302, 732, 284, 290,
288, 276, 778, 170, 248]

#connection to PSQL databsae

conn = psycopg2.connect(
    host = "localhost",
    database = "scraper",
    user = "scraper",
    password = "password"
    )

cur = conn.cursor()



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
cleanList = sortURL(url_list, language)


#for all returned URL's
for x in cleanList:
    #open, read, and decode page
    page = urlopen(x)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print("Page Read at:", datetime.now())
    #tries to match each CWE number to text on page
    for y in patterns:
        matched = re.search(y, html, re.IGNORECASE)
        #inserts CWE and url if successful
        if matched:
           cur.execute(Insert, (y, x))
           print("matched")
           conn.commit()

#close connection
cur.close()
conn.close()

