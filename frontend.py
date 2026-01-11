import streamlit as st
import requests
import pandas as pd

# --- CONFIG ---
API_URL = "http://127.0.0.1:8000"

# --- UI LAYOUT ---
st.set_page_config(page_title="Inventory AI", page_icon="📦")
st.title("📦 Supply Chain AI Agent")
st.caption("Connected to FastAPI & Google Gemini")

st.divider()

# --- SECTION 1: INVENTORY ---
st.subheader("📊 Real-Time Inventory Levels")
st.info("These items are critically low in stock.")

if st.button("Refresh Data"):
    try:
        response = requests.get(f"{API_URL}/restock")
        if response.status_code == 200:
            data = response.json()["data"]
            # Convert to a nice table
            df = pd.DataFrame(data, columns=["Product Name", "Units Sold"])
            st.dataframe(df, use_container_width=True)
        else:
            st.error("Error: Could not fetch data.")
    except Exception as e:
        st.error(f"Connection Error: Is the Backend running? {e}")

st.divider()

# --- SECTION 2: AI AGENT ---
st.subheader("🤖 AI Procurement Agent")
st.write("Generate a supplier email for the low-stock items above.")

if st.button("Draft Urgent Email"):
    with st.spinner("Consulting Gemini AI..."):
        try:
            response = requests.get(f"{API_URL}/agent/write-email")
            if response.status_code == 200:
                email_content = response.json().get("ai_response", "No content received")
                st.success("Email Drafted Successfully!")
                st.text_area("Copy this email:", value=email_content, height=400)
            else:
                st.error("AI Error: Could not generate email.")
        except Exception as e:
             st.error(f"Connection Error: {e}")