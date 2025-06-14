unli = 'aeiou'
text = input().lower()
count = 0
for i in text:
    if i in unli:
        count+=1
if count > 0:       
 print(f"Unlilar soni {count} ta")
else:
    print("Unlilar mavjud emas")
