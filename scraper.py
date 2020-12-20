from urllib.request import urlopen
from bs4 import BeautifulSoup as bsp

# initializing the url
product = "Intel Core2 Extreme Processor QX9650"
product_for_link = product.replace(" ", "+")
url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={product_for_link}&_sacat=0&_pgn=1"

# loading webpage data
web_page = urlopen(url).read()

# csv handling
filename = f"{product}s.csv"
f = open(filename, "w")
headers = "Title,Price,Shipping,No_of_ratings,Link\n"
f.write(headers)

# passing the webpage to BeautifulSoup html parser
page_soup = bsp(web_page, "html.parser")

# finding the units we need
items = page_soup.findAll("div", {"class": "s-item__wrapper clearfix"})

# iterating the each item
for item in items:
    title = item.div.div.div.img["alt"].replace(",", "-").strip(',')
    link = item.div.a["href"].replace(",", "-").strip(',')
    price = item.findAll(
        "span", {"class": "s-item__price"})[0].text.replace(",", "-").strip(',')
    shipping = item.findAll(
        "span", {"class": "s-item__shipping s-item__logisticsCost"})[0].text.replace(",", "-").strip(',')
    try:
        No_of_ratings = item.findAll(
            "span", {"class": "s-item__reviews-count"})[0].span.text.replace(",", "-").strip(',')
    except:
        No_of_ratings = 0

    f.write(f"{title},{price},{shipping},{No_of_ratings},{link}\n")

f.close()
