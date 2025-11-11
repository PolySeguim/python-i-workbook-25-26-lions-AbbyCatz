import math

"""
Exercise 108: Negatives, Zeros, and Positives
Create a program that reads integers from the user until a blank
line is entered. Once all of the integers have been read your
program should display all the negative numbers, followed by all
of the zeros, followed b y all of the positive numbers. Within each
group the numbers should be displayed in the same order that they were
entered by the user. For example, if the user enters the values
3, -4, 1, 0, -1, 0, and -2 then your program should output the values
-4, -1, -2, 0 ,0 , 3, and 1. Your program should display each value
on its own line.
"""
"""
def readIntegers():
    integers = []

    try:
        user_input = int(input("Enter an integer: "))
        while user_input != "":
            integers.append(user_input)  
            user_input = int(input("Enter an integer: "))
    except ValueError:
        user_input = ""
        print(f"Error: '{user_input}' cannot be converted to an integer.")    

    return integers
readIntegers()

def displayIntegers(list_integers):
    neg_list = []
    zero_list = []
    pos_list = []
    all_integers = []
    for i in list_integers:
        if i<0:
            neg_list.append(i)
        elif i==0:
            zero_list.append(i)
        else: 
            pos_list.append(i)
    all_integers.extend(neg_list)
    all_integers.extend(zero_list)
    all_integers.extend(pos_list)
    
    return(all_integers)
#displayIntegers(readIntegers())
"""
"""
Exercise 109: List of Proper Divisors
A proper divisor of a positive integer, n, is a positive integer
less than n which divides evenly into n. Write a function that
computes all of the proper divisors of a positive integer. The
integer will be passed to the function as its only parameter.
The function will return a list containing all of the proper divisors
as its only result. Complete this exercise by writing a main program
that demonstrates the function by reading a value from the user and
displaying the list of its proper divisors. Ensure that your main
program only runs when your solution has not been imported into
another file
"""
"""
def getPosInt():
    posInt = int(input("Input a positive integer: "))
    return posInt

def divisorsList(int):
    divList = []''
    for i in range (int):
        if i==0:
            continue
        elif int%i == 0:
            divList.append(i)
    return divList

print(divisorsList(getPosInt()))
"""

"""
Exercise 110: Perfect Numbers
An integer, n, is said to be perfect when the sum of all the proper
divisors of n is equal to n. For example, 28 is a perfect number
because its proper divisors are 1, 2, 4, 7, and 14, and 1+2+4+7+14 = 28.
Write a function that determines whether or not a positive integer is
perfect. Your function will take one parameter. If that parameter is a
perfect number then your function will return true. Otherwise it will
return false. In addition, write a main program that uses your
function to identify and display all of the perfect numbers between 1 and
10,000. Import your solution to Exercise 109 when completing this task.
"""


def getPosInt():
    posInt = int(input("Input a positive integer: "))
    return posInt

def perfectNumber(num):
    #print("Your number is", num)
    
    if num <= 0: 
        return False
    
    sumOfDivisors = 0
    for i in range(1, num):
        if (num % i == 0):
            sumOfDivisors += i
          
    return sumOfDivisors == num

def displayAllPerfs(aNumber):
    perfect_numbers = []
    for number in range(1, aNumber):
        if(perfectNumber(number)):
            perfect_numbers.append(number)
            
    print("Perfect numbers below ", str(aNumber), " are:", perfect_numbers)


def exercise110():
    perfNumber = getPosInt()

    if perfectNumber(perfNumber):
        print("is a perfect number")
    else:
        print("is not a perfect number")


exercise110() 
displayAllPerfs(20000)
displayAllPerfs(100000)