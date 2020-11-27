#1.create a function getting two integers from the user
x,y=8,4
def arithmetic(x,y):
    a=x+y #adding of twp numbers
    print("Addition of two numbers is:",a)
    b=x-y #subtracting two numbers
    print("Subtraction of two numbers is:",b)
    c=x/y #dividing two numbers
    print("Division of two numbers is:",c)
    d=x*y #multiplying two numbers
    print("Multiplication of two numbers is:",d)
arithmetic(x,y)
#2.create a function covid() & it should accept patient name & body temperature
patient_name=input("enter patient name:")
def covid(patient_name,body_temperature=98): #default body_temperature
    print("Patient name is ",patient_name,"& body temperature is",body_temperature)
covid(patient_name)