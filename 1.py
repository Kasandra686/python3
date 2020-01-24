def new_function(num1, num2):
    return (num1 / num2)


num2 = 0
while num2 == 0:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число не равное нулю: "))
    if num2 == 0:
        print("Нельзя делить на ноль!")

print(new_function(num1, num2))
