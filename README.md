# 📦 AI-Powered Supply Chain Manager

**An intelligent microservice that monitors inventory levels and uses Generative AI to automate supply chain communications.**

## 🚀 Project Overview
This project is an automated inventory management system designed to bridge the gap between **Data Engineering** and **Artificial Intelligence**.

It simulates a real-world retail environment (Superstore) where:
1.  **Sales Data** is ingested and structured into a SQL database.
2.  **A REST API** (FastAPI) provides real-time access to stock levels.
3.  **An AI Agent** (Google Gemini) analyzes low-stock items and autonomously drafts restocking emails to suppliers.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **API Framework:** FastAPI
* **Database:** SQLite (SQL)
* **AI Model:** Google Gemini 1.5 Flash
* **Data Processing:** Pandas

## ⚙️ How It Works
The system follows a 3-tier architecture:
1.  **Data Layer:** `setup_database.py` ingests raw CSV sales data and calculates current stock levels in a SQLite database.
2.  **Logic Layer:** `main.py` runs a FastAPI server that exposes endpoints to query the database.
3.  **Intelligence Layer:** When the `/agent/write-email` endpoint is hit, the system:
    * Queries the database for items with low stock.
    * Formats this data into a prompt.
    * Sends the prompt to Google's Gemini LLM.
    * Returns a professionally written, context-aware procurement email.

## 🔌 API Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Health check (System Online). |
| `GET` | `/restock` | Returns a JSON list of items that need restocking. |
| `GET` | `/agent/write-email` | **(AI Agent)** Generates a restocking email based on real-time data. |

## 📦 Installation & Setup
**1. Clone the repository**
```bash
git clone [https://github.com/jaikumbhar2007-eng/inventory-ai-agent.git](https://github.com/jaikumbhar2007-eng/inventory-ai-agent.git)
cd inventory-ai-agent
