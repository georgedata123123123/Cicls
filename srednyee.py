# Выполнил: Мальцев Георгий Павлович

import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')


def srednyee():
    i = 0
    x = 0
    t = 1
    while t != 0:
        try:
            t = int(input('Write here: '))
            logging.info("Верный тип данных - число")
        except TypeError:
            print("Вы ввели непраильно!, используйте  целые числа по одному!")
            logging.info("Кто-то ввел неправильный тип данных!")
            raise TypeError
        else:
            i += 1
            x += t
    print(f"Ответ: {x / i}")  # Если необходимо учитывать ноль, то оставляем так , нет вычитаем единицу из i
    logging.info("Успех!")

srednyee()
#capsys