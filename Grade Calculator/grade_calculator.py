# User name input
name = input("Enter Your Name: ")

# Welcome Banner
welcome = f"Welcome to Our Grade Calculator {name}"
print(welcome.center(80, "-"))

# Marks input with validation
try:
    marks = int(input("Enter Your Marks: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

# Grade calculator
if 90 <= marks <= 100:
    grade = "Ex"
elif 80 <= marks < 90:
    grade = "A"
elif 70 <= marks < 80:
    grade = "B"
elif 60 <= marks < 70:
    grade = "C"
elif 50 <= marks < 60:
    grade = "D"
elif 0 <= marks < 50:
    grade = "F"
else:
    print("Error! Marks should be between 0 and 100.")
    exit()

# Result
if grade == "F":
    print("You Failed, Try better next year!")
else:
    print("You passed successfully!")

print("Your Grade is:", grade)