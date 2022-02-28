from urllib import request
import requests
from bs4 import BeautifulSoup

URL = "https://remote.co/remote-jobs/developer/"
PAGE = requests.get(URL)

SOUP = BeautifulSoup(PAGE.content, "html.parser")
print(SOUP)
results = SOUP.find_all(
    "a", class_="card m-0 border-left-0 border-right-0 border-top-0 border-bottom")
#job_elements = results.find_all("")
print(results)
#unfinished, not working
