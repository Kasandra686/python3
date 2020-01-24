def new_func(*args):
    result =0
    for el in args:
        if el != "#":
             print(type(el))
             result = result + el
        else:
            print(result)
            return ("#")
    print(result)


srting = ''
print("Программа не работает. я не успела придумать как преобразовать список в число")
print('Для окончания работы программы введите значение "#"')
while srting != "#":
    string = input("Введите данные через пробел: ")
    new_func(string.split())
