# Newegg Web Scraper (Python & Selenium)

A high-performance web scraper designed to extract product data from Newegg.com. This tool handles dynamic content, bypasses basic bot detection, and ensures data integrity.

## Features
- **Dynamic Content Handling:** Uses Selenium to render JavaScript-heavy elements.
- **Enhanced Data Extraction:** Implements a fallback mechanism for product descriptions to avoid "N/A" results.
- **Smart Scrolling:** Features iterative scrolling to trigger lazy-loaded images and text.
- **Duplicate Prevention:** Automatically filters out duplicate records during the scraping process.
- **Multi-Format Export:** Saves data in both CSV and JSON formats.

## Tech Stack
- Python 3.x
- Selenium WebDriver
- Pandas (Data Management)
- Webdriver-manager (Automatic driver handling)

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the script: `python newegg_scraper.py`
