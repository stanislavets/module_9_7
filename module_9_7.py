def sum_three(x, y, z):
    """Сумма трех чисел."""
    return x + y + z

def is_prime(func):
    """Декоратор для проверки, является ли результат функции простым числом."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, result):
                if (result % i) == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return result
    return wrapper

@is_prime
def sum_three_decorated(x, y, z):
    """Сумма трех чисел с использованием декоратора."""
    return x + y + z

# Пример использования
result = sum_three(2, 3, 6)
print(result)  # Простое

result = sum_three_decorated(2, 3, 6)
print(result)  # Простое

# Пример составного числа
result = sum_three(2, 3, 10)
print(result)  # Составное

result = sum_three_decorated(2, 3, 10)
print(result)  # Составное