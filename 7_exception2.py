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
    try:
        price = abs(float(price))
    except(ValueError):
        raise ValueError('Insert correct price!')
    except(TypeError):
        raise TypeError('Insert  price in correct formaT!')
    try:
        discount = abs(float(discount))
    except(ValueError):
        raise ValueError('Insert correct discount!')
    except(TypeError):
        raise TypeError('Insert  discount in correct formaT!')
    try:
        max_discount = abs(float(max_discount))
    except(ValueError):
        raise ValueError('Insert correct max_discount!')
    except(TypeError):
        raise TypeError('Insert  max_discount in correct formaT!')    
    if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)
    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
