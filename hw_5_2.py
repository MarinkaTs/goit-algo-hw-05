import re
from typing import Callable

def generator_numbers(text: str):
    # Регулярний вираз для пошуку дійсних чисел
    pattern = r'\b\d+\.\d+\b'
    
    # Пошук чисел у тексті за допомогою регулярного виразу
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    # Виклик генератора для отримання чисел
    numbers = func(text)
    
    # Підсумовування чисел
    total = sum(numbers)
    
    return total

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
