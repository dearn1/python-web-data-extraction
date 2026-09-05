def validate_dataset(records):
    report = {
        "total_records": len(records),
        "missing_title": 0,
        "missing_price": 0,
        "invalid_price": 0,
        "missing_product_url": 0,
        "missing_availability": 0,
        "missing_upc": 0,
        "duplicate_urls": 0,
        "is_valid": True,
        "issues": []
    }

    seen_urls = set()

    for index, record in enumerate(records, start=1):
        title = record.get("title")
        price = record.get("price")
        product_url = record.get("product_url")
        availability = record.get("availability")
        upc = record.get("upc")

        if not title:
            report["missing_title"] += 1
            report["issues"].append(f"Record {index}: Missing title")

        if price is None:
            report["missing_price"] += 1
            report["issues"].append(f"Record {index}: Missing price")

        if price is not None and price < 0:
            report["invalid_price"] += 1
            report["issues"].append(f"Record {index}: Invalid negative price")

        if not product_url:
            report["missing_product_url"] += 1
            report["issues"].append(f"Record {index}: Missing product URL")

        if not availability:
            report["missing_availability"] += 1
            report["issues"].append(f"Record {index}: Missing availability")

        if not upc:
            report["missing_upc"] += 1
            report["issues"].append(f"Record {index}: Missing UPC")

        if product_url:
            if product_url in seen_urls:
                report["duplicate_urls"] += 1
                report["issues"].append(f"Record {index}: Duplicate product URL")
            seen_urls.add(product_url)

    quality_issue_count = (
        report["missing_title"]
        + report["missing_price"]
        + report["invalid_price"]
        + report["missing_product_url"]
        + report["missing_availability"]
        + report["missing_upc"]
        + report["duplicate_urls"]
    )

    report["is_valid"] = quality_issue_count == 0

    return report
