for i in range(1,6):
   son = int(input(f'{i}-elementga qiymat kiriting = '))
   if  i == 1:
       max = son
   elif max < son:
       max = son
print(max)