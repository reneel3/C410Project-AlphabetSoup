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




def rankData(query, num):

    doc = crepes(query, num)
    bmScores = {}

    for key in doc:
        print("key", key)
        newdoc = doc[key]['recipe']
        print("newdoc", newdoc)

        corpus = [newdoc.translate(str.maketrans('', '', string.punctuation)).replace('\n',"").lower()]
        print("corpus: ", corpus)

        tokenized_corpus = [doc.split(" ") for doc in corpus]
        print("tokenized_corpus: ", tokenized_corpus)

        bm25 = BM25Okapi(tokenized_corpus)
        tokenized_query = query.lower().split(" ")

        doc_scores = bm25.get_scores(tokenized_query)
        print(doc_scores)

        bmScores[key] = abs(float(doc_scores))
        finalBM = sorted(bmScores.items(), key=lambda x:x[1], reverse=True)

        print("bmScores: ", finalBM)
        return bmScores

        #bm25.get_top_n(tokenized_query, corpus, n=num)


rankData("pumpkin pie recipes", 10)
