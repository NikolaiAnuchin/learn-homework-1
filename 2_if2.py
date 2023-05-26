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

#Функция, получается на вход строго две строки
def input_lines(*args):
    lines = []
    for argument in args:
        if isinstance(argument, str):
          lines.append(argument)
        else: 
            return(0)
    if lines[0] == lines[1]:
        return(1)
    elif len(lines[0]) > len(lines[1]):
        return(2)
    elif lines[1] == "learn":
        return(3)

def main():
    print('Test 1: second arg is not in a str format\n', 
          input_lines('111',3, '2223'))
    
    print('\nTest 2: second arg is smaller than first\n', 
          input_lines('koshka', 'kot'))
    
    print('\nTest 3: second arg is bigger than first\n', 
          input_lines('spam', 'bacon'))
  
    print('\nTest 4: lines are not equal and second line is "learn" \n', 
          input_lines('spam', 'learn'))    
    
    print('\nTest 5: both lines are "learn" \n', 
          input_lines('learn', 'learn'))
    
    print('\nTest 6: both lines are "learn", but in different cases \n', 
          input_lines('LEARN', 'learn'))

    print('\nTest 7: both lines are "learn", but in different cases \n', 
          input_lines('learn', 'LEARN'))
    
    

    
if __name__ == "__main__":
    main()
