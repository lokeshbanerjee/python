print("..... MY FIRST ADVANCE CALCULATOR......")
print("======================================================================")
num1 = float(input("Enter your first digit "))
print("")
op = input("Choose your sign +,-,/,* ")
print("")
num2 = float(input("Enter your next digit "))
print("")
if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '/':
    print(num1/num2)
elif op == '*':
    print(num1*num2)
else:
    print("oops... Not a valid key. please check again.")



