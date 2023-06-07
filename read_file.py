#define variables

total = 0

#Read input from text file and split each line into a list

with open("calculator_input.txt", "r", encoding="utf-8-sig") as f:
    for line in f:
        line = line.strip("\n")
        line_split = line.split()
        math_operation = line_split[1]
        number_1 = int(line_split[2])
        number_2 = int(line_split[3]) 
        
        #Carry out the maths operation
        if math_operation == "+":
            number_output = number_1 + number_2
        elif math_operation == "-":
            number_output = number_1 - number_2
        elif math_operation.lower() == "x":
            number_output = number_1 * number_2
        elif math_operation == "/":
            number_output = number_1 / number_2
            
        #Add total
        total += number_output
        
    #Print out the total
    print (f"The total result is {total}.")