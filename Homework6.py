# Программа запрашивает у пользователя пароль и записывает в переменную password.
# # Необходимо посчитать сложность пароля, где за каждую пройденную проверку пароль получает +1
# балл к итоговой оценке, максимальное количество баллов - 5
# # Проверки:
# # Длина пароля больше или равно 8 символам
# В пароле есть хотя бы одна цифра
# В пароле есть хотя бы одна большая
# В пароле есть хотя бы одна маленькая буква
# В пароле есть хотя бы один спец символ (+, -, /, _, % и т.д. P.S. их на самом деле больше)
# После всех проверок нужно вывести пользователю число - количество баллов за пароль, а так-же
# рекомендации по улучшению пароля.



password = input("Введите пароль: ")
a = int()
b = int()
c = int()
d = int()
k = int()
if len(password) >= 8:
    a = 1
for char in password:
    if char.isdigit():
        b = 1
for char in password:
    if char.isupper():
        c = 1
for char in password:
    if char.islower():
        d = 1
for char in password:
    if not char.isalnum():
        k = 1
for char in password:
    print("Password score:", a+b+c+d+k)
    break
if a+b+c+d+k < 5:
    print("Recommendations:")
if a == 0:
    print('Use minimum password length is 8')
if b == 0:
    print('Use at least one digit')
if c == 0:
    print("Use at least one capital letter")
if d == 0:
    print("use at least one small letter")
if k == 0:
    print('Use at least one special character')
