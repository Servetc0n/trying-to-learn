# [Servetc0n]'s GRADE CALCULATOR
print("=== GRADE CALCULATOR ===")
midterm = float(input("Midterm: "))
final = float(input("Final: "))
average = midterm * 0.4 + final * 0.6
print(f"Your average: {average:.2f}")

if average >= 50:
    print("YOU PASSED!")
else:
    print("FAILED!")
