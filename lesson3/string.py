text = "Hello world!"
print(text, "- Довжина рядка -", len(text))
print(text[0])
print(text[7])
print(text[0:7])
print(text[1:])

l1 = text.find("l")
print(l1)
l2 = text.rfind("l")
print(l2)
text2 = text[l1:l2+1]
print(text2)


string = " Hello World!"
string_2 = "- Hello to You!"
string_sum = string + string_2
big_str = string_sum*3
print("string_sum - ", string_sum)
print("big_str -", big_str)

string_list = text.split()
print(string_list)

string_list = text.split("w")
print(string_list)

string_1 = "I am a String and I want to be printed"
print("lower -", string_1.lower())
print("upper -", string_1.upper())
print("title -", string_1.title())
print("capitalize -", string_1.capitalize())
print("swapcase -", string_1.swapcase())

string_1 = "I am a String and I want to be printed"
print(string_1.startswith('I am'))
print(string_1.endswith("printed."))


'''
#text = "In the hole in the ground thera lived a hobbit."
#Вирізати текст з першої по останню літеру h включко  - а все решта - вивести на екран, використовуючи функції вивчені на уроці.

text = "In the hole in the ground there lived a hobbit."
h1 = text.find("h")
h2 = text.rfind("h")
text2 = text[0:h1] + text[h2+1:]
print(text2)
'''

'''
#відгадати 5 загадок
q1 = 'I have 4 legs and a tail. I am very smart.I like to play with you. When I see a cat, I say "Woof, woof" I am… '
q2 = 'I am a pet. I am soft and furry. I like to sleep and drink milk. I do not like mice and dogs. I say "Meow, meow". I am… '
q3 = 'I am a big farm animal. I can be black, white or brown. I like to eat green grass. I give milk. I can say "Moo, moo". I am… '
q4 = 'I have four legs and a tail. I have no teeth. I can swim and dive underwater. I carry my house around with me. I am a… '
q5 = 'I live in the woods. I am very big and furry. I have a big nose,a little tail and four legs. I like to eat fish and berries. I am a… '
answer_1 = "dog"
answer_2 = "cat"
answer_3 = "cow"
answer_4 = "turtle"
answer_5 = "bear"
result = 0

print(q1)
user_answer = input("Enter answer ")
if user_answer.lower() == answer_1:
    result += 1
    print("True")
else:
    result -= 1
    print("False")

print(q2)
user_answer = input("Enter answer ")
if user_answer.lower() == answer_2:
    result += 1
    print("True")
else:
    result -= 1
    print("False")

print(q3)
user_answer = input("Enter answer ")
if user_answer.lower() == answer_3:
    result += 1
    print("True")
else:
    result -= 1
    print("False")

print(q4)
user_answer = input("Enter answer ")
if user_answer.lower() == answer_4:
    result += 1
    print("True")

else:
    result -= 1
    print("False")

print(q5)
user_answer = input("Enter answer ")
if user_answer.lower() == answer_5:
    result += 1
    print("True")
else:
    result -= 1
    print("False")

print("The end of game, you have ", result, "points!")
'''