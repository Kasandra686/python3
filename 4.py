def my_func1(x, y):
    return (x ** y)


def my_func2(x, y):
    i = 1
    fl = 0
    x2=x
    if y < 0:
        y = y * -1
        fl = 1
    while i < y:
        x2 = x2*x
        i += 1
    if fl == 1:
        x2 = 1 / x2
    return x2


while True:
    num1 = float(input("Введите действительное положительное число: "))
    num2 = int(input("Введите целое отрицательное число: "))
    if ((type(num1)) == float) and ((type(num2)) == int):
        break
    print("Допустим ввод только чисел")
print("Первый способ: "+ str(my_func1(num1, int(num2))))
print("Второй способ с циклами: "+ str(my_func2(num1, int(num2))))
