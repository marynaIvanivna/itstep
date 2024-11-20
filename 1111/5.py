'''try:
    print("start code")
    print(10 / 0)
    print("No errors")
except NameError:
    print("We have an NameError")
except ZeroDivisionError:
    print("We have an ZeroDivisionError")

print("code after capsule")'''

'''try:
    print("start code")
    print(10 / 0)
    print("No errors")
except (NameError,ZeroDivisionError) as error:
    print("We have", error )


print("code after capsule")'''

'''try:
    print("Hello")
    print(error)
    print("No error")
except NameError as error:
    print(error)
else:
    print("No problems")
finally:
    print("Finally code")'''



try:
    x1 = int(input("number1"))
    x2 = int(input("number2"))
    print(x1+x2)
    print(x1-x2)
    print(x1/x2)
    print(x1*x2)
except ZeroDivisionError:
    print("Помилка: Ділення на нуль неможливе.")
except ValueError:
    print("Помилка: Введені дані не є числом.")