"""
Exercise 34: Even or Odd?
Write a program that reads an integer from the user.
Then your program should display a message indicating whether
the integer is even or odd
"""

def evenOdd():
    num = int(input("Input an integer: "))
    if (num%2 == 0):
        print("The number is even")
    else:
        print("The number is odd")



"""
Exercise 36: Vowel or consonant
In this exercise you will create a program that reads a letter
of the alphabet from the user. If the user enters a, e, i, o, or u
then your program should display a message indicating that the
entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and
sometimes y is a consonant. Otherwise your program should display
a message indicating that the letter is a consonant.
"""

import string
def alphabetLetters():
    letter = input("Input a letter: ")
    consonants = "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"
    if (letter == "a" or 
        letter == "e" or 
        letter == "i" or 
        letter == "o" or letter == "u"):
        print("This letter is a vowel")
    elif (letter == "y"):
        print("This letter is sometimes a vowel and sometimes a consonant")
    elif (letter in consonants):
        print("This letter is a consonant")
    else:
        print("This is not a letter")


"""
Exercise 40: Name that triangle
A triangle can be classified based on the lengths of its sides as
equilateral, isosceles, or scalene. All 3 sides of an equilateral
triangle have the same length. As isosceles triangle has two sides
that are the same length, and a third side that is a different length.
If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the
user. Display a message indicating the type of triangle
****** CHALLENGE:
Perform the same task as above but with angles and not sides.
"""

def triangleSides():
    side1 = float(input("How long is side 1? "))
    side2 = float(input("How long is side 2? "))
    side3 = float(input("How long is side 3? "))
    if (side1 == side2 == side3):
        print("This is an equilateral triangle")
    if (side1 == side2 != side3):
        print("This is an isosceles triangle")
    if (side1 == side3 != side2):
        print("This is an isosceles triangle")
    if (side2 == side3 != side1):
        print("This is an isosceles triangle")
    if (side1 != side2 != side3):
        print("This is a scalene triangle")
        

"""
Exercise 55: Cell Phone Bill
A particular cell phone plan includes 50 minutes of air time and
50 text messages for $15.00 a month. Each additional minute of
air time costs $0.25 , while additional text messages cost $0.15
each. All cell phone bills include an additional charge of $0.44
to support 911 call centers, and the entire bill (including the
911 charge) is subject to a 5 percent sales tax.
Write a program that reads the number of minutes and text messages
used in a month from the user. Display the base charge, additional
minutes charge (if any), additional text message charge (if any),
the 911 fee, tax and total bill amount. Only display the additional
minute and text charges if the user incurred costs in these
categories. Ensure that all of the charges are displayed using 2
decimal points
"""

minutes = float(input("How many minutes a month are you on your phone? "))
textMessages = float(input("How many text messages do you send per month? "))
costNotTax = (15.00 + 0.44 + 0.25 * (minutes - 50) + 0.15 * (textMessages - 50))
allCost = (costNotTax + costNotTax * 0.05)
print(round(allCost, 2))




#test suite

#evenOdd()
#alphabetLetters()
#triangleSides()