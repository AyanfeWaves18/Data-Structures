# Stack Implementation Using Python

stack = []
MAX_SIZE = 5

# PUSH OPERATION
def push(value):
    if len(stack) == MAX_SIZE:
        print("Stack Overflow! Stack is full.")
    else:
        stack.append(value)
        print(value, "added to the stack.")

# POP OPERATION
def pop():
    if len(stack) == 0:
        print("Stack Underflow! Stack is empty.")
    else:
        removed = stack.pop()
        print(removed, "removed from the stack.")

# PEEK OPERATION
def peek():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Top element:", stack[-1])

# CHECK IF STACK IS EMPTY
def is_empty():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Stack is not empty.")

# CHECK IF STACK IS FULL
def is_full():
    if len(stack) == MAX_SIZE:
        print("Stack is full.")
    else:
        print("Stack is not full.")

# DISPLAY STACK
def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Stack elements:", stack)


# PERFORMING STACK OPERATIONS

push(101)
push(102)
push(103)
push(104)
push(105)

display()

peek()

pop()

display()

push(106)

display()

is_empty()

is_full()