def tinh_tong(n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i
        i = i + 1

    return sum

print(tinh_tong(5))
print(tinh_tong(50))
print(tinh_tong(100))