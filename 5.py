def new_func(*args):
    result = 0
    for el in args[0]:
        if el != "#":
            result = result + int(el)
        else:
            print(result + args[1])
            return ("#")
    return (result)


string = ' '
string2 = 0
print('Для окончания работы программы введите значение "#"')
while string != "#":
    string = input("Введите данные через пробел: ")
    if (new_func(string.split(), string2)) != "#":
        string2 = string2 + new_func(string.split(), string2)
        print(string2)
    else:
        break
