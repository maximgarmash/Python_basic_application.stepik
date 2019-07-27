def f(x, y):
    try:
        return x / y
    except:
        print("Error :(")

print(f(5, 0))
print(f(5, []))

try:
    15/0 # e
except ArithmeticError: # isinstance(e, ArithmeticError) == True
    print("Arithmetic Error")

except ZeroDivisionError:      # Класс ArithmeticError является предком класса ZeroDivisionError
    print("Division by Zero")  # поэтому PyCharm подсказывает, что данный except исполнен не будет
                               # он лишний

print(ZeroDivisionError.mro())