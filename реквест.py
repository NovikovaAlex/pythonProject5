import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


r = requests.get('https://urban-university.pro')
print(r.text)
#возможность с помощью кода искать информацию,картинки, поставить на поток отправку сообщений в мессенджерах


df = pd.read_csv('products.txt')
pot_df = df[df['Potato'] == 'Potato']
print(pot_df)
numeric_df = df.apply(pd.to_numeric, errors='coerce')
total_sum = numeric_df.sum().sum()

print("Сумма всех чисел в файле:", total_sum)
# в файле по старому заданию отобрала только бульбу. возможность структурировать данные файлов по методам, которые нужны: числа, строки и тд, и работать с ними

arr = np.array([1, 2, 3, 4, 5])
print(arr)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
print(a ** 2)
data = np.array([1, 2, 3, 4, 5])
print(np.mean(data))
# помощник для вычислительных математических операций


x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('График синуса')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]
plt.bar(categories, values)
plt.title('Столбчатая диаграмма')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.show()

sizes = [15, 30, 45, 10]
labels = ['Категория A', 'Категория B', 'Категория C', 'Категория D']
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']


plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal') 
plt.title('Круговая диаграмма')
plt.show()
# прикольно создает графики каких захочешь видов




