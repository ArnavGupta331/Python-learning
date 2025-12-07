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


# frinting only even numbers
for i in range(0,51):
    if(i%2==0):
        print(i)


#printing the table of 10
for i in range (0,11):
    print(10,'x',i,'=',10*i)


#for printing number in reverse
for i in range(10,0,-1):
    print(i)


#defining a function
def add(x,y):
    return x+y
result=add(10,1)
print(result)


#giving multiple results
def calc(x,y):
    return x+y,x*y
add,mul=calc(10,5)
print(add,mul)


#learning about lists
name = ["Arnav", "Chiranjeev", "Ayush"]
print(name[1])
print(name[-1])
print(name[0])

#changing the value
name[1]="Arihant"
print(name[1])

#adding the element
#At the end
name.append("Gaurav")
#at the specific point
name.insert(1,"Rushil")

#loops in the list
for i in name:
    print(i)
print(len(name))


#Count how many even numbers are in the list
num=[1,2,3,4,5,6,7,8,9,10]
print(len(num))
for i in num:
    if i % 2==0:
        print(i,"is even")
    else:
        print(i,"not even")


#reversing the function without using reverse function
num=[1,2,3,4,5,6,7,8,9,10]
print(len(num))
for i in num[::-1]:
    print(i)


