import os;os.system('cls')
"""
Working file
This file should Gemini Api connectivity and how gemini convert natural language into pandas command 
checklist to be Done:
1.Formation of client
2.Inputting prompt
3.connecting google gemini
         - mode type
         -content 
        -configure
4.generate response
"""
from google import genai
from google.genai import types
import pandas as pd
df =pd.read_excel("cleaned_Stock_info.xlsx")
df_cut = df.iloc[:500] 
df_cut.to_excel("cut_Stock.xlsx",index=False)
print("Trimming the data Frame Done")
print(f"The view of dataFrame used: \n {df_cut}")
Gemini_Api_key="AIzaSyCr5FFV_teEAumbA9bG0y5KeI2CajiCoYs"
# 1.Formation of client -DONE
module="gemini-2.5-flash"
client = genai.Client(api_key=Gemini_Api_key)
# 2.Inputting prompt-DONE
ask_question = str(input("Ask any question from your stock data: "))
# 3.connecting google gemini-DONE
def pandas_code(df,ask_question):
    # It should generate the pandas code from user question
    DataFrame_content =list(df_cut.columns)
    pandascode_prompt=f"""You are an expert Python data analyst whose sole purpose is to generate Pandas code to answer user questions. 
    Your output MUST be a single, executable line of Pandas code that returns the final numerical or DataFrame result. 
    do not include any text or 'df = ...' assignments.
    Available DataFrame 'df':{DataFrame_content}
    User Query: {ask_question}
    Pandas Code:"
    """
    response1=client.models.generate_content(
        model=module,
        contents =pandascode_prompt,
        config =types.GenerateContentConfig(
            temperature=1# control the creativity of gemini
        )
    )
    return response1.text

def user_question(ask_question,generated_result):
    # it is used to find the solution of user  
    userquestion_prompt=f"""
    The user asked: "{ask_question}"
    The exact calculation result from the Pandas code was: {generated_result}
    Your task is to provide a brief, professional, and conversational answer to the user's original question based only on the calculation result provided. 
    Format numerical data as currency if applicable.
    """
    response2=client.models.generate_content(
        model=module,
        contents=userquestion_prompt,
        config=types.GenerateContentConfig(
            temperature=1
        )
    )
    return response2.text
  
def main():  
    try:
        generating_code = pandas_code(df,ask_question)
        print(f"The Gemini is generating code ...  \n {generating_code}")
        generated_result = generating_code
        finial_result =user_question(ask_question,generated_result)
        print(f"Your answer is : {finial_result}")
    except Exception as e:
        print(f"There is an exception : {e}")
     
if __name__ == "__main__":
    main()