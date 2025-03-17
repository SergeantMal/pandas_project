# Устанавливаем зависимости

import pandas

# Читаем файлы датасетов

data_freelancer = pandas.read_csv("freelancer_earnings_bd.csv")
data_dz = pandas.read_csv("dz.csv")

print(data_freelancer.head(),'\n') #Выводим первые 5 строк
print(data_freelancer.info(),'\n') #Выводим информацию о датасете
print(data_freelancer.describe(),'\n') #Выводим статистические данные


data_dz['City'] = data_dz['City'].fillna("нет_города") #Заполняем пропуски

group = data_dz.groupby('City')['Salary'].mean() #Считаем среднюю зарплату

print(f'Средняя зарплата по городам:\n {group}') #Выводим результат


