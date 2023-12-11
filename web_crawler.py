import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# Google for pumpkin pie recipes
search = "https://www.google.com/search?q=pumpkin+pie+recipes&rlz=1C5CHFA_enUS989US989&oq=pumpkin+pie+recipes&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORiDARixAxiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDM0OTlqMWo3qAIAsAIA&sourceid=chrome&ie=UTF-8"

response = requests.get(search)
soup = BeautifulSoup(response.content, "html.parser")
links = soup.select("a[href]")

urls = []
recipes = {}
# Selects First Ten Secure Recipe Links
i = 0
for link in links:
    if i < 10:
        url = link['href']
        if "https://" in url:
            if not "google" in url:
                if url.startswith("/url?q="):
                    url = url[7:]
                urls.append(url)
                i += 1
        
                resp = requests.get(url)
                html = BeautifulSoup(resp.content, "html.parser")
                product = {}
                product["url"] = url
                product["title"] = html.select_one('title')
                print(product["title"])
    else:
        break

class WebCrawler():
    def launch_browser():
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")

        #driver.quit()
        while(True):
            get_url = driver.current_url
            print("The current url is:" + str(get_url))
            pass


WebCrawler.launch_browser()










