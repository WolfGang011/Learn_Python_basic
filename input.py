# s = input("Xin nhập chuỗi ký tự bất kỳ : ")
# print ("Chuỗi bạn vừa nhập là : ", s)

# Nhập nhiều số

# Bước 1 : nhập 
# s = input('Nhập 3 số : ')

# Bước 2 : tách các số 
# a = s.split()

# Bước 3 : sử dụng hàm map để chuyển các số từ kiểu chuỗi sang kiểu số nguyên
# x, y, z = map(int, a)
# print(x + y + z)

x, y, z, t = map(int, input('Nhập 4 số : ').split())
print(x + y + z + t)