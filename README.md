# Slooze – Data Engineering Take-Home Challenge

This repository contains an **end-to-end Data Engineering solution** built as part of the Slooze take-home challenge.  
The project demonstrates **data collection, ETL, data cleaning, and exploratory data analysis (EDA)** on real-world B2B marketplace data.

The focus of this solution is **practical data engineering**, not perfect data.

---

## 📌 Problem Overview

The objective of this challenge was to:

- Collect product data from a B2B marketplace (IndiaMART or similar)
- Build a reliable data collection pipeline
- Clean and normalize the collected data
- Perform exploratory data analysis to extract insights
- Clearly document assumptions, limitations, and findings

---

## 🧠 Key Engineering Decisions

### Why IndiaMART?
IndiaMART is a large B2B marketplace with:
- Unstructured product listings
- Inconsistent supplier information
- Dynamic rendering on listing pages

This makes it a **realistic data source** for evaluating data engineering skills.

---

### Why Product Detail Pages Instead of Listing Pages?
IndiaMART listing/search pages are **JavaScript-rendered**, which makes static scraping unreliable.

To ensure robustness:
- Listing pages were used **only to extract product detail URLs**
- Actual data was scraped from **individual product detail pages**, which are largely static

This approach improves:
- Reliability
- Repeatability
- Data accuracy

---

## 🗂️ Project Structure

slooze-data-engineering-challenge/
│
├── crawler/
│ └── scraper.py # Data collection (Part A)
│
├── eda/
│ └── eda_analysis.py # Cleaning + EDA (Part B)
│
├── data/
│ ├── indiamart_hyderabad_packaging_machines.csv
│ └── indiamart_hyderabad_packaging_machines_clean.csv
│
├── requirements.txt
└── README.md


---

## 🔍 Part A – Data Collection (Crawler)

### Scope
- Product category: **Industrial / Packaging / Sealing Machines**
- Geography: **Hyderabad**
- Source: **IndiaMART product detail pages**

### Data Collected
Each row in the dataset represents one product and includes:
- Product name
- Price (raw text)
- Supplier city and state
- Product category
- Source URL

### Output
- `data/indiamart_hyderabad_packaging_machines.csv`

---

## 🧹 Part B – Data Cleaning & EDA

### Cleaning Performed
- Extracted numeric price values from messy text fields
- Handled currency encoding issues
- Identified missing values
- Detected duplicate product records
- Preserved raw data for traceability

### EDA Performed
- Price distribution analysis
- Basic descriptive statistics (min, max, median, variance)
- Duplicate product identification
- Supplier availability analysis
- Data quality assessment

### Output
- `data/indiamart_hyderabad_packaging_machines_clean.csv`

---

## 📊 Key Insights

- Product prices vary widely, ranging from low-cost sealing machines to high-end industrial systems
- A significant portion of listings do not publicly disclose prices
- Duplicate product listings are common across suppliers
- Supplier metadata is inconsistently available across product pages
- Marketplace data is inherently noisy and requires downstream normalization

---

## ⚠️ Data Quality Observations

This dataset reflects **real-world B2B marketplace challenges**:

- Inconsistent HTML structure across product pages
- Missing supplier information in some listings
- Prices embedded within descriptive marketing text
- Duplicate product names across different suppliers

These limitations were **intentionally documented rather than hidden**, as handling imperfect data is a core responsibility of a data engineer.

---

## ▶️ How to Run the Project

### Prerequisites
- Python 3.9+
- pip

### Install Dependencies
```bash
pip install -r requirements.txt

