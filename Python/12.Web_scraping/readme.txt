Scraping Websites

- pip install requests - allow us to to request a wesite and grab the info out of install
- pip install lxml - used by beautifulsoup to decypher whas inside the requests
- pip install bs4

- to get the website sourcecode
    - A = requests.get(website url)
    - A.text - get the source code as text(raw string)
    - soup = bs4.BeautifulSoup(A.text,'lxml') - lxml is the engine that bs4 uses
    - soup.select('title') - to grab elements from sourcecode - this retruns a list of tag objects 
    - soup.select('title')[0].gettext()
    - for item in soup.select('.toctext'):
        print(item.text)
    - grabbing an image
        -   import requests, lxml, bs4
            source_code = requests.get("link of the website")
            pretty_source_code = bs4.BeautifulSoup(source_code.text,'lxml')
            image_code = pretty_source_code.select('img')[0]
            image_link_string = image_code['src']
            image_link = requests.get(image_link_string)
            f = open('image.jpg','wb')  - wb represents writing binary to file
            f.write(image_link.content)
            f.close()
        - 



