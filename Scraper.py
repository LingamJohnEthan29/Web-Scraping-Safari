import requests
import bs4
import csv

URL = "https://github.com/trending"
BASE_URL = "https://github.com"

r = requests.get(URL)
soup = bs4.BeautifulSoup(r.text, 'html.parser')

repos = soup.findAll("h2", class_="h3")

with open("trending_repos.csv", mode="w",newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Repository","Link"])

    for repo in repos:
        a_tag = repo.find("a")
        if a_tag:
            title = a_tag.get_text(strip=True).replace(" / ","/")
            link = BASE_URL + a_tag['href']
            writer.writerow([title,link])
