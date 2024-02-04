import datetime

def get_upcoming_birthdays(users):
    
    today = datetime.datetime.today().date()

    upcoming_birthdays = []

    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()

       
        if birthday_this_year < today:
            birthday_next_year = birthday.replace(year=birthday.year + 1)
        else:
            birthday_next_year = birthday

        days_to_birthday = (birthday_next_year - today).days

        if 0 <= days_to_birthday <= 7:
            congratulation_date = birthday_next_year
            if birthday_next_year.weekday() in [5, 6]:
                congratulation_date = birthday_next_year + datetime.timedelta(days=7 - birthday_next_year.weekday())

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


# Приклад використання функції
users = [
    {"name": "Іван Іванов", "birthday": "1980.03.08"},
    {"name": "Петро Петров", "birthday": "1975.12.25"},
    {"name": "Марія Сидорова", "birthday": "1990.07.13"},
    {"name": "Андрій Коваленко", "birthday": "1985.04.19"},
    {"name": "Олена Павленко", "birthday": "1995.01.01"}
]

upcoming_birthdays = get_upcoming_birthdays(users)

for birthday in upcoming_birthdays:
    print(f"Вітаємо {birthday['name']} з днем народження {birthday['congratulation_date']}!")