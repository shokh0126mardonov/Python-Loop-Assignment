password = input("parolingiz:")

for i in range(1,4):
    pass_search = input(f"{i}-marta parolni kiritishga urinib ko'ring ")
    if password != pass_search and 1 <= i < 3:
        print("Yana urunib ko'ring 😊")
    elif pass_search == password:
        print(f"siz {i}-martada to'gri topdiz tabriklayman")   
        break
else:
        print("Bloklandiz") 
    