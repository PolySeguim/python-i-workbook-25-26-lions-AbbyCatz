"""
Exercise 21:  Area of a Triangle
The area of a triangle can be computed using the following formula,
where b is the length of the base of the triangle, and h is its 
height:
        area = (b*h)/2
Write a program that allows the user to enter values for b and h.
The program should then compute and display the area of a triangle
with base length b and height h
"""
def triangle():
    b = float(input("What is the length? "))
    h = float(input("What is the height? "))
    area = (b*h)/2
    print(area)
#triangle()

"""
Exercise 22: Area of a triangle (Again)
In the previous exercise you created a program that computed the area
of a triangle when the length of its base and its height were known.
It is also possible to compute the area of a triangle when the lengths
of all three sides are known.  Let s1, s2, and s3 be the lengths of the
sides.  Let s = (s1 + s2 + s3)/2.  Then the area of a triangle can be 
calculated using the following formula:

     area = (s * (s - s1) * (s - s2) * (s - s3))**(1/2)

Develop a program that reads the lengths of the sides of a triangle from
the user and display its area.
"""
def triangleSides():
    s1 = float(input("How long is side 1 of the triangle? "))
    s2 = float(input("How long is side 2 of the triangle? "))
    s3 = float(input("How long is side 3 of the triangle? "))
    s = (s1 + s2 + s3) / 2
    area = (s * (s - s1) * (s - s2) * (s - s3)) ** (1/2)
    print(area)
#triangleSides()

"""
Exercise 23:  Area of a Regular Polygon
A polygon is regular if its sides are all the same length and the angles
between all of the adjacent sides are equal.  The area of a regular polygon
can be computed using the following formula, where s is the length of a side
and n is the number of sides: 
     area = (n * s**(2))/(4 * tan(pi/n))
Write a program that reads s and n from the user and then displays the area
of a regular polygon constructed from these values.
"""
def regularPolygon():
    import math
    s = float(input("How long are the sides? "))
    n = float(input("How many sides are there? "))
    area = (n * s**(2))/(4 * math.tan(math.pi/n))
    print(area)
#regularPolygon()

"""
Exercise 24: Units of Time
Create a program that reads a duration from the user as a number of days,
hours, minutes, and seconds.  Compute the total number of seconds represented
by this duration.
"""
def unitsOfTime():
    days = float(input("How many days? "))
    hours = float(input("How many hours? "))
    minutes = float(input("How many seconds? "))
    seconds = float(input("How many seconds? "))
    totalSeconds = (days * 86400) * (hours * 3600) * (minutes * 60) * (seconds * 1)
    print(totalSeconds)
#unitsOfTime()

""" 
Exercise 25: Units of Time (again)
In this exercise you will reverse the process described in the previous 
exercise.  Develop a program that begins by reading a number of seconds from 
the user.  Then your program should display the equivalent amount of time 
in the form D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, 
minutes and seconds respectively.  The hours, minutes and seconds should all
be formatted so that they occupy exactly two digits, with a leading 0 displayed
if necessary.
"""
def userTime():
    userSeconds = int(input("How many seconds? "))
    days = userSeconds // 86400
    userSeconds = userSeconds-(days * 86400)
    hours = userSeconds // 3600
    userSeconds = userSeconds-(hours * 3600)
    minutes = userSeconds // 60
    userSeconds = userSeconds-(minutes * 60)
    seconds = userSeconds // 1
    userSeconds = userSeconds-(seconds * 1)
    if len(str(hours))<2:
        hours = "0" + str(hours)
    if len(str(minutes))<2:
        minutes = "0"+str(minutes)
    if len(str(seconds))<2:
        seconds = "0"+str(seconds)
    print(str(days)+":"+str(hours)+":"+str(minutes)+":"+str(seconds))
#userTime()