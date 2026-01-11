
import sqlite3
import pandas as pd
import os

# --- 1. SETUP: Robust File Paths ---
script_dir = os.path.dirname(os.path.abspath(__file__))

# UPDATE THIS NAME: Make sure this matches exactly what you named your new file
csv_filename = 'Superstore_Fixed.csv' 

csv_file = os.path.join(script_dir, csv_filename)
db_file = os.path.join(script_dir, 'inventory_system.db')

if not os.path.exists(csv_file):
    print(f"❌ Error: Could not find '{csv_filename}' in {script_dir}")
else:
    print(f"✅ Found {csv_filename}. Starting database build...")

    # --- 2. INGESTION: Read the clean CSV ---
    # Since you fixed the file in Excel, we can just use the standard reader now.
    df = pd.read_csv(csv_file)
    
    # Clean column names (standardize them)
    df.columns = [c.replace(' ', '_').replace('-', '_').lower() for c in df.columns]

    # --- 3. STORAGE: Save to SQLite ---
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    df.to_sql('sales_data', conn, if_exists='replace', index=False)
    print("✅ Database built successfully!")

    # --- 4. ANALYSIS: The Business Logic ---
    print("\n--- 🔍 QUERY RESULT: Top 5 Items Running Low ---")
    
    query = """
    SELECT 
        product_name, 
        sum(quantity) as total_sold,
        round(sum(sales), 2) as total_revenue
    FROM sales_data
    GROUP BY product_name
    ORDER BY total_sold DESC
    LIMIT 5;
    """
    
    results = cursor.execute(query).fetchall()

    for rank, item in enumerate(results, 1):
        print(f"{rank}. {item[0]} (Sold: {item[1]} units | Rev: ${item[2]})")

    conn.close()