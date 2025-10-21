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
"""
def isDivisible(x, y):
    if (x%y == 0):
        return True
    else:
        return False
"""

# A fruitful compare function that compares two integers
# and returns the largest integers 
"""
def compare(num1, num2):
    if(num1>num2):
        return num1
    elif(num2>num1):
        return num2
    else:
        print("Numbers are equal")
        return 0
"""
"""
print(compare(5, 4))
print(compare(5, -4))
print(compare(-5, 4))
print(compare(5, 0))
print(compare(5.5, 4))
print(compare(5, 4.4))
print(compare(0, 4))
print(compare(0, 0))
print(compare(10, 10))
"""
# A fruitful hypotenuse that returns the value of
# the hypotenuse given the a and b value
"""
def hypotenuse(numA, numB):
    hypoTenuse = (numA**2 + numB**2)**(1/2)
    return hypoTenuse
"""
"""   
print(hypotenuse(3, 4))
print(hypotenuse(5, 8))
print(hypotenuse(12, 13))
"""

# A fruitful slope function that returns the slope of a line
# given 4 parameters (x1, y1, x2, y2)
"""
def slope(x1,y1,x2,y2):
    slope = (x2-x1)/(y2-y1)
    return slope

def y_int(x1, y1, x2, y2):
    yInt = y1-(slope(x1,x2,y1,y2)*x1)
    return yInt
"""
#x1 = int(input("What does x1 equal? "))
#y1 = int(input("What does y1 equal? "))
#x2 = int(input("What does x2 equal? "))
#y2 = int(input("What does y2 equal? "))
"""
print(slope(2, 3, 4, -4))
print(y_int(3,-5,7,-11))
"""

# A fruitful intercept function function that will find the y-intercept
# given two points (x1, y1, x2, y2)
# *** This function should call the slope function in order to
# *** calculate the y-intercept or b-value



# A fruitful function that will calculate whether a number is
# a factor of another number.
# *** Is 3 a factor of 9?
# *** return a BOOLEAN (True or False)
"""
def function(funcA, funcB): 
    funcC = funcA % funcB
    print(bool(funcC==0))
    return bool
    
    
print(function(8, 4))
print(function(8, 5))
"""
    

# A fruitful function function thaat will calculate whether a number is
# a multiple of another another number.
# *** Is 12 a multiple of 36?
# *** return a BOOLEAN (True or False)
"""
def multiple(multA, multB):
    multC = multB % multA
    print(bool(multC==0))
    return bool

print(multiple(8, 4))
print(multiple(8, 5))
print(multiple(4, 8))
"""


"""
print(isDivisible(5,2))
print(isDivisible(12,4))
print(isDivisible(18,6))
"""