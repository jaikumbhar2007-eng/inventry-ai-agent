from fastapi import FastAPI
import sqlite3
import os
import google.generativeai as genai

app = FastAPI()

# --- CONFIGURATION ---
script_dir = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(script_dir, 'inventory_system.db')

# PASTE YOUR KEY HERE
API_KEY = "PASTE_YOUR_KEY_HERE"
genai.configure(api_key=API_KEY)

# --- HELPER FUNCTION ---
def get_low_stock_data():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    query = """
    SELECT product_name, sum(quantity) as total_sold
    FROM sales_data
    GROUP BY product_name
    ORDER BY total_sold DESC
    LIMIT 5;
    """
    results = cursor.execute(query).fetchall()
    conn.close()
    return results

# --- ENDPOINTS ---
@app.get("/")
def home():
    return {"message": "System Online. Go to /docs to use the AI Agent."}

@app.get("/restock")
def view_restock_list():
    data = get_low_stock_data()
    return {"status": "success", "data": data}

@app.get("/agent/write-email")
def write_email_agent():
    # 1. Get Data
    raw_data = get_low_stock_data()
    
    # 2. Format Data
    data_string = "\n".join([f"- {item[0]} (Sold: {item[1]})" for item in raw_data])
    
    # 3. Prompt
    prompt = f"""
    You are a Supply Chain Manager. 
    The following items are low in stock:
    {data_string}
    
    Write a short, urgent email to 'Global Supplies' ordering these items.
    """
    
    try:
        # Use the exact model name found in your diagnostic script
        model = genai.GenerativeModel('gemini-flash-latest')
        response = model.generate_content(prompt)
        return {"ai_response": response.text}
    except Exception as e:
        return {"error": str(e)}