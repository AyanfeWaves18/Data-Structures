REAL-LIFE APPLICATIONS OF STACK DATA STRUCTURE

1.1 Definition of Stack
A Stack is a linear data structure that follows the LIFO (Last In, First Out) principle. This means that the last element inserted into the stack is the first element to be removed.

A good real-life example is a pile of plates. When plates are stacked on top of one another, the last plate placed on top is the first one removed.
1.2 Real-Life Applications of Stack
Stacks are used in several real-world applications, including:
1. Web Browser History: Browsers such as Google Chrome use stack-based operations to manage browsing history. When a user clicks the Back button, the browser returns to the previously visited page.
2. Undo and Redo Operations: Applications such as Microsoft Word and Adobe Photoshop use stacks to keep track of actions. The most recent action can be undone first.
3. Function Calls and Recursion: Programming languages use a call stack to manage function execution. Whenever a function is called, it is added to the call stack and removed when execution is completed.
4. Expression Evaluation: Compilers and calculators use stacks to evaluate mathematical expressions and convert expressions between different formats.
5. Mobile Application Navigation: Mobile applications use stack-based navigation to manage screens. Pressing the Back button takes the user to the previous screen.
6. Bracket Matching: Compilers use stacks to check whether brackets, parentheses and braces in a programming code are properly opened and closed.
1.3 Where Stack is Operational
Stacks are operational in the following areas:
- Google Chrome and Mozilla Firefox browsers.
- Microsoft Word and other text editors.
- Adobe Photoshop.
- Programming languages and compilers.
- Operating systems.
- Calculator applications.
- Mobile application navigation systems.
1.4 Basic Operations of Stack
Operation	Description
Push	Adds an element to the top of the stack.
Pop	Removes the top element from the stack.
Peek	Displays the top element without removing it.
isEmpty	Checks whether the stack is empty.
isFull	Checks whether the stack is full.
Display	Displays all elements in the stack.


1.5 Practical Implementation of Stack Using Python
For this practical example, we will use an array of 5 elements, representing a class size of five students.

The students' identification numbers will be stored in the stack.

Initial Array:

Stack = [101, 102, 103, 104, 105]

The maximum capacity of the stack is 5.