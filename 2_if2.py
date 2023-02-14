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

def main(string_1, string_2):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if (type(string_1 and string_2) != str):
      return 0
    
    if string_1 == string_2:
      return 1
    
    elif string_1 != string_2 and len(string_1) > len(string_2):
      return 2
    
    elif string_1 != string_2 and string_2 == 'learn':
      return 3
    
print(main(4, 13))
print(main('python', 'python'))
print(main('python', 'easy'))
print(main('python', 'learn'))
    
if __name__ == "__main__":
    main('string_1', 'string_2')
