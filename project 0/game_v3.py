"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def my_predict(number: int = 1) -> int:
    """ Угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = np.random.randint(1, 101)  # предполагаемое число
    # ограничиваем поиск числа мин и макс числами
    min_num = 1
    max_num = 100

    while True:
        count += 1
        number = (min_num+max_num)//2

        if number == predict_number:
            break  # выход из цикла если угадали
        elif predict_number < number :
            max_num = number - 1 # верхний предел для поиска числа
           
        elif number < predict_number:
            min_num = number + 1 # нижний предел для поиска числа
            
    return count


def score_game(my_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        my_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(my_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

# RUN
if __name__ == "__main__":
    score_game(my_predict)

    
