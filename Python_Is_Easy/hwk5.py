"""
    Date:   2021-02-
    Dev:    Me
    Purpose: 

"""
stopAt = 30
number = 1

def checkPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    print('prime')
    return True

def FizzBuzz(num):
    if num % 3 == 0 and num % 5 ==0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else: 
        return False
    return True

while number <= stopAt:
    if checkPrime(number):
        number += 1
        continue
    
    if FizzBuzz(number):
        number +=1
        continue
    
    print(number)
    number += 1
