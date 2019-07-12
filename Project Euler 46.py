import math
import time

primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
odd_composites = [9, 15, 21, 25, 27, 33, 35, 39, 45, 49, 51, 55, 57, 63, 65, 69, 75, 77, 81, 85, 87, 91, 93, 95, 99]
start = time.time()

def primefinder(number):
    for y in range(103, number + 1, 2):
        prime = True
        for x in primelist:
            if y % x == 0:
                prime = False
                odd_composites.append(y)
                break
            if x > math.sqrt(y):
                break
        if prime == True:
            primelist.append(y)

primefinder(6000)

def Goldbachs_other_conjecture(found):
    for x in odd_composites:
        for y in primelist:
            if x > y:
                if math.sqrt((x-y)/2).is_integer() == False:
                    continue
                else:
                    break
            else:
                print(x)
                return None

Goldbachs_other_conjecture(True)

end = time.time()
print(end - start)
