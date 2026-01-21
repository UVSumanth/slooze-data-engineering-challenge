import pandas as pd
import matplotlib.pyplot as plt
import re
import os

# -------------------------
# CONFIG
# -------------------------
RAW_FILE = "../data/indiamart_hyderabad_packaging_machines.csv"
CLEAN_FILE = "../data/indiamart_hyderabad_packaging_machines_clean.csv"

os.makedirs("data", exist_ok=True)

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv(RAW_FILE)

print("Initial Data Snapshot:")
print(df.head())
print("\nData Info:")
print(df.info())

# -------------------------
# CLEAN PRICE COLUMN
# -------------------------
def extract_price(text):
    """
    Extract numeric price from messy text like:
    'Automatic Sealing Machine at ₹ 85000 in Hyderabad'
    """
    if pd.isna(text):
        return None
    match = re.search(r'₹\s*([\d,]+)', str(text))
    if match:
        return int(match.group(1).replace(",", ""))
    return None

df["price_clean"] = df["price"].apply(extract_price)

# -------------------------
# DATA QUALITY CHECKS
# -------------------------
print("\nMissing Values Per Column:")
print(df.isnull().sum())

duplicate_count = df.duplicated(subset=["product_name", "price_clean"]).sum()
print(f"\nDuplicate product records (name + price): {duplicate_count}")

# -------------------------
# BASIC STATS
# -------------------------
print("\nPrice Statistics:")
print(df["price_clean"].describe())

# -------------------------
# SUPPLIER ANALYSIS
# -------------------------
top_suppliers = df["supplier_name"].value_counts().head(10)
print("\nTop Suppliers:")
print(top_suppliers)

# -------------------------
# CITY & STATE CHECK (Sanity)
# -------------------------
print("\nSupplier City Distribution:")
print(df["supplier_city"].value_counts())

# -------------------------
# SAVE CLEAN DATA
# -------------------------
df.to_csv(CLEAN_FILE, index=False)
print(f"\n✅ Cleaned dataset saved to: {CLEAN_FILE}")
print("File exists:", os.path.exists(CLEAN_FILE))

# -------------------------
# VISUALIZATIONS
# -------------------------

# Price Distribution
plt.figure()
df["price_clean"].dropna().plot(kind="hist", bins=10, title="Price Distribution (₹)")
plt.xlabel("Price (₹)")
plt.tight_layout()
plt.show()

# Top Suppliers
plt.figure()
top_suppliers.plot(kind="bar", title="Top Suppliers by Listings")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.show()

# -------------------------
# KEY OBSERVATIONS (LOGGED)
# -------------------------
print("\nKEY OBSERVATIONS:")
print("- Prices vary significantly across similar products")
print("- Several listings do not disclose prices")
print("- Supplier data is inconsistently available")
print("- Duplicate product names exist across suppliers")
