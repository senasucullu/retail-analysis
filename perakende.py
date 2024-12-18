import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\Devil\Desktop\perakende\Online Retail.xlsx"

df = pd.read_excel(file_path)

print("Verinin ilk 5 satırı:")
print(df.head())

print("\nVeri Bilgisi:")
print(df.info())

# Boş değerlerin kontrolü
print("\nBoş Değerler:")
print(df.isnull().sum())

# Veri temizliği
df = df.dropna(subset=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'UnitPrice'])


df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]


df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Ürünlerin toplam satışı
top_products = df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)

print("\nEn Çok Harcama Yapılan Ürünler:")
print(top_products)

# En çok harcama yapılan 10 ürün
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='blue')
plt.title('En Çok Harcama Yapılan Ürünler')
plt.xlabel('Ürünler')
plt.ylabel('Toplam Harcama')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
