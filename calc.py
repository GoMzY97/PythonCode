first =input("Enter first number : ")
op =input("Enter operator (+,-,*,/,%) : ")
second =input("Enter second number : ")

first = int(first)
second = int(second)

if op == "+":
	print(first + second)
elif op == "-":
	print(first - second)

elif op == "*":
	print(first * second)

elif op == "/":
	print(first / second)

elif op == "%":
	print(first % second)
else:
	print("Invalid Operation")


