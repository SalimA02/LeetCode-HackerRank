stack1 = []
stack2 = []

def enqueue(x):
    stack1.append(x)

def dequeue():
    if not stack2:
        shift_stacks()
    if stack2:
        stack2.pop()

def front():
    if not stack2:
        shift_stacks()
    if stack2:
        print(stack2[-1])

def shift_stacks():
    while stack1:
        stack2.append(stack1.pop())

if __name__ == "__main__":
    q = int(input())
    
    for _ in range(q):
        query = input().split()
        query_type = int(query[0])
        
        if query_type == 1:
            x = int(query[1])
            enqueue(x)
        elif query_type == 2:
            dequeue()
        elif query_type == 3:
            front()
