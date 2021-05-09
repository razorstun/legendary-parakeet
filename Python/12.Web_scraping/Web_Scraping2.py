import requests
import lxml
import bs4

tags = []

SC = requests.get("https://quotes.toscrape.com/")
PSC = bs4.BeautifulSoup(SC.text,'lxml')
tag_list = PSC.select(".tag")
for tag in tag_list:
    print(tag.text)