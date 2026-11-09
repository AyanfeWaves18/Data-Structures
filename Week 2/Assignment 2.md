IMPLEMENTATION OF QUEUE DATA STRUCTURE USING PYTHON

2.1 Definition of Queue
A Queue is a linear data structure that follows the FIFO (First In, First Out) principle. This means that the first element inserted into the queue is the first element to be removed.

A real-life example is a queue of students waiting to collect their examination results. The student who arrives first is attended to first.
2.2 Real-Life Applications of Queue
1. Printer Queue: Documents sent to a printer are arranged in a queue and printed in the order they were received.
2. Customer Service Systems: Customers waiting for assistance are attended to in the order they arrive.
3. CPU Scheduling: Operating systems use queues to manage processes waiting for CPU execution.
4. Network Communication: Network devices use queues to manage data packets waiting for transmission.
5. Call Centre Systems: Incoming calls are placed in a queue until an available operator can attend to them.
2.3 Basic Operations of Queue
Operation	Description
Enqueue	Adds an element to the rear of the queue.
Dequeue	Removes an element from the front of the queue.
Peek/Front	Displays the first element without removing it.
Rear	Displays the last element in the queue.
isEmpty	Checks whether the queue is empty.
isFull	Checks whether the queue is full.
Display	Displays all elements in the queue.


2.4 Algorithm for Implementing Queue
Step 1: Start.

Step 2: Declare an array to store queue elements.

Step 3: Initialise FRONT and REAR to -1.

Step 4: Display the available queue operations.

Step 5: Perform the following operations:
- Enqueue: Check if the queue is full. If it is not full, insert the new element at the rear.
- Dequeue: Check if the queue is empty. If it is not empty, remove the element at the front.
- Peek: Display the front element.
- Rear: Display the last element.
- isEmpty: Check whether the queue is empty.
- isFull: Check whether the queue is full.
- Display: Display all elements in the queue.
Step 6: Allow the user to select an operation.

Step 7: Repeat the process until the user chooses to exit.

Step 8: Stop.