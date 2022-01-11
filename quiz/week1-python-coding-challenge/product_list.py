def sum_of_cube(n):
    result = 0
    for i in range(1, n):
        result += i*i*i
    return result


print(sum_of_cube(8))
