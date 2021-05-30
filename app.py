# Collaborated with Liz for this assignment.

# Importing modules to use them.
from addition import add
from subtraction import subtract
from division import divide
from multiplication import multiply
# This prints out a selection of operations for the user to choose from.
print("""Hello, this is a simple calculator. Please select from the following operators:
1) Addition
2) Subtraction
3) Multiplication
4) Division""")
# This takes in the user's input to determine which operation they have chosen.
# Using the int function to convert user input into an integer.
operations = int(input("Enter your selection: "))
# This takes in the user's input to determine the number they have chosen.
# Using the int function to convert user input into an integer.
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

# Conditionals that print our results by taking in specific functions.
# These conditinals are dependent on the operation that is chosen by the user.
if(operations == 1):
  print("Your result is:", add(first_number, second_number))
elif(operations == 2):
  print("Your result is:", subtract(first_number, second_number))
elif(operations == 3):
  print("Your result is:", multiply(first_number, second_number))
elif(operations == 4):
  print("Your result is:", divide(first_number, second_number))
else:
  print("Invalid operator, please try again")
