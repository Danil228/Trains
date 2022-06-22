from datetime import datetime
import string
from collections import Counter
import csv

class_list = []  # Список с нашими рассписаниями поездов

# Блок списков со станциями прибытия
station_1921 = []
station_1937 = []
station_1902 = []
station_1929 = []
station_1981 = []
station_1909 = []

best_price = []  # Список с лучшими ценами
best_time = []  # Список с лучшим временем в пути

# Вызываем менеджер контекста что бы прочитать содержимое файла с рассписаниями поездов
with open('trains.csv', 'r') as f:
    for row in f:
        line_list = row.translate({ord(c): None for c in string.whitespace}).split(';')
        class_list.append(line_list)  # Добавляем наш файл в список


# Функция для сортировки списка рассписаний по станциям прибытия,
# так мы точно будем уверены что будем на каждой станции хоть 1 раз
# Для большого количества станций можно все автоматизирвать, но так как станций всего 6 я их ввел от руки
def st():
    for i in class_list:
        if i[2] == '1921':
            station_1921.append(i[:])
        elif i[2] == '1937':
            station_1937.append(i[:])
        elif i[2] == '1902':
            station_1902.append(i[:])
        elif i[2] == '1929':
            station_1929.append(i[:])
        elif i[2] == '1981':
            station_1981.append(i[:])
        elif i[2] == '1909':
            station_1909.append(i[:])


# Функция для определения минимальной цены в списке рассписаний по станциям прибытия
# По каждой станции находиться лучшая цена
def min_price(p):
    for i in p:
        if str(i[3]) == str(sorted(p, key=lambda x: x[3])[0][3]):  # Проверка на наличие нескольких вариантов мин. цены
            best_price.append(i)


# Функция для определения минимального времени в пути в списке рассписаний по станциям прибытия
# По каждой станции находиться лучшее время в пути
def min_time(t):
    for i in t:
        time1 = datetime.strptime(i[4], "%H:%M:%S")
        time2 = datetime.strptime(i[5], "%H:%M:%S")
        time_interval = str(time2 - time1).split()  # Ищем дельту между временем прибытием и отправкой
        i.append(time_interval[-1])
    for i in t:
        # Проверка на наличие нескольких вариантов минимального времени поездки
        if str(i[-1]) == str(sorted(t, key=lambda date: datetime.strptime(date[-1], "%H:%M:%S"))[0][-1]):
            best_time.append(i)
    for i in t:
        i.pop(-1)


# Блок вызова функций
st()
min_price(station_1921)
min_price(station_1937)
min_price(station_1902)
min_price(station_1929)
min_price(station_1981)
min_price(station_1909)
min_time(station_1921)
min_time(station_1937)
min_time(station_1902)
min_time(station_1929)
min_time(station_1981)
min_time(station_1909)
print(best_price)
print(best_time)

# Вызываем менеджер контекста что бы записать в новый файл рассписание с лучшими ценами
with open('best_price.csv', 'w', newline='') as bp:
    writer = csv.writer(bp)
    for i in best_price:
        writer.writerow(i)

# Вызываем менеджер контекста что бы записать в новый файл рассписание с лучшим врменем в пути
with open('best_time.csv', 'w', newline='') as bt:
    writer = csv.writer(bt)
    for i in best_time:
        writer.writerow(i)


# Класс для определения общего количества станций
class Trains:
    def __init__(self, arg):
        self.train_number = [i[0] for i in arg]
        self.dep_station = [i[1] for i in arg]
        self.arr_station = [i[2] for i in arg]
        self.cost = [i[3] for i in arg]
        self.dep_time = [i[4] for i in arg]
        self.arr_time = [i[5] for i in arg]

    def find_dupe(self):
        d = Counter(self.dep_station)
        v = Counter(self.arr_station)
        print(d)
        print(v)
