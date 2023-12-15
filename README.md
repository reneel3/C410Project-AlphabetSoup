# C410Project-AlphabetSoup

## Overview

Our Project is called Alphabet Soup. We were inspired by the trouble it takes for one to find a recipe that best suits their needs, such as their dietary restrictions or current ingredients on hand. We decided that we would solve this problem by creating an all-in-one dynamic program that would take all these factors into mind. By combining our diverse skillset and creative minds, we came together to create a mechanism that mimics a Google search query. Users would be able to enter the recipe of their choice, along with any dietary restrictions they may have, plus their preferred ingredients to cook with. Our program would take all these factors into consideration and then use a variety of Python packages to provide a ranked list of URLs with recipes that best suit the users' tastes.

## How it Works

We started by creating an input form using the Tkinter package. This form allows the user to input their desired recipe, number of desired recipes, dietary restrictions, and preferred ingredients. The form builds a query based off of the user inputs and triggers the search query, which then uses the GoogleSearch package to crawl the desired number of links. This information is then utilized by another package called ZenRows, which scrapes through each webpage and pulls the relevant data, including the title and recipe itself. Next, this data is passed to our ranking function, which creates our corpus and query to be used by the BM25 ranking function to return the URLs in the order of most relevant to the query. Finally, the results are displayed in another window, which displays the links with their titles in their ranked order. The displayed results can be clicked on by the user to automatically copy the URL to the user's clipboard. 

## Installation
```
pip install rank_bm25
pip install zenrows
pip install google

```

## Get Started
This program runs on Python 3.9

Run the RecipeInputForm.py  
`python RecipeInputForm.py`

This file will run all the other necessary functions for the program to work.

The results will be displayed in a separate window.

## Supplements

We've kept a Supplements directory to save our previous efforts in building our program using Python 3.5. This includes pursuits in creating a web crawler using BeautifulSoup4 to collect Google search result URLs. We also developed a web scraper using Selenium to input the user's query to Google as well as pull the title and recipe from relevant web pages. Lastly, we attempted to create a Google Chrome extension for collecting the user's inputs. The decisions to switch to Python 3.9 and packages such as Tkinter, GoogleSearch, and ZenRows were all made to optimize the user's experience in both runtime and ease of use.
