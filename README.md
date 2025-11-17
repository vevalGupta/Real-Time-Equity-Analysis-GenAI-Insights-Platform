# FinQuery – Natural Language Financial Data Analyst

FinQuery is an intelligent financial analysis tool that converts natural-language queries into secure and optimized Pandas operations. It allows users to analyze bank statements, expense data, and financial CSV/Excel files without writing any code. Powered by GenAI + Gemini API and a safe Pandas execution engine.

---

## 🚀 Features

### 🔍 Natural Language → Pandas Code
Ask questions like:
- “Show total expenses for July”
- “Plot my monthly savings”
- “Group spending by category”

FinQuery interprets the query, generates Pandas code, validates it using AST guardrails, and executes it safely.

---

### 🛡️ Safe Execution Environment
- Strict AST validation  
- Whitelisted Pandas functions  
- Prevents unsafe operations, file access, and system-level code  
- Fully sandboxed execution  

---

### 📊 Visualizations
Generated using **matplotlib**:
- Line charts  
- Bar charts  
- Histograms  
- Correlation heatmaps  

Automatically created based on user queries.

---

### 💾 File Upload & Data Handling
- Upload CSV/Excel files  
- Auto-detects date, amount, category, merchant fields  
- Cleans and normalizes dataset for analysis  

---

### 🧠 Powered by GenAI + Gemini API
- Converts user natural-language queries into structured intents  
- Performs safe, validated Pandas code generation  
- Enhances analysis accuracy and relevance  

---

## 🧱 Tech Stack

### Backend / Core
- Python  
- Pandas  
- AST / RestrictedPython  
- Matplotlib  
- Gemini API (GenAI)

### Frontend
- Streamlit  
- Interactive charts & tables  

---

## 🧠 Data Structures Used

| Data Structure | Purpose |
|----------------|---------|
| **DataFrame** | Stores and processes uploaded financial data |
| **Dictionary** | Intent mapping, safe-op rules, AST metadata |
| **List** | Query history, allowed methods, suggestions |
| **AST Trees** | Validates Pandas code securely |
| **Custom Classes** | Code guards, interpreter, execution manager |
| **Tuples** | Immutable configuration settings |

---

## ⚙️ How It Works

1. Upload a financial CSV/Excel file  
2. Ask a natural-language question  
3. FinQuery interprets → generates safe Pandas code  
4. Validates via AST guardrails  
5. Executes securely  
6. Displays results + charts  

---

## ✨ Example Queries

- “What is the total food expenditure this month?”  
- “Plot my daily expense trend.”  
- “Compare income vs expenses for 2024.”  
- “Show the highest transaction in March.”  
- “Group expenses by category and create a bar chart.”  

---

## 🔐 Security

FinQuery includes:
- AST-based validation  
- Operation whitelisting  
- Sandbox execution  
- Protection from harmful Python expressions  

This ensures safe handling of financial datasets.

---

## ▶️ Usage

### Start the Streamlit App
```bash
streamlit run app.py
