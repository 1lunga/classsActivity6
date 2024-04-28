#21800060 LG Nyasengo
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/June Gemini/Downloads/dataset - 2020-09-24.csv")
#display first 5 rows
print(df.head(5))

#display last 5 rows
print(df.tail(5))

#display first 3 rows
print(df.head(3))

#count number of missing entries
missing_values = df.isnull().sum()
print(missing_values)

#find and count duplicate rows
duplicates = df.duplicated().sum()
print("Number of duplicate entries:", duplicates)

#Ploting histogram for numeric column
df['Wins'].hist()
plt.show()
