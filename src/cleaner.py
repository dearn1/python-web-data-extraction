import re


def clean_price(value):
    if value is None:
        return None

    cleaned = re.sub(r"[^0-9.]", "", value)

    try:
        return float(cleaned)
    except ValueError:
        return None


def clean_availability(value):
    if not value:
        return None

    value = value.strip()

    if "In stock" in value:
        return "In stock"

    if "Out of stock" in value:
        return "Out of stock"

    return value


def clean_integer(value):
    if value is None:
        return None

    try:
        return int(value)
    except ValueError:
        return None


def clean_text(value):
    if value is None:
        return None

    return " ".join(value.strip().split())


def clean_book_record(book):
    return {
        "title": clean_text(book.get("title")),
        "category": clean_text(book.get("category")),
        "rating": clean_text(book.get("rating")),
        "availability": clean_availability(book.get("availability")),
        "price": clean_price(book.get("price")),
        "upc": clean_text(book.get("upc")),
        "product_type": clean_text(book.get("product_type")),
        "price_excluding_tax": clean_price(book.get("price_excluding_tax")),
        "price_including_tax": clean_price(book.get("price_including_tax")),
        "tax": clean_price(book.get("tax")),
        "number_of_reviews": clean_integer(book.get("number_of_reviews")),
        "product_url": clean_text(book.get("product_url"))
    }
