'''
mark = int(input("Enter your mark "))
if mark == 12:
    print("Perfect!")
if mark < 1 or mark > 12:
    print("Error!")
'''

'''
# оператор break, while зупиняє
a = 1
while a < 10:
  print("Число " + str(a))
  if a == 5:
    break
  a = a + 1
print("Цикл while закінчено!")

# оператор continue, while пропускає 1 ітерацію
a = 0
while a < 10:
  a = a + 1
  if a == 5:
    continue
  print("Число " + str(a))
print("Цикл while закінчено!")'''

#сиулятор світлофора
import random
color = ["green", "yellow", "red"]
light = random.choice(color)
print(light)
if light == "green":
    print("You can go!")
else:
    print("Wait!")