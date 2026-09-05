import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from cleaner import clean_book_record
from validator import validate_dataset
from exporter import export_to_csv, export_to_json, export_validation_report


BASE_URL = "https://books.toscrape.com/"
START_URL = "https://books.toscrape.com/catalogue/page-1.html"
OUTPUT_DIR = "data"


def get_soup(url):
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    return BeautifulSoup(response.text, "lxml")


def extract_rating(book_element):
    rating_classes = book_element.select_one("p.star-rating").get("class", [])
    for item in rating_classes:
        if item != "star-rating":
            return item
    return None


def extract_book_links(page_url):
    soup = get_soup(page_url)
    books = soup.select("article.product_pod")

    book_links = []

    for book in books:
        relative_url = book.select_one("h3 a").get("href")
        absolute_url = urljoin(page_url, relative_url)

        title = book.select_one("h3 a").get("title")
        price = book.select_one(".price_color").get_text(strip=True)
        availability = book.select_one(".availability").get_text(strip=True)
        rating = extract_rating(book)

        book_links.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "product_url": absolute_url
        })

    next_page = soup.select_one("li.next a")
    next_page_url = urljoin(page_url, next_page.get("href")) if next_page else None

    return book_links, next_page_url


def extract_product_details(book):
    soup = get_soup(book["product_url"])

    category = soup.select("ul.breadcrumb li a")[-1].get_text(strip=True)

    table_rows = soup.select("table.table.table-striped tr")
    details = {}

    for row in table_rows:
        key = row.select_one("th").get_text(strip=True).lower().replace(" ", "_")
        value = row.select_one("td").get_text(strip=True)
        details[key] = value

    book["category"] = category
    book["upc"] = details.get("upc")
    book["product_type"] = details.get("product_type")
    book["price_excluding_tax"] = details.get("price_(excl._tax)")
    book["price_including_tax"] = details.get("price_(incl._tax)")
    book["tax"] = details.get("tax")
    book["number_of_reviews"] = details.get("number_of_reviews")

    return book


def scrape_books(max_pages=None):
    all_books = []
    current_url = START_URL
    page_count = 0

    while current_url:
        page_count += 1
        print(f"Scraping listing page {page_count}: {current_url}")

        book_summaries, next_page_url = extract_book_links(current_url)

        for book in book_summaries:
            print(f"Extracting details: {book['title']}")
            detailed_book = extract_product_details(book)
            cleaned_book = clean_book_record(detailed_book)
            all_books.append(cleaned_book)
            time.sleep(0.3)

        if max_pages and page_count >= max_pages:
            break

        current_url = next_page_url
        time.sleep(0.5)

    return all_books


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    books = scrape_books(max_pages=3)

    validation_report = validate_dataset(books)

    csv_path = os.path.join(OUTPUT_DIR, "books_dataset.csv")
    json_path = os.path.join(OUTPUT_DIR, "books_dataset.json")
    validation_path = os.path.join(OUTPUT_DIR, "validation_report.json")

    export_to_csv(books, csv_path)
    export_to_json(books, json_path)
    export_validation_report(validation_report, validation_path)

    print("Scraping completed.")
    print(f"Records extracted: {len(books)}")
    print(f"CSV exported to: {csv_path}")
    print(f"JSON exported to: {json_path}")
    print(f"Validation report exported to: {validation_path}")


if __name__ == "__main__":
    main()
