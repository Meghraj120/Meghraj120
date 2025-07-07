import requests
from bs4 import BeautifulSoup
import json
import csv

url = "http://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Cannot fetch page")
        return

    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="product_pod")

    books = []

    for article in articles:
        title = article.h3.a['title']
        price_text = article.find("p", class_="price_color").text
        currency = price_text[0]
        price = float(price_text[1:])

        print(title, currency, price)

        books.append({
            "title": title,
            "currency": currency,
            "price": price
        })

    
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(books, f, indent=2, ensure_ascii=False)

    print("\nSaved book data to 'books.json'.")

    
    with open("books.csv", mode="w", newline='', encoding="utf-8",newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "currency", "price"])
        writer.writeheader()  # Write header row
        writer.writerows(books)  # Write book data

    print("\nSaved book data to 'books.csv'.")

scrape_books(url)



#go to git bash
#git config --m global username"Meghraj12"
#git config --m global email "meghraj12@gmail.com"

#git init
#git status=>if you want to add all files then use git add .
#git diff => to see the changes

#git add .
#git commit -m "your first message"
#copy paste git from githubgi