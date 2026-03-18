# 🦅 Newegg Market Intelligence Bot
**Autonomous High-Volume E-commerce Extraction Engine**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Automation-Selenium-red.svg?style=for-the-badge&logo=selenium)
![E-commerce](https://img.shields.io/badge/Target-Newegg-orange.svg?style=for-the-badge)
![Data](https://img.shields.io/badge/Output-CSV_&_JSON-green.svg?style=for-the-badge)

---

## ⚡ The "Smart-Extraction" Logic
This isn't just a basic scraper. Built to handle Newegg's complex JavaScript-heavy environment, this bot uses **Dynamic Rendering** and **Iterative Scrolling** to capture deep-level product data that standard scrapers miss.

> **Targeting:** High-End Tech, GPUs, CPUs, and PC Components.

---

## 🚀 Key Technical Features

### 🖥️ Dynamic Content Handling
Uses **Selenium WebDriver** to fully render JavaScript-heavy elements, ensuring that dynamic price updates and stock status are captured accurately.

### 🛡️ Smart Scrolling & Lazy-Loading
Implements an **Iterative Scroll Algorithm** that triggers Newegg's lazy-loaded images and hidden text, ensuring 100% data visibility before extraction.

### 🔄 Fallback Mechanism (No More "N/A")
Built-in logic to handle inconsistent HTML structures. If a primary selector fails, the bot automatically switches to a secondary "Fallback" path to ensure the product description is always captured.

### 🧹 Integrity & Deduplication
* **Zero-Duplicate Engine**: Uses **Pandas** to verify and filter records in real-time.
* **Multi-Format Export**: Generates both **CSV** for spreadsheets and **JSON** for developer-ready database integration.

---

## 🛠️ Tech Stack & Components

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Core Logic & Control |
| **Automation** | Selenium WebDriver | Browser Emulation & Rendering |
| **Engineering** | Pandas | Data Cleaning & Deduplication |
| **Driver Management** | Webdriver-manager | Auto-handling for Chrome Binaries |

---

## 📂 Project Structure

```text
├── src/
│   ├── newegg_scraper.py    # The Core: Extraction Engine
│   └── data_processor.py    # The Polisher: Deduplication & Formatting
├── output/
│   ├── tech_leads.csv       # Business-ready Spreadsheet
│   └── tech_leads.json      # Developer-ready JSON
├── requirements.txt
└── README.md
