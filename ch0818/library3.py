import requests
from bs4 import BeautifulSoup

url = "https://kream.co.kr/?utm_source=naver&utm_medium=cpm&utm_campaign=0816_PC&utm_content=homelink&utm_term=KREAM"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

main_section = soup.find("div", {"class": "info_box"})
top_news_ul = main_section.find("p")

top_news = top_news_ul.find_all("p")

for article in top_news:
    print(article.get_text())
