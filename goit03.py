import re

def normalize_phone(phone_number):
   
    phone_number = re.sub(r'[^0-9+]+', '', phone_number)
 
    if not phone_number.startswith('+'):
        phone_number = '+38' + phone_number
   
    phone_number = re.sub(r'[^0-9+]+', '', phone_number)

    return phone_number


# Приклад використання функції
phone_number = '067 123 45 67'
normalized_phone_number = normalize_phone(phone_number)

print('Нормалізований номер телефону:', normalized_phone_number)