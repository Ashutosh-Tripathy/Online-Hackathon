def convertBase(digits, c):
    """Convert the digits representation of a number from base b to base c."""
    return toDigits(digits, c)

def toDigits(n, b):
    """Convert a positive number n to its digit representation in base b."""
    digits = []
    while n > 0:
        digits.insert(0, n % b)
        n  = n // b
    return digits

def isPanlindrome(inputOnNewBase):
    print(inputOnNewBase)
    #listInputOnNewBase=list(str(inputOnNewBase))
    for i in range(int(len(inputOnNewBase)/2)):
        if(inputOnNewBase[i]!=inputOnNewBase[len(inputOnNewBase)-i-1]):
            return False
    return True

def getInputOnNewBase(inputNumber,base):
    
    return inutNumber

inputNumber=int(input())
base=2
while(True):
    inputOnNewBase=convertBase(inputNumber,base)
    if(isPanlindrome(inputOnNewBase)):
        print(base)
        break
    base +=1