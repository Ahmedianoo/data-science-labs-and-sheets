
import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://quotes.toscrape.com/"

# Send HTTP request
response = requests.get(url, timeout=10)
response.raise_for_status()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Look for price values (example selectors)
# This depends on the actual page structure — may need adjustment
# Here we look for key text and then grab the next element
# prices = {}
# labels = ["24", "21", "18", "14","10"]

tags = soup.find_all('span', class_='tag-item')
top_10_tags = []
for tag in tags:
    text_tag = tag.find('a', class_='tag').text
    top_10_tags.append(text_tag)


print("top ten tags: ")
for i in range(len(top_10_tags)):
    print(f"{i + 1}. {top_10_tags[i]}")



