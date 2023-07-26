# задача Де моргана необязательная:
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# теперь надо проверить ее практически
# в цикле 100 раз прогоняем
# каждый раз генерируем случайное количество предикат от 3 до 15
# и конечно со случайным булевым значением
# и засекаем общее время выполнения программы
# юзаем библиотеки random и time
# предикаты НЕ ЗАДАЕМ как целое число!

import random
import time

def evaluate_expression(predicates):
    result = True
    for predicate in predicates:
        result = result or predicate
    return not result

def test_expression():
    start_time = time.time()
    for _ in range(100):
        num_predicates = random.randint(3, 15)
        predicates = [random.choice([True, False]) for _ in range(num_predicates)]
        evaluate_expression(predicates)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

execution_time = test_expression()
print(f"Общее время выполнения программы: {execution_time} секунд.")