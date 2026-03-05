try:
    x = float(input("Введите значение x: "))
except ValueError:
    print("Неккоректное значение x! Введите число!")
    exit()
if x < 2:
    print(-3*x + 9)
else:
    print(x - 7)