# QUEUE IMPLEMENTATION USING PYTHON

MAX_SIZE = 5
queue = []

# ENQUEUE OPERATION
def enqueue(value):
    if len(queue) == MAX_SIZE:
        print("Queue Overflow! Queue is full.")
    else:
        queue.append(value)
        print(value, "inserted into the queue.")

# DEQUEUE OPERATION
def dequeue():
    if len(queue) == 0:
        print("Queue Underflow! Queue is empty.")
    else:
        removed = queue.pop(0)
        print(removed, "removed from the queue.")

# PEEK OPERATION
def peek():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Front element:", queue[0])

# REAR OPERATION
def show_rear():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Rear element:", queue[-1])

# CHECK IF QUEUE IS EMPTY
def is_empty():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Queue is not empty.")

# CHECK IF QUEUE IS FULL
def is_full():
    if len(queue) == MAX_SIZE:
        print("Queue is full.")
    else:
        print("Queue is not full.")

# DISPLAY QUEUE
def display():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Queue elements:", queue)


# PERFORMING QUEUE OPERATIONS

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)

display()

peek()

show_rear()

dequeue()

display()

enqueue(50)
enqueue(60)

display()

is_empty()

is_full()