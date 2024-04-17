def caching_fibonacci():
    # Створення порожнього словника для кешування результатів
    cache = {}
    
    # Внутрішня функція fibonacci замкнута у caching_fibonacci
    def fibonacci(n):
        # Перевірка базових випадків
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Перевірка наявності результату в кеші
        if n in cache:
            return cache[n]
        
        # Обчислення числа Фібоначчі і збереження у кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        return cache[n]
    
    # Повернення внутрішньої функції fibonacci
    return fibonacci

# Приклад використання
fib = caching_fibonacci()

# Виведення результатів
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
