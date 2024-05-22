def generate_password(n):
    password = ""
    for i in range(1, n):
        for j in range(i+1, n):
            if (i + j) % n == 0:
                password += str(i) + str(j)
    return password

number = int(input("Введите число от 3 до 20: "))
if number < 3 or number > 20:
    print("Число должно быть от 3 до 20")
else:
    password = generate_password(number)
    print("Пароль для числа", number, ":", password)
