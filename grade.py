name = input("Enter student name: ")

mark1 = float(input("Enter first subject mark: "))
mark2 = float(input("Enter second subject mark: "))

total_marks = mark1 + mark2
average = total_marks / 2

is_pass = "Pass" if mark1 > 40 and mark2 > 40 else "Fail"

print("Student Name: ", name)
print("Average mark: ", average)
print("Result: ", is_pass)

