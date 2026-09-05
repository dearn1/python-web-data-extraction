# Python Web Data Extraction Demo

This project demonstrates an end-to-end Python web scraping and data extraction workflow. It extracts structured book data from a public demo website, cleans and validates the data, and exports the final dataset to CSV and JSON formats.

## Target Website

This project uses the public scraping practice website:

https://books.toscrape.com/

The website is intentionally created for web scraping practice.

## Features

- Python-based web scraping
- Multi-page extraction
- Product detail page extraction
- HTML parsing with BeautifulSoup
- Data cleaning and normalization
- Data validation checks
- CSV export
- JSON export
- Validation report generation
- Modular project structure

## Extracted Data Fields

The scraper extracts the following fields:

- Title
- Category
- Rating
- Availability
- Product page URL
- Price
- UPC
- Product type
- Price excluding tax
- Price including tax
- Tax
- Number of reviews

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- Pandas
- CSV
- JSON

## Project Structure

```text
python-web-data-extraction/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── scraper.py
│   ├── cleaner.py
│   ├── validator.py
│   └── exporter.py
│
├── data/
│   ├── books_dataset.csv
│   ├── books_dataset.json
│   └── validation_report.json
│
└── docs/
    └── workflow.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/dearn1/python-web-data-extraction.git
cd python-web-data-extraction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the scraper

```bash
python src/scraper.py
```

### 6. Output files

The scraper generates the following files:

```text
data/books_dataset.csv
data/books_dataset.json
data/validation_report.json
```

## Data Quality Checks

The validation process checks:

- Missing titles
- Missing prices
- Invalid prices
- Missing product URLs
- Duplicate product records
- Missing availability values
- Missing UPC values

## Example Output

```json
{
  "title": "A Light in the Attic",
  "category": "Poetry",
  "rating": "Three",
  "availability": "In stock",
  "price": 51.77,
  "upc": "a897fe39b1053632",
  "product_type": "Books",
  "price_excluding_tax": 51.77,
  "price_including_tax": 51.77,
  "tax": 0.0,
  "number_of_reviews": 0,
  "product_url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
}
```

## Relevance to Data Scraping Engineering

This project demonstrates:

- End-to-end data extraction workflow ownership
- Structured data collection from HTML pages
- Data cleaning and normalization
- Dataset validation before delivery
- CSV and JSON export
- Independent troubleshooting and modular code design

## Future Enhancements

Possible future improvements:

- Add Selenium or Playwright for JavaScript-rendered websites
- Add proxy support
- Add retry logic and error handling
- Add logging with structured log files
- Add Docker support
- Add cloud deployment example using Azure or AWS
- Add LLM-assisted data normalization workflow

## Author

Endra Sim  
GitHub: https://github.com/dearn1  
LinkedIn: https://www.linkedin.com/in/endra-sim-1bbb7897/
