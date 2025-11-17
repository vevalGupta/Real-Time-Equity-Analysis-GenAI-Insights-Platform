import os;os.system('cls')
"""
Data Visualization
"""
import matplotlib.pyplot as p
import pandas as pd
df=pd.read_excel("cleaned_Stock_info.xlsx")
# 1. line Graph(Stock Price Trend)
p.figure(figsize=(10,5))
p.plot(df['Date'], df['Close'], color='blue')
p.title('Stock Closing Price Trend')
p.xlabel('Date')
p.ylabel('Close Price')
p.xticks(rotation=45)
p.tight_layout()
p.show()
# # Shows how stock prices changed over time.
# # 2.bar graph(Volume Over Time)
p.figure(figsize=(10,5))
p.bar(df['Date'], df['Volume'], color='orange')
p.title('Trading Volume Over Time')
p.xlabel('Date')
p.ylabel('Volume')
p.xticks(rotation=45)
p.tight_layout()
p.show()
# To analyze trading activity
# 3. heatmap
df_cut = df.iloc[:100] 
df_cut=df_cut.select_dtypes(include=['number'])
print(df_cut.head())
df_cut=df_cut.drop(columns="Split coefficient")
# correlation
heat=df_cut.corr()
print(f"correlation between AQI Parameters: \n{heat}")
p.figure(figsize=(11,11))
p.imshow(heat,cmap="YlOrRd")
p.colorbar()
p.title("correlation matrix")
p.xticks(range(len(heat.columns)),heat.index)
p.yticks(range(len(heat.columns)),heat.index)
# code to write value in between the figure
for i in range(len(heat.columns)):
    for j in range(len(heat.columns)):# here we use lop to place corr() in correct place
        p.text(i,j,"{:.2f}".format(heat.values[i, j]))#used to put text of head variable

p.savefig("Heat_map.png",dpi=200,bbox_inches='tight')
p.show()