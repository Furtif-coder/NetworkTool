# FUNCTIONS

# convert a decimal byte to binary
def toBinary(decimalNumber):
    power = 7
    binaryNumber = ""
    while power > 0:
        weight = 2 ** power
        if decimalNumber >= weight:
            binaryNumber += "1"
        else:
            binaryNumber += "0"
        power -= 1
    return binaryNumber

# convert a binary byte to decimal
def toDecimal(binaryNumber):
    pass

# convert a decimal IP to binary
def ipToBinary():
    pass

# convert a binary IP in to decimal
def ipToDecimal():
    pass
