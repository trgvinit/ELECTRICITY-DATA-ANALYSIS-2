import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("/content/electricity.csv")
df.isnull().sum()
df.head()
df.dropna(subset=["nswprice", "nswdemand", "vicprice", "vicdemand"], inplace=True)

#let's plot a simple analyzation of data
plt.plot(df.nswprice[0:10],df.nswdemand[0:10], color='pink')
plt.xlabel("nswprice")
plt.ylabel("nswdemand")
plt.title("Price by Demand")
plt.show()

plt.bar(df.day,df.transfer, color='#CCCCFF')
plt.xlabel("Day")
plt.ylabel("Transfer")
plt.xticks(rotation=45)
plt.title("Electricity Transfer by Day")
plt.show()

sb.boxplot(x=df['nswprice'], color='orange')
plt.show()

plt.scatter(df.iloc[17425:17525]["vicprice"], df.iloc[17425:17525]["vicdemand"], color='skyblue')
plt.xlabel("vicprice")
plt.ylabel("vicdemand")
plt.title("Price by Demand")
plt.show()