from googlesearch import search
from zenrows import ZenRowsClient
import json

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