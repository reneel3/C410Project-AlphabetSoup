import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import multiprocessing

def scrape(url, opt, driver_path, return_dict):
    print(url)
    driver = webdriver.Chrome(options=opt, executable_path=driver_path)
    driver.get(url)

    title = driver.find_element(By.TAG_NAME, 'h1').text
    print(title)

    paras = []
    elements = driver.find_elements_by_tag_name('p')
    for el in elements:
        paras.append(el.text)
    text = " ".join(paras)
    #print(text)
    return_dict[url] = [title, text]
    print("Done")
    driver.quit()


query = "Pumpkin Pie Recipes"

opt = Options()
opt.experimental_options['prefs'] = {
    'profile.managed_default_content_settings.images': 2,
    'profile.managed_default_content_settings.javascript': 2
}
opt.headless = True
# opt.add_argument("--headless=new")
opt.add_argument("--window-size=1920,1200")

driver_path = '/Users/shihabsiddique/Repositories/alphabet_soup/chromedriver'
driver = webdriver.Chrome(options=opt, executable_path=driver_path)
driver.get('https:google.com')
# search = driver.find_element_by_name("q")
search = driver.find_element(By.NAME, "q")
search.send_keys(query)
search.send_keys(Keys.RETURN)
search_url = driver.current_url
print(search_url)
driver.quit()

response = requests.get(search_url)
soup = BeautifulSoup(response.content, "html.parser")
links = soup.select("a[href]")

crawl_urls = []
recipes = {}
# Selects First Five Secure Recipe Links
i = 0
for link in links:
    if i < 1:
        url = link['href']
        if "https://" in url:
            if not "google" in url:
                if url.startswith("/url?q="):
                    url = url[7:]
                crawl_urls.append(url)
                i += 1
    else:
        break
# print(urls)

scrape_urls = []
for url in crawl_urls:
        index = url.rindex("&sa")
        scrape_urls.append(url[:index])
print(scrape_urls)

manager = multiprocessing.Manager()
return_dict = manager.dict()
processes = []
for url in scrape_urls:
    p = multiprocessing.Process(target=scrape, args=(url, opt, driver_path, return_dict))
    p.start()
    processes.append(p)

for p in processes:
    p.join()

for item in return_dict.items():
    print(item)
    break
