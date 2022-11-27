"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    user_line_1 = input('Введите первую строку: ')
    user_line_2 = input('Введите вторую строку: ')
    print(line_verification(user_line_1, user_line_2))

def line_verification(line_1, line_2):
    if not(isinstance(line_1, str)) or not(isinstance(line_2, str)):
        return 0
    elif line_1 == line_2:
        return 1
    elif len(line_1) > len(line_2):
        return 2
    elif line_2 == 'learn':
        return 3

if __name__ == "__main__":
    main()
