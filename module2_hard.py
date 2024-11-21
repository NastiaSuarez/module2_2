a = int(input("Введите число: "))
if not (3 <= a <= 20):
        print("Значение a должно быть в диапазоне от 3 до 20")
else:
    def find_pairs(a):
        pairs = []
        for x in range(1, a):
            for k in range(1, a // x + 1):
                y = a - x * k
                if y >= x and a % (x + y) == 0:
                    pairs.append((x, y))
        return pairs
result = find_pairs(a)
if result:
    print("Найденные пары:")
    for pair in result:
             print(pair)
else:
    print("Пар не найдено.")


