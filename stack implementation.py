print("Type 'push' to push something to the stack and pop to pop out of it. example 'push a' ")
x = " "
stack = []
while x != exit:
    x = input("->")
    x = x.lower()
    if x[0:4]=="push":
        stack.append(x[5:])
        print(stack)
    elif stack == [] and (x[0:4]=="push" or x[0:3]=="pop"):
        print("stack is empty")
    elif x[0:3]=="pop":
        stack.pop()
        if stack != []:
            print(stack)
        else:
            print("stack is empty")
    elif x == "exit":
        break
    else:
        print("invalid syntax")
