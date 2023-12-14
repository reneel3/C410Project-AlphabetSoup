from googlesearch import search
from zenrows import ZenRowsClient
import json
import string
from rank_bm25 import BM25Okapi

# The 'crepes' function takes the specified query and inputs it into a Google search to collect the specified number of recipe URLs.
# It then uses the ZenRows package to scrape through each webpage for its title and recipe to be used as the collection of documents
# in the rankData function. This is done by returning a dictionary containing the URL keys with the Title and Recipe as each value.
# query: A string containing the food or meal the user would like recipes for.
# num: An integer for the number of ranked recipes the user wants
# return results: A nested dictionary with a URL as the key, and a dictionary as the value. 
#The second dictionary contains a key for Title and Recipe with corresponding strings as their values.
def crepes(query, num): 
    scrape_urls = []
    for url in search(query, stop=num): # Uses GoogleSearch package to collect N recipes for the user's query
        scrape_urls.append(url)

    # Uses ZenRows Web Scraper to collect Titles and Recipes from each web page as a list/collection of documents.
    resps = []
    for url in scrape_urls: 
        client = ZenRowsClient("b7b02bdb545da1de88ffffb5b1c12bbd5a3607fc")
        params = {"css_extractor" : "{\"title\":\"h1\", \"recipe\":\"p\"}" }
        response = json.loads(client.get(url,params=params).text) # ZenRows returns a string in JSON format that is converted to a dictionary
        response['recipe'] = text = " ".join(response['recipe']) # Joins list of strings in recipe into one string
        resps.append(response)

    # Creates a dictionary mapping Scraped URLs to its corresponding ZenRows Dictionary
    results = {}
    for i in range(len(scrape_urls)):
        results[scrape_urls[i]] = resps[i] 

    return results




def rankData(query, num, ingredients):

    doc = crepes(query, num)
    bmScores = {}
    print("doc: ", doc)
    titles = {}
    finalBM = {}

    for key in doc:
        newdoc = doc[key]['recipe']
        title = doc[key]['title']
        titles[key] = title

        corpus = [newdoc.translate(str.maketrans('', '', string.punctuation)).replace('\n',"").lower()]
        tokenized_corpus = [doc.split(" ") for doc in corpus]

        bm25 = BM25Okapi(tokenized_corpus)
        tokenized_query = query.lower().split(" ") + ingredients

        doc_scores = bm25.get_scores(tokenized_query)
        doc_scores = abs(float(doc_scores[0]))

        bmScores[key] = doc_scores

    finalBM = dict(sorted(bmScores.items(), key=lambda item: item[1], reverse=True))

    for key in finalBM:
        finalBM[key] = titles[key]

    return finalBM



# ingredients = ["pumpkin", "butter"]
# rankData("pumpkin pie recipes", 3, ingredients)
