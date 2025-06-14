num = int(input("num = "))   #95
n = 0
while num!=0:
   n += num % 10  # 5 qiymatga o'zgardi
   num = num//10  # 9 qiymat bo'ladi
print(n)