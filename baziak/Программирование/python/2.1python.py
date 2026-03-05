try:
    x, y = map(float,input("Введите координаты x, y (через пробел): ").split)
except ValueError and TypeError:
    print("Неккоректное значение координаты, введите числа!")
    exit()
if x == 0 and y == 0:
    print("Точка в центре.")
elif x == 0:
    print("Точка на оси X.")
elif y == 0:
    print("Точка на оси Y.")
elif x > 0 and y > 0:
    print("Точка в Первом координатном угле.")
elif x < 0 and y > 0:
    print("Точка в Втором координатном угле.")
elif x < 0 and y < 0:
    print("Точка в Третьем координатном угле.")
elif x > 0 and y < 0:
    print("Точка в Четвертом координатном угле.")