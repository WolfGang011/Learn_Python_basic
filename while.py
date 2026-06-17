# n = 1
# while n <= 5: 
#     print(n)
#     n = n + 1
#     if n == 3:
#         break

# while True: 
#     n = int(input("Nhập số: "))
#     if n > 0:
#         break

# đếm số lượng chữ số 

n = 1234
dem = 0
while n != 0:
    dem = dem + 1
    n = n // 10
print("Số lượng chữ số là:", dem)