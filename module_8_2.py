def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        total_sum, incorrect_data = personal_sum(numbers)
        if len(numbers) == incorrect_data:
            return 0
        average = total_sum / (len(numbers) - incorrect_data)
        return average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка, каждый символ считается отдельно
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только числа 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передано одно число, а не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Корректный список чисел