print("Type 'push' to push something to the stack and pop to pop out of it. \n example 'push a' \n To exit the program type exit. \n everything will be in lowercase")

x = " "
stack = []

while x != exit:

    x = input("->")
    x = x.lower()

    #push operation
    if x[0:4]=="push":
        stack.append(x[5:])
        print(stack)
    
    #empty stack and valid command check
    elif stack == [] and (x[0:4]=="push" or x[0:3]=="pop"):
        print("stack is empty")

    #pop operation
    elif x[0:3]=="pop":
        stack.pop()
        if stack != []:
            print(stack)
        else:
            print("stack is empty")

    #exit the program
    elif x == "exit":
        break

    else:
        print("invalid syntax")
