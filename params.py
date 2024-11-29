def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# 1. Вызовы функции с разным количеством аргументов
print_params()  # вызов без аргументов
print_params(b=25)  # передаем только b
print_params(c=[1, 2, 3])  # передаем только c

# 2. Распаковка параметров
values_list = [42, 'Hello', False]
values_dict = {'a': 100, 'b': 'Urban', 'c': [1, 2, 3]}

print_params(*values_list)  # распаковка списка
print_params(**values_dict)  # распаковка словаря

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # передаем распакованный список и дополнительный параметр
