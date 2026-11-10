name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
marks = float(input("Enter Marks: "))

print("\n--- Student Details ---")
print(f"Name     : {name}")
print(f"Roll No  : {roll_no}")
print(f"Marks    : {marks}")

if marks >= 40:
    print("Result   : Pass")
else:
    print("Result   : Fail")
    