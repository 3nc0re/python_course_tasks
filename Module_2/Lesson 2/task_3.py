# Задача 3. Написати декоратор, що повторює виконання функції у випадку провалу
#
# Напишіть декоратор, що повторює виклик функції N разів, якщо до цього він завершився з помилкою.
#
# Якщо помилка повторюється N разів, треба видати повідомлення про помилку, але не рейзити ексепшн.

def a():
    a = 10
    b = 100

a.__code__.