#Scientific Calculator
import math as m
def information():
    '''** Python Mini Project****

This project is based on scientific calculator on which you can calculate different  operation:

Mathematical Operation such as (add,subtract,divide,multiply)
Trignometric Operation such as (sin,cos,tan)
Exponential  Operation such as (power,sqaure root,square)
Conversion such as (radian to degree,degree to radian)

'''    


def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def modulus(a,b):
    return a%b
def power(a,b): 
    return a**b
def sqaure_root(a):
    return m.sqrt(a)
def square(a):
    return a*a
def sin(a):
    return m.sin(a)
def cos(a):
    return m.cos(a)
def tan(a):
    return m.tan(a)
def radian_to_degree(a):
    return ((180/m.pi) *a)
def degree_to_radian(a):
    return (a* (m.pi/180))

print('''
1.Addition
2.Substraction
3.Multiplication
4.Division
5.Modulus
6.Power
7.Square Root
8.Square
9.Sin
10.Cos
11.Tan
12.Radian To Degree
13.Degree To Radian''')


option =eval(input('What operation do you want to perform? '))

while option<=13:
    if option == 1:
        print('**Addition Operation**')
        n1 = eval(input("Enter first Number"))
        n2 = eval(input("Enter Second Number"))
        result = addition(n1,n2)
        print("The Addition of {} and {} is {}".format(n1,n2,result))
    elif option == 2:
        print('**Substraction Operation**')
        n1 = eval(input("Enter first Number"))
        n2 = eval(input("Enter Second Number"))
        result = substraction(n1,n2)
        print("The Substraction of {} and {} is {}".format(n1,n2,result))
    elif option == 3:
        print('**Multiplication Operation**')
        n1 = eval(input("Enter first Number"))
        n2 = eval(input("Enter Second Number"))
        result = multiplication(n1,n2)
        print("The Multiplication of {} and {} is {}".format(n1,n2,result))
    elif option == 4:
        print('**Division Operation**')
        n1 = eval(input("Enter first Number"))
        n2 = eval(input("Enter Second Number"))
        result = division(n1,n2)
        print("The Division of {} and {} is {}".format(n1,n2,result))
    elif option == 5:
        print('**Modulus Operation**')
        n1 = eval(input("Enter first Number"))
        n2 = eval(input("Enter Second Number"))
        result = modulus(n1,n2)
        print("The Modulus of {} and {} is {}".format(n1,n2,result))
    elif option == 6:
        print('**Power Operation**')
        n1 = eval(input("Enter first Number"))
        n2 = eval(input("Enter Second Number"))
        result = power(n1,n2)
        print("The Power of {} is {} ithen answer is {}".format(n1,n2,result))
    elif option == 7:
        print('**Square Root Operation**')
        n1 = eval(input("Enter  Number "))
        result = Sqare_root(n1,)
        print("The Square Root of {}  is {}".format(n1,result))
    elif option == 8:
        print('**Square Operation**')
        n1 = eval(input("Enter first Number "))
        result = square(n1)
        print("The Square of {} is {}".format(n1,result))
    elif option == 9:
        print('**Sin Operation**')
        n1 = eval(input("Enter Number "))
        result = sin(n1)
        print("The Sin of {} is {}".format(n1,result))
    elif option == 10:
        print('**Cos Operation**')
        n1 = eval(input("Enter Number "))
        result = cos(n1)
        print("The Cos of {} is {}".format(n1,result))
    elif option == 11:
        print('**Tan Operation**')
        n1 = eval(input("Enter  Number"))
        result = tan(n1)
        print("The Tan of {} is {}".format(n1,result))
    elif option == 12:
        print('**Radian To degree Operation**')
        n1 = eval(input("Enter no. in radian "))
        result = radian_to_degree(n1)
        print("The Degree of {} radian is {}".format(n1,result))
    elif option == 13:
        print('**Degree To Radian Operation**')
        n1 = eval(input("Enter no. in degree "))
        result = tan(n1)
        print("The Radian of {} degree is {}".format(n1,result))
    
    
    else:
        print("Please Choose Correct Operation")

    print()

    new_option=eval(input("Do you want to continue other option operations (YES - 1 or No - 0): "))
    if new_option ==1:
        option =eval(input('What operation do you want to perform? '))
    else:
        print("Thank you for visiting here...........!")
        