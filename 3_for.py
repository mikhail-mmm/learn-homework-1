"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

list_1 = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def main():
    answer_1 = []
    answer_2 = []
    sum_solded_phones = 0
    amount_phones = 0
    for phone in list_1:
        answer_1.append(f'Суммарное количество продаж для {phone["product"]} = {counter_solded_phone(phone["items_sold"])}')
        answer_2.append(f'Среднее количество продаж для {phone["product"]} = {avg_solded_phone(phone["items_sold"])}')
        sum_solded_phones += counter_solded_phones(phone["items_sold"])
        amount_phones += len(phone["items_sold"])
    avg_solded_phones = round(sum_solded_phones / amount_phones, 2)
    print('\n'.join(answer_1))
    print('\n'.join(answer_2))
    print(f'Суммарное количество продаж всех товаров = {sum_solded_phones}')
    print(f'Среднее количество продаж всех товаров = {avg_solded_phones}')



def counter_solded_phone(phones):
    phone_sum = 0
    for el in phones:
        phone_sum += el
    return phone_sum

def avg_solded_phone(phones):
    phone_sum = 0
    for el in phones:
        phone_sum += el
    mean = phone_sum / len(phones)
    return round(mean, 2)

def counter_solded_phones(phones):
    phones_sum = 0
    for el in phones:
        phones_sum += el
    mean = phones_sum / len(phones)
    return round(mean, 2)




    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass
    
if __name__ == "__main__":
    main()
