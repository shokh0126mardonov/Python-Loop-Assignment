from random import randint

num = randint(1,20)
print(num)   #sinov uchun

for i in range(1,21):
    num_tax = int(input("num_tax = "))
    if num == num_tax:
        print("topding")
        break