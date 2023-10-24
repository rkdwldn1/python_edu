import requests
from bs4 import BeautifulSoup

url = ""

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

main_section = soup.find("div", {"class": "new_area"})
top_news_ul = main_section.find("ul")

top_news = top_news_ul.find_all("span")

for article in top_news:
    print(article.get_text())
