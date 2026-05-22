# ============================================
# E-COMMERCE SALES ANALYTICS PROJECT
# DATA CLEANING + EXPLORATORY DATA ANALYSIS
# ============================================

# ---------------------------
# IMPORT LIBRARIES
# ---------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display settings
pd.set_option('display.max_columns', None)

# ---------------------------
# LOAD DATASET
# ---------------------------

print("-" * 30)
print("LOADING DATASET")
print("-" * 30)

df = pd.read_csv(
    "C:/Users/Sneha/OneDrive/Desktop/Data Analytics/E-Commerce/data/data.csv", encoding='ISO-8859-1')

print("Dataset Loaded Successfully!\n")

# ---------------------------
# BASIC DATA INSPECTION
# ---------------------------

print("-" * 30)
print("FIRST 5 ROWS")
print("-" * 30)
print(df.head())
print("\n")

print("-" * 30)
print("DATASET SHAPE")
print("-" * 30)
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n")
print("-" * 30)
print("COLUMN INFORMATION")
print("-" * 30)
print(df.info())

print("\n")
print("-" * 30)
print("MISSING VALUES")
print("-" * 30)
print(df.isnull().sum())

print("\n")
# ---------------------------
# DATA CLEANING
# ---------------------------

print("-" * 30)
print("STARTING DATA CLEANING")
print("-" * 30)

# Create copy of dataset
clean_df = df.copy()

# ---------------------------
# REMOVE DUPLICATES
# ---------------------------

duplicates = clean_df.duplicated().sum()

print(f"\nDuplicate Rows Found: {duplicates}")

clean_df.drop_duplicates(inplace=True)

print(f"Duplicate Rows Removed!")

# ---------------------------
# HANDLE MISSING VALUES
# ---------------------------

print("\nHandling Missing Values...")

# Remove rows where CustomerID is null
clean_df.dropna(subset=['CustomerID'], inplace=True)

# Remove rows where Description is null
clean_df.dropna(subset=['Description'], inplace=True)

print("Missing Values Handled!")

# ---------------------------
# REMOVE CANCELLED ORDERS
# ---------------------------

print("\nRemoving Cancelled Orders...")

# Cancelled invoices start with 'C'
clean_df = clean_df[
    ~clean_df['InvoiceNo'].astype(str).str.startswith('C')
]

print("Cancelled Orders Removed!")

# ---------------------------
# REMOVE INVALID QUANTITIES
# ---------------------------

print("\nRemoving Invalid Quantities...")

clean_df = clean_df[clean_df['Quantity'] > 0]

print("Invalid Quantities Removed!")

# ---------------------------
# REMOVE INVALID PRICES
# ---------------------------

print("\nRemoving Invalid Prices...")

clean_df = clean_df[clean_df['UnitPrice'] > 0]

print("Invalid Prices Removed!")

# ---------------------------
# CONVERT DATA TYPES
# ---------------------------

print("\nConverting Data Types...")

clean_df['InvoiceDate'] = pd.to_datetime(
    clean_df['InvoiceDate']
)

clean_df['CustomerID'] = clean_df['CustomerID'].astype(int)

print("Data Types Converted!")

# ---------------------------
# FEATURE ENGINEERING
# ---------------------------

print("\nCreating New Features...")

# Total Sales
clean_df['Sales'] = (
    clean_df['Quantity'] * clean_df['UnitPrice']
)

# Extract Date Features
clean_df['Year'] = clean_df['InvoiceDate'].dt.year
clean_df['Month'] = clean_df['InvoiceDate'].dt.month
clean_df['Day'] = clean_df['InvoiceDate'].dt.day
clean_df['Hour'] = clean_df['InvoiceDate'].dt.hour
clean_df['Weekday'] = clean_df['InvoiceDate'].dt.day_name()

print("Feature Engineering Completed!")

# ---------------------------
# CLEANED DATA SUMMARY
# ---------------------------

print("\n")

print("=" * 50)
print("CLEANED DATASET SUMMARY")
print("=" * 50)

print(clean_df.info())

print("\n")

print(clean_df.describe())

# ---------------------------
# EXPLORATORY DATA ANALYSIS
# ---------------------------

print("\n")

print("=" * 50)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# ---------------------------
# TOTAL REVENUE
# ---------------------------

total_revenue = clean_df['Sales'].sum()

print(f"\nTotal Revenue: ${round(total_revenue, 2)}")

# ---------------------------
# TOP 10 COUNTRIES
# ---------------------------

print("\nTop 10 Countries by Revenue:\n")

top_countries = (
    clean_df.groupby('Country')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_countries)

# ---------------------------
# TOP 10 PRODUCTS
# ---------------------------

print("\nTop 10 Products by Revenue:\n")

top_products = (
    clean_df.groupby('Description')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

# ---------------------------
# MONTHLY SALES TREND
# ---------------------------

monthly_sales = (
    clean_df.groupby('Month')['Sales']
    .sum()
)

# ---------------------------
# VISUALIZATIONS
# ---------------------------

sns.set_style("whitegrid")

# ---------------------------
# MONTHLY SALES CHART
# ---------------------------

plt.figure(figsize=(10, 5))

monthly_sales.plot(
    kind='line',
    marker='o'
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

# ---------------------------
# TOP COUNTRIES CHART
# ---------------------------

plt.figure(figsize=(12, 6))

top_countries.plot(
    kind='bar'
)

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.show()

# ---------------------------
# SALES DISTRIBUTION
# ---------------------------

plt.figure(figsize=(10, 5))

# sns.histplot(
#     clean_df['Sales'],
#     bins=50
# )
sns.histplot(clean_df['Sales'], bins=50, log_scale=True)

plt.title("Sales Distribution")

plt.show()

# ---------------------------
# SAVE CLEANED DATA
# ---------------------------

print("\nSaving Cleaned Dataset...")

clean_df.to_csv(
    "C:/Users/Sneha/OneDrive/Desktop/Data Analytics/E-Commerce/data/cleaned_ecommerce_data.csv",
    index=False
)

print("Cleaned Dataset Saved Successfully!")

# ---------------------------
# FINAL MESSAGE
# ---------------------------

print("\n")

print("=" * 50)
print("DATA CLEANING + EDA COMPLETED")
print("=" * 50)