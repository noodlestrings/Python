import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
# .prettify cleans up the beatuiful soup output
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
dev_jobs = results.find_all(
    "h2", string=lambda text: "developer" in text.lower())
# ^finds all h2 elements with the string developer
# dev_job_elements = [h2_element.parent.parent.parent for h2_element in dev_jobs]
# print(dev_job_elements)

# for job_element in job_elements:

#     title_elements = job_element.find("h2", class_="title")
#     company_elements = job_element.find("h3", class_="company")
#     location_elements = job_element.find("p", class_="location")
#     print(title_elements.text.strip(), company_elements.text.strip(),
#           location_elements.text.strip(), "\n\n")
#     # .text gets only the text values of the html
#     # .strip gets rid of the white space
#     print()

# print(soup)
