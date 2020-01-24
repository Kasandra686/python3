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
list=[]
print('Для окончания работы программы введите значение "#"')
while srting != "#":
    string = input("Введите данные через пробел: ")
    ind=1
    while (ind>0)
    ind=string.find(' ')
    if string[:ind+1].isdigit()
        list.append(int(string[:ind+1]))

    new_func(string.split())