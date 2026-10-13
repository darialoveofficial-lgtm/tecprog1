def divide(a, b):
    if b == 0:
        return "Ошибка: на ноль делить нельзя"
    return a / b

x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))

print("Результат:", divide(x, y))
