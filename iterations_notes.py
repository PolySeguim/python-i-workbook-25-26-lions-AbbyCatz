def variable():
    airtime_remaining = 15 + 3
    print(airtime_remaining)
    airtime_remaining = 7
    print(airtime_remaining)

    for i in ['red', 'blue', 'yellow']:
        print(i)

    print("printing outside the loop")
    print(i)

    a = 5
    b = a
    a = 3

    print(a, b)
    
def mysum(xs):
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total

def sum_to (n):
    ss = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
        return ss

#Testing Area
def test(pass_fail):
    if pass_fail:
        return True
    else:
        return False

def testsuite():
    print(test(mysum([1, 2, 3, 4]) == 10))
    print(test(mysum([1.25, 2.5, 1.75]) == 5.5))
    print(test(mysum([1, -2, 3]) == 2))
    
