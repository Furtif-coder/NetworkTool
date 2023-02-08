# FUNCTIONS

# convert a decimal byte to binary
def toBinary(decimalNumber):

    # checking errors
    try:
        number = int(decimalNumber)
        if number < 0 or number > 255:
            return 1 # Out of range
        else:
            decimalNumber = number
        
    except ValueError:
        return 2 # Extra characters
    
    

    power = 7
    binaryNumber = ""
    while power >= 0:
        weight = 2 ** power
        if decimalNumber >= weight:
            binaryNumber += "1"
            decimalNumber -= weight
        else:
            binaryNumber += "0"
        power -= 1
    return binaryNumber

# convert a binary byte to decimal
def toDecimal(binaryNumber):
    # checking errors
    try:
        if int(binaryNumber) < 0:
            return 1 # Negative number
        elif len(binaryNumber) > 8:
            return 2 # more than 8 bits
        else:
            for digit in binaryNumber:
                if int(digit) > 1:
                    return 3 # Digit other than '0' or '1'       
        
    except ValueError:
        return 4 # extra characters
    
    # Check missing bits and fill them with with '0'    
    if len(binaryNumber) < 8:
        nDigitsOff = 8 - len(binaryNumber)
        while nDigitsOff > 0:
            binaryNumber = "0" + binaryNumber
            nDigitsOff -= 1
        print(binaryNumber)
    


    decimalNumber = 0
    power = 0
    while power < 8:
        weight = 2 ** power
        decimalNumber += weight * int(binaryNumber[7-power])
        power += 1
    return decimalNumber

# convert a decimal IP to binary
def ipToBinary():
    pass

# convert a binary IP in to decimal
def ipToDecimal():
    pass
