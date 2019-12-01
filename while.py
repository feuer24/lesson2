

def ask_user():
    diction = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Как сам?": "Нормально"}     
    while True:
        quest = input()
        if quest == "ок":
            break        
        print(diction[quest])

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    ask_user()

if __name__ == "__main__":
    main()