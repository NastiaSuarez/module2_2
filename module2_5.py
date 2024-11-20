def get_matrix(m, n, value):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(value)
        matrix.append(row)
    return matrix

result1 = get_matrix(2, 8, 7)
result2 = get_matrix(5, 1, 9)
result3 = get_matrix(3, 2, 12)

print(result1)
print(result2)
print(result3)

