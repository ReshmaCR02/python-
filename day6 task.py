#1.loop through a list of numbers & add +2 to every value to elemants in list
old_list=[1,2,3,4,5]
print("old list is:",old_list)
new_list=[]
for i in range(0,len(old_list)):
    new_list.append(old_list[i] + 2)
print("New list is:"+str(new_list))
#2.
rows=4
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()
#3.Fibonacci sequence
x=int(input("enter x value: "))
a=0
b=1
sum=0
count=1
print("Fibonacci Series: ", end = " ")
while(count <= x):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b
#4.Armstrong number
num=int(input("\nenter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
#5.Multiplication tables of 9
num = 9
for i in range(1, 13):
    print(num, 'x', i, '=', num*i)
#6.positive or negative
a=int(input("enter a value:"))
if(a>0):
    print("positive number")
else:
    print("negative number")
#7.convert number of days to ages
days=int(input("enter days:"))
years=(days/365)
print("number of years:",years)
#8.trigonometry problem using math function
import math
a=math.sin(math.pi/6)
print("sin(n/3)=",a)
#9.calculator using if condition
choice = input("""select the type of operation you want to perform:+,-,* or / = """)
a=int(input("enter a value:"))
b=int(input("enter b value:"))
if choice == "+":
    print("(a) + (b) = ".format(a,b))
    print(a+b)
elif choice == "-":
    print("(a) - (b) = ".format(a,b))
    print(a-b)
elif choice == "*":
    print("(a) * (b) = ".format(a,b))
    print(a*b)
elif choice == "/":
    print("(a) / (b) = ".format(a,b))
    print(a/b)
else:
    print("enter a valid operator, please run the program again")



