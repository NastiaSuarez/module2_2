a = int(input("Введите число: "))

def find_pairs(a):
    pairs = set()
    for x in range(1, a):
        for y in range(x+1, a):

            if a % (x + y) == 0:
                pairs.add((x, y))
    return pairs
if not (3 <= a <= 20):
        print("Значение a должно быть в диапазоне от 3 до 20")
else:
    find_pairs(a)

result = find_pairs(a)
if result:
    print("Найденные пары:")
    for pair in result:
             print(pair)
else:
    print("Пар не найдено.")

