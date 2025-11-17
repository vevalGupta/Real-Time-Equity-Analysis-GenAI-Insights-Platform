import streamlit as st
import pandas as pd
import plotly.express as px
import Working

# ================= PAGE HEADER ===================
st.title("📈 Smart Stock Analyzer & Query Engine")
st.subheader("Upload your stock data (CSV or Excel) and ask questions naturally!")

# ================= FILE UPLOAD ===================
st.markdown("### 📂 Upload Stock Data File")
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    
    # Load DataFrame correctly
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("File uploaded successfully ✅")

    except Exception as e:
        st.error(f"❌ Failed to read the file: {str(e)}")
        st.stop()

    # ================= DATA PREVIEW ===================
    st.markdown("### 📊 Data Preview")
    st.dataframe(df.head())

    # ================= GRAPH SECTION ==================
    st.markdown("### 📉 Price Trend Graph")

    if ("Date" in df.columns) and ("Close" in df.columns):
        try:
            df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
            fig = px.line(df, x="Date", y="Close", title="Stock Closing Price Trend")
            st.plotly_chart(fig)
        except Exception as e:
            st.warning(f"Graph Error: {e}")
    else:
        st.warning("Make sure your file has **'Date'** and **'Close'** columns for the graph.")

   # ================= SMART QnA SECTION ==================
st.markdown("### 🤖 Ask Questions About Your Data")
ask_question = st.text_input("Ask something like: 'What is the highest closing price?'")

if ask_question:
    try:
        # Generate pandas code using your Gemini function
        generated_code = Working.pandas_code(df, ask_question)

        # --- FIX: remove backticks / markdown ---
        generated_code = (
            generated_code
            .strip()
            .replace("```python", "")
            .replace("```", "")
            .replace("`", "")
        )

        st.markdown("#### 🧠 Generated Code")
        st.code(generated_code, language="python")

        # Safe execution space
        local_vars = {"df": df}

        exec(generated_code, {}, local_vars)

        result = local_vars.get("result", None)

        # Convert result to readable answer
        final_answer = Working.user_question(ask_question, result)

        st.success(final_answer)

    except Exception as e:
        st.error(f"❌ Error while processing your question: {str(e)}")


else:
    st.info("Please upload your data file to begin analysis.")
