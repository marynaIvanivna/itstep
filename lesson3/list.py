list = ["This is text in list"]
print(list)

list.append("new1")
list.insert(1, "new2")
list.insert(2, 12)
list.append(False)
print(list)

list.reverse()
print(list)

x = list[4]
print(x)

list.pop()
print(list)

list.pop(0)
print(list)

list.remove(12)
print(list)

list.insert(0, x)
print(list)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)

list3 = list1+list2
list3.insert(1, 7)
list3.append(0)
print(list3)

list3.sort()
print(list3)

minimum = min(list3)
maximum = max(list3)
suma = sum(list3)
number = len(list3)
print(minimum, maximum, suma, number)

medium = suma/number
print("mediana ", medium)
print(list3.count(5))
'''
import random
list = []
number = int(input("enter number of list "))
for i in range(number):
  n1 = random.randint(-10, 10)
  list.append(n1)
print(list)

for i in range(number):
  if list[i] % 2 == 0: # парні числа
    print(list[i])
'''

'''
list_1 = [1,1]
list_2 = [2,2]
tuple_1 = 3,3
tuple_2 = 4,4
print(list_1 + list_2)
print(tuple_1 + tuple_2)
print(list_1 * 2)
print(tuple_1 * 2)

str1 = "Ї"
str2 = "ї"
print(str1 > str2)
print(ord(str1))
print(ord(str2))
print(chr(666))
print(chr(123))
'''

import random
user_hero=[]
super_hero = ["spider-man", "super-man", "iron-man","batman","aquaman", "hulk", "captan_america", "doctor_strenge", "black_panther", "tor", "houmlender", "black-nuar"]
print("вітаю в грі в якій ви станете супергероєм")
print("введіть своє ім'я та імена своїх друзів для завершення напешіть stop")
name =input()
while name != "stop":
    if len(super_hero) > 0:
        hero = random.choice(super_hero)
        super_hero.remove(hero)
        user_hero.append(name)
        user_hero.append(hero)
        print(f"{name},ваш супергерой - {hero}!")
        print("введіть своє ім'я та імена своїх друзів для завершення напешіть stop")
        name = input()
    else:
        print("на жаль, всі супергерої вже розподілені,спробуйте пізніше")
        name = input()
print("гра закінчена, ось список гравнців та їх супергероїв")
print("ім'я користувача  cупергерой")
for i in range(0,len(user_hero), +2):
    print(user_hero[i], user_hero[i+1])