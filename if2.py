"""Домашнее задание №1
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

def string_compare(str1, str2):
    if(isinstance(str1,str) and isinstance(str2,str)):
        if str1 == str2:
            print(1)
        else:
            if len(str1) > len(str2):
                print(2)
            if str2 == "learn":
                print(3)            
    else:     
        print(0)

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    string_compare(23, "erwer")
    string_compare("fsdfsdf", 56)
    string_compare("fsdfsdf", "rter")
    string_compare("f", "rter")
    string_compare("erwer", "erwer")
    string_compare("erwer", "learn")
    
if __name__ == "__main__":
    main()