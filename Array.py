from array import *

numbers = array('i',[])
for i in range(0,5):
    number = int(input("Enter a number: "))
    numbers.append(number)

numbers = sorted(numbers)
numbers.reverse()

import random

nums = array('i',[])

for i in range(0,5):
    num = random.randint(1,100)
    nums.append(num)

for i in nums:
    print(i)

nummies = array'i',[])
while len(nummies) < 5
nummy = int(input(Enter a number from 10 to 20: ))
if nummy >= 10 and nummy <=20:
    nummies.append(nummy)
else:
    print("number not in range")

for i in nummies(1):
    print(i)