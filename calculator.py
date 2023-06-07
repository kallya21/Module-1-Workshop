#Ask user to enter integers

number_1 = int(input("Please enter your first number. "))
number_2 = int(input("Now enter your second number. "))

#Ask user to enter mathematical operation

math_operation = input("""What maths operation would you like to carry out?
Please select one of the options below.
+ To add the numbers
- To subract the smaller number from the larger number
x To multiply both numbers
/ To divide the larger number by the smaller number. """)

#Carry out the maths operation

if math_operation == "+":
    number_output = number_1 + number_2
    print (f"The result of {number_1} {math_operation} {number_2} is {number_output}.")
elif math_operation == "-":
    number_output = number_1 - number_2
    print (f"The result of {number_1} {math_operation} {number_2} is {number_output}.")
elif math_operation.lower() == "x":
    number_output = number_1 * number_2
    print (f"The result of {number_1} {math_operation} {number_2} is {number_output}.")