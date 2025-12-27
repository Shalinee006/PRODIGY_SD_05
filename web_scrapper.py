import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
URL = "https://books.toscrape.com/catalogue/page-1.html"

# Send HTTP request
response = requests.get(URL)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all product containers
books = soup.find_all("article", class_="product_pod")

# Open CSV file to store data
with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["Product Name", "Price", "Rating"])

    # Extract data from each product
    for book in books:
        name = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]  # Rating is stored as a class
        
        writer.writerow([name, price, rating])

print("Data scraped successfully and saved to products.csv")