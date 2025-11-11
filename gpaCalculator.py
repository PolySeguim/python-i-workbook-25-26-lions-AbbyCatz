import math
"""
Exercise 51:  Letter Grade to Grade Points

At a particular university, letter grades are mapped to grade
points in the following manner:

Letter                  Grade points
A+                      4.0
A                       4.0
A-                      3.7
B+                      3.3
B                       3.0
B-                      2.7
C+                      2.3
C                       2.0
C-                      1.7
D+                      1.3
D                       1.0
F                       0


Write a program that begins by reading a letter grade from the 
user.  Then your program should compute and display the equivalent
number of grade points.  Ensure that your program generates an 
appropriate error message if the user enters an invalid letter
grade.
"""

#Create global variables because you dont want these values to change

A_PLUS  = 4.0
A       = 4.0 
A_MINUS = 3.7
B_PLUS  = 3.3
B       = 3.0 
B_MINUS = 2.7
C_PLUS  = 2.3
C       = 2.0 
C_MINUS = 1.7
D_PLUS  = 1.3
D       = 1.0 
D_MINUS = 0.7
F       = 0.0 
INVALID = -1

def readLetter():
    letter = input("Enter a letter grade: ")
    letter = letter.upper()
    readLetter()


def assignGPA(letter):
    gpa = 0
    if (letter == "A+" or "A"):
        gpa = A
    elif(letter == "A-"):
        gpa = A_MINUS
    elif(letter == "B+"):
        gpa = B_PLUS
    elif(letter == "B"):
        gpa = B
    elif(letter == "B-"):
        gpa = B_MINUS
    elif(letter == "C+"):
        gpa = C_PLUS
    elif(letter == "C"):
        gpa = C
    elif(letter == "C-"):
        gpa = C_MINUS
    elif(letter == "D+"):
        gpa = D_PLUS
    elif(letter == "D"):
        gpa = A_MINUS
    elif(letter == "A-"):
        gpa = D
    elif(letter == "D-"):
        gpa = D_MINUS
    else:
        gpa = INVALID
    assignGPA(letter)


"""
Exercise 52:  In the previous exercises you created a program that
converts a letter grade into the equivalent number of grade points.
In this exercise you will create a program that reverses the process
and converts from a grade point value entered by the user to a letter
grade.  Ensure that your program handles grade point values that fall
between letter grades.  These should be rounded to the closes letter
grade.  Your program should report A+ for a 4.0 (or greater) grade
point average.
"""

def assignLetter(given_gpa):
    if(given_gpa >= 4.0):
        letter_grade = "A+"
    elif(given_gpa < 4.0 and given_gpa >= 3.7):
        letter_grade = "A-"
    elif(given_gpa < 3.7 and given_gpa >= 3.3):
        letter_grade = "B+"
    elif(given_gpa < 3.3 and given_gpa >= 3.0):
        letter_grade = "B"
    elif(given_gpa < 3.0 and given_gpa >= 2.7):
        letter_grade = "B-"
    elif(given_gpa < 2.7 and given_gpa >= 2.3):
        letter_grade = "C+"
    elif(given_gpa < 2.3 and given_gpa >= 2.0):
        letter_grade = "C"
    elif(given_gpa < 2.0 and given_gpa >= 1.7):
        letter_grade = "C-"
    elif(given_gpa < 1.7 and given_gpa >= 1.3):
        letter_grade = "D+"
    elif(given_gpa < 1.4 and given_gpa >= 1.0):
        letter_grade = "D"
    elif(given_gpa < 1.0 and given_gpa >= 0.7):
        letter_grade = "D-"
    elif(given_gpa < 0.7 and given_gpa >= 0):
        letter_grade = "F"
    else:
        letter_grade = "INVALID"
    assignLetter(given_gpa)


"""
Exercise 66:  Compute a Grade Point Average
Exercise 51 includes a table that shows the conversion from letter
grades to grade points at a particular academic institution.  In this
exercise you will compute the grade point average of an arbitrary number
of letter grades entered by the user.  The user will enter a blank
line to indicate that all of the grades have been provided.  For example,
if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solutions to Exercise 51 helpful when completing this 
exercise.  Your program does not need to do any error checking.  It can
assume that each value entered by the user will be a valid letter grade
or a blank line.
"""
"""
def giveAvgGPA():
    while True: 
        grade1 = input("Input letter grade: ")
        grade2 = input("Input letter grade: ")
        grade3 = input("Input letter grade: ")
        grade4 = input("Input letter grade: ")
        grade5 = input("Input letter grade: ")
        grade6 = input("Input letter grade: ")
        grade7 = input("Input letter grade: ")
        grade8 = input("Input letter grade: ")
"""

def giveAvgGPA(grade):
    if (grade == "A+" or "A"):
        gpa = 4.0
    elif(grade == "A-"):
        gpa = 3.7
    elif(grade == "B+"):
        gpa = 3.3
    elif(grade == "B"):
        gpa = 3.0
    elif(grade == "B-"):
        gpa = 2.7
    elif(grade == "C+"):
        gpa = 2.3
    elif(grade == "C"):
        gpa = 2.0
    elif(grade == "C-"):
        gpa = 1.7
    elif(grade == "D+"):
        gpa = 1.3
    elif(grade == "D"):
        gpa = 1.0
    elif(grade == "D-"):
        gpa = 0.7
    elif(grade == "F"):
        gpa = 0.0
    else:
        gpa = INVALID
    return gpa



"""
sumofLets = 0
count = 0  
letters = float(input("Input letter grade: "))           
for number in letters:
    sumofLets += letters
    count += 1
average = sumofLets / count
print("Your gpa is:", letters)
"""
"""
a = []
numGrades = int(input("How many grades do you have? "))


for i in range(numGrades):
    print(f"\n--- Grade {i+1} ---")
    grade = input("Input letter grade: ")
    a.append(grade)
    if(grade == "A+"):
        grade = 4.0
    elif(grade == "A"):
        grade = 4.0 
    elif(grade == "A-"):
        grade = 3.7
    elif(grade == "B+"):
        grade = 3.3
    elif(grade == "B"):
        grade = 3.0
    elif(grade == "B-"):
        grade = 2.7
    elif(grade == "C+"):
        grade = 2.3
    elif(grade == "C"):
        grade = 2.0
    elif(grade == "C-"):
        grade = 1.7
    elif(grade == "D+"):
        grade = 1.3
    elif(grade == "D"):
        grade = 1.0
    elif(grade == "D-"):
        grade = 0.7
    elif(grade == "F"):
        grade = 0.0
    else:
        print("Invalid")

print(a)
finalGrade = sum(a)
finalGrade / numGrades
number = finalGrade / numGrades
print("your gpa is", number)
"""
def getGrades():
    gradesList = []
    grade = "nothing"
    while grade != "":
        grade = input("What is the grade ")
        gradesList.append(grade)
    return gradesList

def gpaCalculator(grades):
    gpav = 0
    for i in range(len(grades)-1):
        gpav += giveAvgGPA(grades[i])
    gpav = gpav/(len(grades)-1)
    print(gpav)
    return gpav
gpaCalculator(getGrades())
    