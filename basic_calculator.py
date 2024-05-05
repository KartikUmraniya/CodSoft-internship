

# function to take number of values user wants to operate 
def calculator(num_values):
 

  values = []
  for i in range(num_values):
    values.append(float(input("Enter value " + str(i + 1) + ": ")))

  operation = input("Enter the operation (+, -, *, /,%, //(for floor division)): ")
# Addition operation 
  if operation == "+":
    result = sum(values)

# Subtraction operation 
  elif operation == "-":
    result = values[0]
    for i in range(1, len(values)):
      result -= values[i]

# Multiplication operation 
  elif operation == "*":
    result = 1
    for value in values:
      result *= value

# Division operation 
  elif operation == "/":
    result = values[0]
    for i in range(1, len(values)):
      result /= values[i]

# Mod operation 
  elif operation == "%":
    result = values[0]
    for i in range(1, len(values)):
      result %= values[i]

# floor division operation 

  elif operation == "//":
    result = values[0]
    for i in range (1, len(values)):
      result //= values[i]

# if user enter any othe operations 
  else:
    print("Invalid operation. Please try again.")
    return

  print("Result:", result)

# Get the number of values from the user
num_values = int(input("Enter the number of values: "))

# Call the calculator function
calculator(num_values)