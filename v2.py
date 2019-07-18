import time
import math
start = time.time()
primelist= [2]
odd_composites = []

def primefinder(number):
    prime = [True for x in range(number + 1)]
    for y in range(3,int(math.sqrt(number+1)),2):
        if prime[y] == True:
            for x in range(y+y, number + 1,y):
                prime[x] = False
    for x in range(3,number+1,2):
        if prime[x] == True:
            primelist.append(x)
        else:
            odd_composites.append(x)

primefinder(6000)

def Goldbachs_other_conjecture():
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

Goldbachs_other_conjecture()

end = time.time()
print(end - start)
