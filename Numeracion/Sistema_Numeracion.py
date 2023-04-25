def decimal_wrapper(decimal, base):
    convertion = ''
    while decimal >= base:
        resto = decimal % base
        if resto > 9:
            resto = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}.get(resto)
        decimal = decimal // base
        convertion = str(resto) + convertion
    if decimal > 9:
        decimal = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}.get(decimal)
    convertion = str(decimal) + convertion
    return convertion

def bin_oct_hex_to_decimal_wrapper(number, base):
    number = str(number)
    num_length = len(number)
    decimal = 0
    for i in range(num_length):
        # print(f'decimal = {decimal} + ({number[i]} x 2^{num_length-1-i})')
        if number[i] in 'ABCDEF':
            block = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}.get(number[i])
        else:
            block = int(number[i])
        decimal += block * base**(num_length-i-1)
    return decimal


#Decimal a otras bases#

def decimal_a_binario(decimal):
    return decimal_wrapper(decimal, 2)

def decimal_a_octal(decimal):
    return decimal_wrapper(decimal, 8)

def decimal_a_hexadecimal(decimal):
    return decimal_wrapper(decimal,16)

#Binario a otras bases#

def binario_a_decimal(binario):
    return bin_oct_hex_to_decimal_wrapper(binario, 2)

def binario_a_octal(binario):
    return decimal_a_octal(binario_a_decimal(binario))

def binario_a_hexadecimal(binario):
    return decimal_a_hexadecimal(binario_a_decimal(binario))

#Octal a otras bases#

def octal_a_decimal(octal):
    return bin_oct_hex_to_decimal_wrapper(octal, 8)

def octal_a_binario(octal):
    return decimal_a_binario(octal_a_decimal(octal))

def octal_a_hexadecimal(octal):
    return decimal_a_hexadecimal(octal_a_decimal(octal))

#Hexadecimal a otras bases#

def hexadecimal_a_decimal(hexadecimal):
    return bin_oct_hex_to_decimal_wrapper(hexadecimal, 16)

def hexadecimal_a_binario(hexadecimal):
    return decimal_a_binario(hexadecimal_a_decimal(hexadecimal))

def hexadecimal_a_octal(hexadecimal):
    return decimal_a_octal(hexadecimal_a_decimal(hexadecimal))