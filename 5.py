def new_func(*args):
    result = 0
    for el in args[0]:
        if el != "#":
            result = result + int(el)
        else:
            print(result)
            return ("#")
    print(result)


string = ' '
print('Для окончания работы программы введите значение "#"')
while string != "#":
    string = input("Введите данные через пробел: ")
    string = new_func(string.split())
