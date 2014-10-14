############## Main Hash Function ##############

import memoized

@memoized.memoized
def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = int(round(n**0.5))
    for factor in xrange(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

@memoized.memoized
def nthPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (isPrime(guess)):
            found += 1
    return guess

@memoized.memoized
def changeToBase62(n, length=None):
    # Base 62: 0-9, followed by a-z, and finally A-Z.
    numOfLetters = 26
    numOfNumbers = 10
    base = numOfNumbers + numOfLetters*2
    base62 = ""
    while n > 0:
        temp = n%base
        if numOfNumbers <= temp < numOfNumbers + numOfLetters:
            number = chr(ord('a') + temp - numOfNumbers)
        elif numOfNumbers + numOfLetters <= temp < base:
            number = chr(ord('A') + temp - (numOfNumbers + numOfLetters))
        else:
            number = str(temp)
        base62 = number + base62
        n /= base

    if (length != None):
        while len(base62) < length: base62 = "0" + base62

    return base62

def hash(s):
    sumOfUnicode = 0
    length = 0
    lengthCode = 0
    key = "0000"
    spaceCount = 0
    for char in s:
        sumOfUnicode += ord(char)*length
        spaceCount += 1
        lengthCode += ord(char)*nthPrime(spaceCount)
        length += 1

    base = 62
    codedSum = changeToBase62(sumOfUnicode%(base**4), 4)
    key = key[:-len(codedSum)] + codedSum
    key = changeToBase62(lengthCode%(base**2), 2) + key

    return key
