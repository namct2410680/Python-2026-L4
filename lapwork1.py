import math
r=int(input("Enter circle radius?"))
pi=3.14
circle_area= pi*r**2
print("Circle Area:",circle_area)

temp_c = int(input("Enter the temperature in Celsius?" ))
temp_f = 5*temp_c
print(temp_c,"(C) =",temp_f,"(F)")

a = int(input("Enter a number"))
if a < 2:
    print(a,"is not a prime number")
else:
    is_prime= True
    for i in range(2,(math.isqrt(a))+1):
        if a % i == 0:
            is_prime = False
            break
    if is_prime:
        print(a,"is a prime number")
    else:
        print(a,"is not a prime number")

a = int(input("Enter the number"))
if a <=1:
    print(a,"is not a perfect number")
else:
    sum=1
    for i in range(2,(math.isqrt(a))+1):
        if a % i == 0:
            sum+=i
            if i != a//i:
                sum+=i
    if sum == a:
        print(a,"is a perfect number")
    if sum != a:
        print(a,"is not a perfect number")

list_color=["blue","red","yellow"]
a = str(input("What is your favorite color?"))
if a not in list_color:
    print("Sorry, I could not find your color")
else:
    for i in range(0,3):
        if a in list_color[i]:
            print(f"Your colod is at index {i+1} in my list")

range1 = range(0,7)
print([x for x in range1])
range2 = range(1,11,3)
print([x for x in range2])
range3 = range(5,0,-1)
print([x for x in range3])
range4 = range(6,-3,-2)
print([x for x in range4])

def remove_dollar_sign(s):
    return s.replace("$","")
money = input("Enter your money have $ sign ")
print("Your money dont have $ sign",remove_dollar_sign(money))

def extract_even():
    number=[]
    number_even=[]
    n= int(input("Enter number of number:"))
    for i in range(n):
        num=int(input(f"Enter the{i+1}th number:"))
        number.append(num)
    for i in range(0,n):
        if number[i]%2 == 0:
            number_even.append(number[i])
    print("Even number in your list are",number_even)
extract_even()

def factorial():
    a=int(input("Enter the number: "))
    factorial=1
    if a < 0:
        print("The number must be positive")
    else:
        for i in range(1,a+1):
            factorial *=i
    print(f"The factorial for number {a} is {factorial}")
factorial()

def division_of_number():
    a = int(input("Enter the number: "))
    division=[]
    for i in range(1,a+1):
        if a%i == 0:
            division.append(i)
    print(f"The division of number {a} are {division}")
division_of_number()

x1=float(input("Enter coordinate of point A, x1= "))
y1=float(input("Enter coordinate of point A, y1= "))
x2=float(input("Enter coordinate of point A, x2= "))
y2=float(input("Enter coordinate of point A, y2= "))
distance=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("The distance of point A to B is",distance)

def rectangle(m,n):
    for i in range(m):
        for j in range(n):
            if  i==0 or i==m-1 or j==0 or j==n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
rectangle(4,5)
