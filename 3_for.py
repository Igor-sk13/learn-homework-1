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

total_sold_of_products = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def main(sales_list):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sold_sum = 0
    for sold in sales_list:
      sold_sum += sold
    return sold_sum
    

all_sold_product = 0
for sold_product in total_sold_of_products:
  sum_product_sold = main(sold_product["items_sold"])
  sold_product_avg = main(sold_product["items_sold"]) / len(sold_product["items_sold"])
  all_sold_product += main(sold_product["items_sold"])
  all_sold_product_avg = all_sold_product / len(sold_product["items_sold"])
  print(f'Cуммарное количество продаж {sold_product["product"]}:{sum_product_sold}')
  print(f'Cреднее количество продаж {sold_product["product"]}: {sold_product_avg}')
print(f'Cуммарное количество продаж всех товаров: {all_sold_product}')
print(f'Cреднее количество продаж всех товаров: {all_sold_product_avg}')
  

    
if __name__ == "__main__":
    main(sold_product["items_sold"])
