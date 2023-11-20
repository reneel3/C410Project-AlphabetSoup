## CS 410 - Term Project Progress Report
Renee Liu (Team Leader) - reneel3  
Ammara Ashraf - aashra5  
Shihab Siddique - shihabs2


### 1. Which tasks have been completed? 
We completed creating the foundations of a web crawler to select the top 10 viable results from a Google search for a particular food recipe and scraping information from the particular site. This was done using the BeautifulSoup4 package with Python 3.5. The web crawler will use a generated search query as input and output a list of recipe documents for ranking. We also completed creating a base chrome extension using HTML and manifest.json. We were able to upload on chrome://extensions and see our extension.

### 2. Which tasks are pending? 
Now that we have our web crawler and chrome extension working, we need to begin ranking our data. We plan on using BM25 to rank the data, and then we will need to present that data in a summarized form for the user to easily interpret. We will continue developing the Chrome extension, database server, and web crawler to better suit our use case.

### 3. Are you facing any challenges? 
One challenge we are currently facing is being blocked from accessing information on recipe websites due to protection against bots. Further research and steps must be taken to overcome this obstacle. Some ideas to resolve the issue include using the Selenium python package to scrape each site which will allow us to combine the use of headless browsers and proxies to avoid being blocked by sites. We also anticipate some challenges in incorporating all the different components of the project to work in sync together.
