# First Activity 1/27/2025

grade = eval(input("Input your grade this semester: "))
if grade > 100 or grade < 0:
    print("Invalid Grade")
elif grade >= 95 and grade <= 100:
    print("You got an A!")
elif grade >= 90 and grade <= 94:
    print("You got a B!")
elif grade >= 85 and grade <= 89:
    print('You got a C!')
elif grade >= 80 and grade <= 84:
    print('You got a D!')
elif grade >= 75 and grade <= 79:
    print('You got an E!')
else:
    print('You failed!')    