
def f(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e: # Использование кортежа и вызов конструктора класса для
                                                # экземпляра е класса error
        print("Error :(")
        print(type(e)) # тип экземпляра
        print(e)       # значение экземпляр
        print(e.args)  # аргументы экземпляра
    # Введение дополнительного отдельного except для проверки деления на ноль
    #except ZeroDivisionError:
    #    print("Zero division :(")

# Можно добавить конструкцию try except в основное тело <module>
#try:
#    print(f(5, 0))
#except ZeroDivisionError:
#    print("Zero division :(")

print(f(5, 0))
print(f(5, []))