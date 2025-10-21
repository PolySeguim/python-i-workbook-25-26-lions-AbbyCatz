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
    return letter

def assignGPA(letter):
    gpa = 0
    if (letter == "A+" or "A"):
        gpa = A
    elif(letter == "A-"):
        gpa = A_MINUS
    else:
        gpa = INVALID
    print(gpa)
    return gpa

def assignLetter(given_gpa):
    letter_grade
    if(given_gpa >= 4.0):
        letter_grade = A
    elif(given_gpa < 4.0 and given_gpa >= 3.7):
        letter_grade = "A-"
    elif(given_gpa < 3.7 and given_gpa >= 3.3):
        letter_grade = "B+"
    else:
        letter_grade = "INVALID"





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

"""
Exercise 66:  Compute a Grade Point Average
Exercise 51 includes a table that shows the conversion from letter
grades to grade points at a particular academic institution.  In this
exercise you will compute the grade point average of an arbitrary number
of letter grades entered by teh user.  The user will enter a blank
line to indicate that all of the grades have been provided.  For example,
if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solutions to Exercise 51 helpful when completing this 
exercise.  Your program does not need to do any error checking.  It can
assume that each value entered by the user will be a valid letter grade
or a blank line.
"""