"""
    Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
Вимоги до завдання:

Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
Для роботи з датами слід використовувати модуль datetime Python.

Рекомендації для виконання:

Імпортуйте модуль datetime.
Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
Отримайте поточну дату, використовуючи datetime.today().
Розрахуйте різницю між поточною датою та заданою датою.
Поверніть різницю у днях як ціле число.

"""
from datetime import datetime


def get_days_from_today(date):
    current_date = datetime.today().date()   # візьмемо поточну дату
    try:
        # спроба перетворити дату від користувача в об'єкт datetime
        user_data = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        print('Дата введена некорректно.\nБудь ласка, введіть дату у форматі "РРРР-ММ-ДД"')
        return None  # хоча функція в разі помилки і так поверне None зазначимо це наглядності і розуміння нащадками
    # окремо порахуемо різницю і візмемо лише дні, щоб не захаращувати оператор return
    res = (current_date - user_data).days
    return res


if __name__ == '__main__':
    # блок автотесту
    # тестові дати, минула, майбутня, сьогоденна і з помилкою
    curr = datetime.today().strftime("%Y-%m-%d")
    dates = ['2020-10-09', '2025-10-09', curr, '2024-18-20']
    # виклик і перевірка можна додати вивід результату
    for data in dates:
        res = get_days_from_today(data)
        # якщо дата задана правильно, тобто результат функції не None
        if res != None:
            print(data, 'різниця між поточною датою:', res)
            # перевірка що результат фуекції число а не обьект timedelta
            # print(type(res))
