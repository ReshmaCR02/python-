#1
num=int(input("enter n value:"))
a=[]
for i in range(1,num):
    a.append(i)
print(a)
a.insert(3,6) #add an item to list
print(a)
a.remove(4) #delete an item in the list
print(a)
b=max(a) #largest value
print(b)
c=min(a) #smallest value
print(c)
#2
my_tuple=(1,2,3,4,5)
new_tuple=tuple(reversed(my_tuple)) #reverse of tuple
print(new_tuple)
#3
my_tuple=(3,4,5)
my_list=list(my_tuple) #convert tuple into list
print(my_list)