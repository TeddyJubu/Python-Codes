from collections import deque
# deque object is used because without it pop operation takes too much memory as it needs to shift all the items in the list one step back

print("Type 'insert' to insert something to the queue and delete to delete from it. \n example 'delete a' \n To exit the program type exit. \n everything will be in lowercase")
queue = deque([])
x = ''

while 1:

    x = input("->")
    x = x.lower()

    #insert operation
    if x[0:6]=="insert":
        queue.append(x[7:])
        print(queue)
    
    #empty queue and valid command check
    # if not queue means queue is empty
    elif not queue and (x[0:6]=="insert" or x[0:6]=="delete"):
        print("queue is empty")

    #delete operation
    elif x[0:6]=="delete":
        queue.popleft()
        if queue : #means queue is not empty
            print(queue)
        else:
            print("queue is empty")

    #exit the program
    elif x == "exit":
        break

    else:
        print("invalid syntax")
