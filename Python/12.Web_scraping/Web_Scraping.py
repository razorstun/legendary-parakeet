import requests
import lxml
import bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

book = []

for i in range(1,51):
    SC = requests.get(base_url.format(i))
    PSC = bs4.BeautifulSoup(SC.text,'lxml')
    ABC = PSC.select('.product_pod')
    for prod in ABC:
        if len(prod.select(".star-rating.Two")) != 0:
            book_title = prod.select('a')[1]['title']
            book.append(book_title)

print(book)