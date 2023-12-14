from googlesearch import search
from zenrows import ZenRowsClient
import json
import string
from rank_bm25 import BM25Okapi

#query = "Pumpkin Pie Recipes"

def crepes(query, num): 
    scrape_urls = []
    for url in search(query, stop=num):
        scrape_urls.append(url)
    #print(scrape_urls)

    resps = []
    for url in scrape_urls:
        client = ZenRowsClient("b7b02bdb545da1de88ffffb5b1c12bbd5a3607fc")
        params = {"css_extractor" : "{\"title\":\"h1\", \"recipe\":\"p\"}" }
        response = json.loads(client.get(url,params=params).text)
        response['recipe'] = text = " ".join(response['recipe'])
        resps.append(response)
    #print(resps)
    
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
