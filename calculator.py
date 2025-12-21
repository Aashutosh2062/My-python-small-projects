x=float(input("enter the 1st  number: "))
y=float(input("enter the  second number: "))
op=input("enter the operator: ")

if(op=="+"):
    print("the sum is: ",x+y)
elif(op=="-"):
    print("the difference is: ",x-y)
elif(op=="*"):
    print("the product is: ",x*y)
elif(op=="/"):
    if(y==0.0):
        print("divisible by 0 can't be performed")
    else:
        print("the quotient is: ",x/y)
