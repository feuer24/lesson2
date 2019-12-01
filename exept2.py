def discounted(price, discount):
    try:    
        price = price
        discount = discount
        if discount >= 100:
            price_witn_discount = price
        else:
            price_witn_discount = price - price*discount/100
        return price_witn_discount
 
    except TypeError:
        print("Неверный тип")
        #break
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    price = input()
    discount = input()
    print(discounted(price, discount))

if __name__ == "__main__":
    main()

