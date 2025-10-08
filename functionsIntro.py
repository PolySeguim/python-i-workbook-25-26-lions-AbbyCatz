#All import statements are up here
import math


#FUNCTION DECLARATION
#void function
def setName(fName):
    #fName is the local function variable
    #f_name is the global function above
    f_name.set(fName)
    f_name = fName
    print(fName)
        

def getName():
    return f_name


#Function Calls
"""
setName("Abby")
setName("Clara")
setName("Ella")


#name = getName()
abby = getName()
"""

def sum(numbers):
    sum = 0
    for i in numbers:
        sum += i
        
    return sum

num1 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10
num2 = 2.3, 4.2, 6.2, 7.3


test1 = sum(num2)
#print(test1)

def absValue(x):
    if x < 0:
        return -x
    return x

def absoluteValue(x):
    if x < 0:
        return -x
    else:
        return x
    
    
#print(absValue(-23))

def distance(x1, y1, x2, y2):
    return math.sqrt( (x2-x1)**2 + (y2-y1) **2 )
    #return ((x2-x1)**2 + (y2-y1)**2)**(0.5)

#print(distance(1, 2, 3, 4))

#Boolean Functions return a true or false
#Examples of boolean functions are
#   - is age 16?
#   - is the pwd correct?

#Fun Fact: boolean functions are normally named as ___
def isDivisible(x, y):
    if (x%y == 0):
        return True
    else:
        return False


"""
print(isDivisible(5,2))
print(isDivisible(12,4))
print(isDivisible(18,6))
"""