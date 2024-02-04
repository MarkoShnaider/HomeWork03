import random

def get_numbers_ticket(min, max, quantity):
    
    if min < 1 or max > 1000 or quantity < 1 or quantity > max - min + 1:
        print('Неправильні вхідні дані!')
        return []

    
    numbers = set()
    while len(numbers) < quantity:
        number = random.randint(min, max)
        numbers.add(number)

    
    numbers = sorted(numbers)

    
    return numbers


# Приклад використання функції
min = 1
max = 49
quantity = 6
numbers_ticket = get_numbers_ticket(min, max, quantity)

print('Випадковий набір чисел для лотерейного квитка:', numbers_ticket)