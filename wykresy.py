import funkcje as f
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


a = pd.read_csv('polski2015.csv')
b = pd.read_csv('polski2023.csv')

x_1 = a['* liczba zdających']
y_1 = a['* zdawalność (%).1']
z_1 = a['średni wynik (%)']

x_2 = b['* liczba zdających.2']
y_2 = b['* zdawalność (%).3']
z_2 = b['średni wynik (%).2']


""" Histogramy reprezentujące gęstość empiryczną """

sns.kdeplot(z_1, color='navy')
sns.kdeplot(z_2, color='red')
plt.legend(['formuła 2015', 'formuła 2023'], loc='best')
plt.title("Średni wynik egzaminu maturalnego z j. polskiego")
plt.show()

sns.ecdfplot(z_1, color='navy')
sns.ecdfplot(z_2, color='red')
plt.legend(['formuła 2015', 'formuła 2023'], loc='best')
plt.title("Wykres reprezentujący dystrybuantę")
plt.show()

f.boxplot(z_1)
f.boxplot(z_2)


print('Mediana średnich wyników, formuła 2015:', f.median(z_1))
print('Mediana średnich wyników, formuła 2023:', f.median(z_2))

print('Średnia arytmetyczna dla średnich wyników, formuła 2015:', f.arithmetic_mean(z_1))
print('Średnia arytmetyczna dla średnich wyników, formuła 2023:', f.arithmetic_mean(z_2))

x_list = [k for k in range(len(z_1)//2 - 1)]
y1_list = [f.cut_mean(z_1, k) for k in range(len(z_1)//2 - 1)]
y2_list = [f.windsor_mean(z_1, k) for k in range(len(z_1)//2 - 1)]

plt.plot(x_list, y1_list)
plt.title('Średnia ucinana')
plt.axhline(y=f.arithmetic_mean(z_1), color='r', linestyle='-')
plt.axhline(y=f.median(z_1), color='g', linestyle='-')
plt.show()

plt.plot(x_list, y2_list)
plt.title('Średnia windsorowska')
plt.axhline(y=f.arithmetic_mean(z_1), color='r', linestyle='-')
plt.axhline(y=f.median(z_1), color='g', linestyle='-')
plt.show()
