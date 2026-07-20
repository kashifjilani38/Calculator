# Calculator
This Python program is a simple command-line calculator that performs basic arithmetic operations: addition (+), subtraction (-), multiplication (*), and division (/). It first asks the user to enter two numbers and an operator, then calculates and displays the result. The program validates the operator and prevents division by zero by displaying an error message and exiting if necessary.

After the initial calculation, the calculator enters a continuous loop, allowing the user to perform additional calculations using the previous result. The user can repeatedly choose an operator and enter another number to update the current result. If an invalid operator is entered, the program closes gracefully. It also uses exception handling (try-except) to catch invalid numeric inputs and prompts the user to try again instead of crashing.

Overall, the program demonstrates the use of:

User input with input()
Type conversion using float()
Conditional statements (if, elif, else)
A while loop for repeated calculations
Error handling with try-except
Input validation for operators and division by zero
Formatted output using f-strings to display calculation results clearly.
