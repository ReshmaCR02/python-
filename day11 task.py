#1.Using zip() function and list() function,create a merged list of tuples from two lists given
name=["gill","mavi","hardik"]
num=[77,23,33]
my_list=list(zip(name,num))
print(my_list)
#2.First create a range from 1 to 8.
# Then using zip, merge the given list and the range together to create a new list of tuples
month=["jan","feb","mar","apr","may","jun","jul","aug"]
my_list=list(zip(month,range(1,9)))
print(my_list)
#3.Using sorted function,sort the list in ascending order
x= ("b","g","a","d","f","c","h","e")
y= sorted(x)
print(y)
#4.Using filter function,filter the even numbers so that only odd numbers are passed to the new list
