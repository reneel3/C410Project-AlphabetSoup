from googlesearch import search
from zenrows import ZenRowsClient

query = "Pumpkin Pie Recipes"

scrape_urls = []
for url in search(query, stop=10):
    scrape_urls.append(url)
print(scrape_urls)

results = []
for url in scrape_urls:
    client = ZenRowsClient("b7b02bdb545da1de88ffffb5b1c12bbd5a3607fc")
    params = {"css_extractor" : "{\"title\":\"h1\", \"recipe\":\"p\"}"}
    response = client.get(url,params=params).text
    results.append(response)
print (results)