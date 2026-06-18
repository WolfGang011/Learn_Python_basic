def tim_so_lon_nhat (a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
large = tim_so_lon_nhat(5, 10, 15)
print("Số lớn nhất là :", large)