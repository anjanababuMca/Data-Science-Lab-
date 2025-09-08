import matplotlib.pyplot as plt
import pandas as pd

data={'Fruits':['Apple','Banana','Orange', 'Grapes', 'Mango'],'sales':[150,200,120,90,180]}
df = pd.DataFrame(data)
df.to_csv('fruits_sales.csv',index=False)
df=pd.read_csv('fruits_sales.csv')
plt.bar(df['Fruits'],df['sales'],color='skyblue')
plt.xlabel('Fruits')
plt.ylabel('Sales')
plt.title('Fruits Sale Data- Bar Chart')
plt.show()

plt.scatter(df['Fruits'],df['sales'],color='red',s=100)
plt.xlabel('Fruits')
plt.ylabel('Sales')
plt.title('Fruits Sale Data- Scatter Plot')
plt.show()