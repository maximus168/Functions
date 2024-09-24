def get_matrix(n, m, value):
    matrix = []
    for k in range(n):
        row = []
        for l in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

result1 = get_matrix(4, 3, 7)
result2 = get_matrix(3, 2, 31)
result3 = get_matrix(3, 3, 9)
print(result1)
print(result2)
print(result3)