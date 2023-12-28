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
def ipToBinary(Ip):
    try:
        a, b, c, d = Ip.split(".")
    except ValueError:
        return -1
    
    ipBinary = f"{toBinary(int(a))}.{toBinary(int(b))}.{toBinary(int(c))}.{toBinary(int(d))}"
    return ipBinary

# convert a binary IP in to decimal
# def ipToDecimal():
# recieves a.b.c.d IP in base 2 and returns a decimal version of the IP
def ipToDecimal(ipBinary):
	a, b, c, d = ipBinary.split('.')

	IP = f"{toDecimal(a)}.{toDecimal(b)}.{toDecimal(c)}.{toDecimal(d)}"
	return IP
   

# From last program
# Read the mask id 
def readMask(num):
	# Reading to Mask IP in base 2
	r = int(num) % 8
	n_fullbytes = int(num) // 8
	n_emptbytes = 4 - n_fullbytes
	
	# The Mask IP in 32bits format
	if r == 0:
		maskBin32 =  "11111111"*n_fullbytes + "00000000"*n_emptbytes
	else:
		maskBin32 =  "11111111"*n_fullbytes + "1"*r + "0"*(8-r) + "00000000"*(n_emptbytes-1)
	
	return maskBin32

# Operation AND between Host and Mask to find the Network Adress
def calculateNetBin32(hostBin32, maskBin32):
	i = 0
	netBin32 = ""
	while i < 32:
		if int(hostBin32[i]) * int(maskBin32[i]) == 0:
			netBin32 += "0"
		else:
			netBin32 += "1"	
		i += 1
	return netBin32

# decode IP/mask
def readFullIP(fullIP):
    try:
        a, b, c, d = fullIP.split(".")
        d, maskID = d.split("/")
        hostDecimal = f"{a}.{b}.{c}.{d}"
    except ValueError:
        return -1
    
    hostBin32 = toBinary(a) + toBinary(b) + toBinary(c) + toBinary(d) # Host IP in 32 bits format - used for calculation
    hostBin = f"{toBinary(int(a))}.{toBinary(int(b))}.{toBinary(int(c))}.{toBinary(int(d))}" # Host IP in binary bytes
    # Reading the 32bits format of a mask IP from a integer || ID_mask --> func: numToIP --> mask in 32bits 
    maskBin32 = readMask(maskID)
    maskBin = Bin32ToBinBytes(maskBin32)
    maskDecimal = ipToDecimal(maskBin)

    # Calculation of the network IP --> function "netIP_Bin" --> returns a.b.c.d in binary
    netBin32 = calculateNetBin32(hostBin32, maskBin32)
    netBin = Bin32ToBinBytes(netBin32)
    netDecimal = ipToDecimal(netBin) # Network Adress in decimal bytes : a.b.c.d

    return hostDecimal, maskDecimal, netDecimal

def Read_full_IP(decIP_maskID):
	a, b, c, d = decIP_maskID.split('.')
	d, ID_mask = d.split('/')
	IP_host_Dec = a + '.' + b + '.' + c + '.' + d

	# All Adresses count
	n_adresses = 2**(32-int(ID_mask))

	# Reading the Host IP in base 2 / for calculation later
	a = toBinary(int(a))
	b = toBinary(int(b))
	c = toBinary(int(c))
	d = toBinary(int(d))

	IP_host_Bin = a + "." + b + "." + c + "." + d # Host IP in binary bytes
	IP_host_Bin32 = a + b + c + d # Host IP in 32 bits format - used for calculation
	
	# Reading the 32bits format of a mask IP from a integer || ID_mask --> func: numToIP --> mask in 32bits 
	maskBin32 = readMask(ID_mask)
	print(maskBin32)
	# The Mask IP in Binary format in bytes: a.b.c.d
	maskBin = Bin32ToBinBytes(maskBin32) # Mask IP in binary format
	# Mask in decimal a.b.c.d format
	maskDec = ipToBinary(maskBin)

	
	# Calculation of the network IP --> function "netIP_Bin" --> returns a.b.c.d in binary
	IP_net_Bin32 = netBin32(IP_host_Bin32, maskBin32)
	IP_net_Bin = Bin32ToBinBytes(IP_net_Bin32)
	IP_net_Dec = ipToDecimal(IP_net_Bin) # Network Adress in decimal bytes : a.b.c.d

	return hostDec, maskDec, netDec, n_adresses

# Function that turns all the 32 bits of an IP adress to the usual a bytes (a.b.c.d) / Binary Version
def Bin32ToBinBytes(IP_Bin32):
	a = IP_Bin32[0:8]
	b = IP_Bin32[8:16]
	c = IP_Bin32[16:24]
	d = IP_Bin32[24:32]

	return a + '.' + b + '.' + c + '.' + d



def Num_Adresses(n):
	return 2**n

def eNumBin(n):
	i=0
	for i in range(n):
		print(toBinary(i))
		i+=1