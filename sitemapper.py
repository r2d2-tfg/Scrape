
from email.contentmanager import raw_data_manager
from usp.tree import sitemap_tree_for_homepage
import re

#function to map site and return URL's
def getPagesFromSitemap(fullDomain):

    listPagesRaw = []
    listURLs = []

    tree = sitemap_tree_for_homepage(fullDomain)
    for page in tree.all_pages():
        listPagesRaw.append(page.url)
    
    for page in listPagesRaw:
        
        if page in listURLs:
            
            pass

        else:
            
            listURLs.append(page)


    return listURLs
    
#function to check URL's for language
def sortURL(listURLs, lang):
    URLs = []

    for x in listURLs:
        match = re.search(lang, x, re.IGNORECASE)
        if match:
            URLs.append(x)

    return(URLs)







