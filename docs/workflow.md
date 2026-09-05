# Data Extraction Workflow

This document explains the scraping, cleaning, validation, and export workflow used in this project.

## 1. Source Selection

The project uses Books to Scrape:

https://books.toscrape.com/

This website is designed for practicing web scraping and contains paginated book listings and product detail pages.

## 2. Extraction Process

The scraper starts from the first catalogue page and processes listing pages one by one.

For each listing page, it extracts:

- Title
- Price
- Availability
- Rating
- Product detail page URL

The scraper then visits each product detail page and extracts:

- Category
- UPC
- Product type
- Price excluding tax
- Price including tax
- Tax
- Number of reviews

## 3. Cleaning Process

The cleaning process normalizes:

- Price fields into numeric float values
- Review count into integer values
- Availability values into consistent text
- Text fields by trimming whitespace and removing extra spaces

## 4. Validation Process

The validation process checks for:

- Missing titles
- Missing prices
- Invalid prices
- Missing product URLs
- Missing availability values
- Missing UPC values
- Duplicate product URLs

A validation report is generated as JSON.

## 5. Export Process

The final cleaned dataset is exported into:

- CSV
- JSON

The validation report is exported into:

- JSON

## 6. Reliability Considerations

The scraper includes:

- Request timeout handling
- Modular code structure
- Detail page extraction
- Controlled delay between requests
- Validation before delivery

## 7. Future Enhancements

Future enhancements could include:

- Selenium or Playwright support for JavaScript-rendered content
- Proxy support
- Retry logic
- Structured logging
- Docker support
- Cloud execution using Azure or AWS
- LLM-assisted extraction or classification