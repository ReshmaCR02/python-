#1.create a lambda function that multiplies argument x with argument y
a=lambda x,y : x*y
print(a(2,4))
#2.create fibonacci series to n using lambda
from functools import reduce
a=int(input("enter a value:"))
f_series=lambda a: reduce(lambda x,_: x+[x[-1] + x[-2]],range(a - 2),[0, 1])
print(f_series(a))
#3.multiply each number of given list with a given number
num=[2,4,6,8]
print(num)
a=int(input("enter a value:"))
filtered_numbers=list(map(lambda number:number*a,num))
print(' '.join(map(str,filtered_numbers)))
#4.find numbers divisible by 9 from a list of numbers
my_list=[2,4,6,8,12,13,16]
result=list(filter(lambda x: (x % 4 == 0),my_list))
print("Numbers divisible by 4:",result)
#5.count even numbers in a given list of integers
my_list=[20,31,45,68,88,99]
even_num=len(list(filter(lambda x: (x%2 == 0),my_list)))
print("number of even numbers in my_list:",even_num)