import requests
from bs4 import BeautifulSoup

url = "https://example.com/checklist"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

cards = []

for item in soup.select(".card"):
    cards.append(item.text)

print(cards)
