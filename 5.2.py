def new_func(*args):
    result =0
    for el in args:
        if el != "#":

            result=
        else:
            print(result)
            return "#"
    print(result)


srting = ''
list=[]
print('Для окончания работы программы введите значение "#"')
while srting != "#":
    string = input("Введите данные через пробел: ")
    arg=1
    string2 = string
    while (arg>0):
        arg = string2.find(' ')
        print(arg)
        print(string2[:arg])
        if string2[:arg].isdigit():
            list.append(int(string2[:arg]))
        elif(string2[: (arg)]=="#" ):
            list.append("#")
        string2=string2[(arg+1):]
    print(list)
    new_func(list)



