print('''
      CALCULATOR
      1. ADDITION (+)
      2. SUBTRACTION (-)
      3. DIVIDE (/)
      4. MULTIPLICATION (*)
''' )  

a = int(float(input("enter the number1:")))
b = int(float(input("enter the number2:")))

operator = input("enter the operator:")

if operator == '+':
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '/':
    print(a/b)
elif operator == '*':
    print(a*b)
else:
    print("this is not valid")
        
    
