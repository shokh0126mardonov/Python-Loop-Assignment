text = input("matnni kiriting:")
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
cout = 0

for i in text:
    if i in upper:
        cout+=1
if cout > 0:
    print(f"katta harflar{cout} ta")        

elif cout == 0 :
    print("Katta harf mavjud emas")