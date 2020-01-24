def new_func(*args):
    result =0
    print(args)
    for el in args:
        if el != "#":
             print(type(el))
             result = result + int(el)
        else:
            print(result)
            return ("#")
    print(result)


srting = ''
print("Программа не работает(")
print('Для окончания работы программы введите значение "#"')
while srting != "#":
    string = input("Введите данные через пробел: ")

    for el in string.split()
    new_func(el)
