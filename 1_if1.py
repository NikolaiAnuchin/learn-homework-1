"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
def user_age():
  print('Please, input your age:\t')
  user_age = int(input())
  if type(user_age) == type(1):
    return(int(user_age))

def user_work(age):
  if 0 < age < 6:
    print('I am a kid, I must go to the kindegarten, I dont know nothing about Python!' )
  elif  7 <= age < 18:
    print('I am a teenager, I must go to the school, I dont know nothing about Python!' )
  elif  18 <= age < 23:
    print('I am a student, I must go to the university, I  know everything about Python!' )
  else:
     print('I am an adult, I must go to work, I want to die.' )

def main():
  user_work(user_age())
    
  """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
  """
  return()

if __name__ == "__main__":
    main()
