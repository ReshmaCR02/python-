#2.calculator
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
choice = input("Enter +,-,* or /: ")
a=int(input("enter a value:"))
b=int(input("enter b value:"))
try:
     if choice == '+':
            print(a, "+", b, "=", add(a,b))
     elif choice == '-':
            print(a, "-",b, "=", subtract(a,b))
     elif choice == '*':
            print(a, "*",b, "=", multiply(a,b))
     elif choice == '/':
            print(a, "/",b, "=", divide(a,b))
     else:
            print("Invalid Input")
except exception as ex:
    print("error:()".format(str(ex)))
#3.
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something went wrong,please check again")
#4.
#5.
a=1
try:
    a=int(input("age:"))
    print(a)
except:
    print("error")