# Create a program that calculates the factorial of a user-inputted number in Python.
#n is the user-inputted number and f is the factorial of the number
n=int(input("enter number to find factorial of : "))
f=1
if n<0:
    print("invalid input")
elif n==0 or n==1:
    print(" the factorial is 1")
    #factorial of 0 and 1 is 1
else:
    for i in range(2,n+1):
        f*=i
    print("the factorial is ", f)
