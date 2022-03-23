#Conditional statements
# print("PYTHON PROGRAM THAT ACCEPTS AND COMPARES TWO NUMBERS")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if num2 > num1:
    print(f"{num2} is greater than {num1}")
    
elif num2 < num1:
    print(f"{num2} is less than {num1}")
elif num2 == num1:
    print(f"{num2} is same as {num1}")
    
else:
    print(f"No conditions were true")

#Nested If
# if num2 > num1:
#     if num2 != num1:
#     print(f"{num2} is greater than {num1}")    
# else:
#     print(f"No conditions were true")

#Multiple conditions using and/or
# if num2 > num1 or num2 != num1:
#     print(f"{num2} is greater than {num1}")
#     
# else:
#     print(f"No conditions were true")

#Empty Condidionals - pass
if num1 <= num2:
    pass

#Ternary Operator or conditional expression method
x = 5
y = 6
if x < y: print(f"{x} is less than {y}")