name=input("enter your choice: ")
import random
num1 = random.randint(0,2)
#0=rock
#1=paper
#2=scissor
print(num1)

def greet(name):
    if((name=="rock" and num1==0) or (name=="paper" and num1==1) or (name=="scissor" and num1==2)):
        print("its a draw")
    elif((name=="rock" and num1==2) or (name=="paper" and num1==0) or (name=="scissor" and num1==1)):
        print("you won")
    else:
        print("you lost")
    

    
    

greet(name)
