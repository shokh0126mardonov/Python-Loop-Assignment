from random import randint

num = randint(1000,9999)
print(num)

while True:
    num_tax = int(input("num_tax = "))
    
    if num < num_tax:
        print("Juda katta son!")
    elif num > num_tax:
        print("Juda kichik son")
    elif num == num_tax:
        print("Tabriklaymiz,topdingiz!")    
        break
    