'''
for index in range(1,10+1): # (від, до, крок)
    print(index)
    '''

'''
for index in range(10,1-1,-1): # спадання
    print(index)
    '''

'''
for i in range(1, 5+1, +2): # range( from, to, step):
  print(i)
print("вийшов зайчик погулять")

for i in range(5, -5-1, -2): # range( from, to, step):
  print(i)
print("вийшов зайчик погулять")
'''

#цикл з перевіркою на спадання або зростання
number1 = int(input("number1 "))
number2 = int(input("number2 "))
if number1 > number2:
    for index in range(number1,number2-1,-1):
        print(index)
else:
    for index in range(number1,number2+1,+1):
        print(index)