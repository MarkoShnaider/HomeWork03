import datetime

def get_days_from_today(date):
    
    try:
        date_object = datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print('Неправильний формат дати!')
        return None

    today = datetime.datetime.today()

    days_difference = (today - date_object).days

    return days_difference


# Приклад використання функції
date = '2023-03-08'
days_difference = get_days_from_today(date)

print('Кількість днів від', date, 'до поточної дати:', days_difference)