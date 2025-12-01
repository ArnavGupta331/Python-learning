num1=int(input("Enter num 1 "))
num2=int(input("Enter num 2 "))
sum=num1+num2
print(sum)
# Now starting with loops
#normal arthimetic 
a= 10
b= 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a ** b)
#comparision operator
print(5 > 3)  # True
print(5 < 3)  # False
#if else
#Input 3 numbers → print largest
num1=int(input("Enter thr number"))
num2=int(input("Enter thr number"))
num3=int(input("Enter thr number"))
if num1>num2:
    print(num1)
elif num2>num3:
    print(num2)
elif num3>num1:
    print(num3)
else:
    print("All numbers are equal")
