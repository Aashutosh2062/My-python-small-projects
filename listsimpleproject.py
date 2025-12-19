list=[]
while True:
    print("enter your choice: add for adding an item,remove for removing an item,show for showing the list,exit for exiting the program")
    x=input("enter your choice: ")
    if(x=="add"):
        y=input("enter the element you wish to add in the list: ").split()
        list.extend(y)
    elif(x=="remove"):

        y = input("enter the element you wish to remove in the list : ").split()
        for item in y:
            if item in list:
                list.remove(item)
            else:
                print(item, "not found")

    elif(x=="show"):
        print(list)
    elif(x=="exit"):
        break