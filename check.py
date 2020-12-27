from bs4 import BeautifulSoup
import requests
# specify the url we want to scrape from
Link = "https://dramacool.so/drama-detail/moon-lovers-scarlet-heart-ryeo"
# convert the web page to text
Link_text = requests.get(Link).text
# print(Link_text)
# to convert Link_text into a BeautifulSoup Object
soup = BeautifulSoup(Link_text, 'lxml')
print(soup.title.string)
