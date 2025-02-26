# Задача 2: "сортування" словника.
#
# Починаючи з Python 3.7 словники зберігають порядок, у котрому в них були вставлені елементи.
# Це значить, що цим порядком можна керувати.
#
# Напишіть програму, що приймає на вхід словник і список. Повертати програма має словник, що має ключі відсортовані
# в тому ж порядку, в котрому вони перелічені в списку.
#
example_dict = {1: "a", 2: "b", 3: "c"}
example_list = [3, 2, 1]

expected_dict = {3: "c", 2: "b", 1: "a"}
