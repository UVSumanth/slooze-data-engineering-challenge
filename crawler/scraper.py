import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import os
import re

# -------------------------
# CONFIG
# -------------------------
SEARCH_URL = (
    "https://dir.indiamart.com/search.mp?"
    "ss=automatic-sealing-machine&cq=Hyderabad"
)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

OUTPUT_FILE = "data/indiamart_hyderabad_packaging_machines.csv"
CATEGORY_NAME = "Industrial Packaging Machines"

os.makedirs("data", exist_ok=True)

# -------------------------
# STEP 1: GET SEARCH PAGE (FOR LINKS ONLY)
# -------------------------
response = requests.get(SEARCH_URL, headers=HEADERS, timeout=10)
html = response.text

# -------------------------
# STEP 2: EXTRACT PRODUCT DETAIL LINKS
# -------------------------
# Product links are embedded in page source as /proddetail/ URLs
links = set(
    re.findall(r"https://www\.indiamart\.com/proddetail/[^\"]+", html)
)

print(f"🔍 Found {len(links)} product detail links")

# Limit for safety
links = list(links)[:15]

# -------------------------
# STEP 3: SCRAPE PRODUCT DETAIL PAGES
# -------------------------
records = []

for url in links:
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        # Product Name
        h1 = soup.find("h1")
        product_name = h1.text.strip() if h1 else ""

        # Price
        price = ""
        price_tag = soup.find(string=re.compile("₹"))
        if price_tag:
            price = price_tag.strip()

        # Supplier Name
        supplier_name = ""
        supplier_div = soup.find("div", class_=re.compile("company-name"))
        if supplier_div:
            supplier_name = supplier_div.text.strip()

        records.append({
            "product_name": product_name,
            "price": price,
            "supplier_name": supplier_name,
            "supplier_city": "Hyderabad",
            "supplier_state": "Telangana",
            "category": CATEGORY_NAME,
            "source_url": url
        })

        time.sleep(random.uniform(2, 4))

    except Exception as e:
        print(f"⚠️ Error scraping {url}: {e}")

# -------------------------
# STEP 4: SAVE CSV
# -------------------------
df = pd.DataFrame(records)
df.to_csv(OUTPUT_FILE, index=False)

print(f"✅ Successfully scraped {len(df)} Hyderabad products.")
