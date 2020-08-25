#Excersice 2 faulty calculator

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
op1 = input("Enter opertor which you want to perform: ")

if op1 == "+":
    if num1 == 56 and num2 == 9:
        print(int(77))
    else:
        print(int(num1+ num2))
elif op1 == "-":
    print(int(num1- num2))
elif op1 == "*":
    if num1 == 45 and num2 == 3:
        print(int(555))
    else:
        print(int(num1 * num2))
elif op1 == "/":
    if num1 == 56 and num2 == 6:
        print(int(4))
    else:
        print(float(num1/num2))
else:
    print("This is not operator any more.")


