import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

filename = "product.csv"
file = open(filename, "w")

headers = "brand, product_name, price, shipping\n"
file.write(headers)

# get the url
url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=video%20card"

# download the webpage
uClient = uReq(url)

# offload the the content into a variable
page_html = uClient.read()

# close the client
uClient.close()

# parsing html
page_soup = soup(page_html, "html.parser")

# grabbing products
containers = page_soup.findAll("div", {"class":"item-container"})

# each product in containers
container = containers[0]

# grab each product
for container in containers:


    # grab the prdict brand
    brand = container.div.div.a.img["title"]

    # get the tag of item title
    title_container = container.findAll("a", {"class":"item-title"})

    # assign the title to the product name
    product_name = title_container[0].text

    # get the tag of current price
    price_container = container.findAll("li", {"class":"price-current"})
    current_price = price_container[0].text.strip().encode("utf-8")

    # get the tag of shipping
    ship_container = container.findAll("li", {"class":"price-ship"})
    shipping = ship_container[0].text.strip().encode("utf-8")

    print("brand: " + brand)
    print("product name: " + product_name)
    print("price: " + str(current_price))
    print("shipping: " + str(shipping))
    print("-------------------")

    file.write(str(brand) + "," + str(product_name) + "," + str(current_price) + "," + str(shipping) + "\n")

file.close()