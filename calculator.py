# [Servetc0n]'s CALCULATOR - self-taught project
print("=== [YOUR NAME]'s CALCULATOR ===")
a = float(input("First number: "))
b = float(input("Second number: "))
op = input("( + - * / ): ")

if op == "+": print("Result:", a + b)
elif op == "-": print("Result:", a - b)
elif op == "*": print("Result:", a * b)
elif op == "/": print("Result:", a / b if b != 0 else "Can't divide by zero!")
else: print("Wrong operation!")
print("Thanks for using!")
