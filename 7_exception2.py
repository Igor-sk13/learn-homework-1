"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)  

if __name__ == "__main__":
    try:
      print(discounted(float(100), float(2)))
      print(discounted(float(100), float("3")))
      print(discounted(int("100"), int("4.5")))
      print(discounted("five", 5))
      print(discounted("сто", "десять"))
      print(discounted(100.0, 5, "10"))
    except(ValueError, TypeError):
      print("Не подходящее значение переменной")