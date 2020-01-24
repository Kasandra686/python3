def new_function(data):
    print(
        f"{data[1]} {data[0]}, {data[2]} года рождения, проживает в городе {data[3]}. Контактные данные : {data[4]} , "
        f"тел. {data[5]}")


data = input("Введите данные через пробел  имя, фамилия, год рождения, город проживания, email, телефон: ").split()
while len(data) < 6:
    data.append(" ")
new_function(data)
