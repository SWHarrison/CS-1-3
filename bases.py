def base_ten_to_two(n):

    max_power_of_two = 1

    while max_power_of_two <= n/2:

        max_power_of_two *= 2

    remainder = n

    binary_string = ""
    while(remainder != 0):

        if(max_power_of_two <= remainder):
            binary_string += "1"
            remainder -= max_power_of_two

        else:
            binary_string += "0"

        max_power_of_two = max_power_of_two //2

    while(max_power_of_two >= 1):
        binary_string += "0"
        max_power_of_two = max_power_of_two //2

    return binary_string

def base_ten_to_sixteen(n):

    max_power_of_16 = 1

    while max_power_of_16 <= n/16:

        max_power_of_16 *= 16

    remainder = n

    hex_string = ""
    while(remainder > 0):

        digit = remainder // max_power_of_16
        if(digit < 10):
            hex_string += str(digit)
        else:
            hex_string += chr(digit+87)

        remainder -= max_power_of_16 * digit
        max_power_of_16 = max_power_of_16 //16

    while(max_power_of_16 >= 1):
        hex_string += "0"
        max_power_of_16 = max_power_of_16 //16

    return hex_string

#Takes a number in base 10 and returns a string representation of that number in the given base
def encode(num,base):

    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    assert num >= 0, 'number is negative: {}'.format(number)

    max_power_of_x = 1

    while max_power_of_x <= (num/base):

        max_power_of_x *= base

    remainder = num

    string = ""

    while remainder > 0:

        digit = remainder // max_power_of_x
        if(digit < 10):
            string += str(digit)
        else:
            string += chr(digit+87)

        remainder -= max_power_of_x * digit
        max_power_of_x = max_power_of_x // base

    while(max_power_of_x >= 1):
        string += "0"
        max_power_of_x = max_power_of_x //base

    return string

def decode(digits,base):

    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    total_base_10 = 0
    base_power = 1
    for i in range(1,len(digits)+1):

        digit = digits[-i]
        if(ord(digit) >= 97):
            digit = ord(digit) - 87
        elif(ord(digit) >= 65):
            digit = ord(digit) - 55
        total_base_10 += base_power * int(digit)
        base_power *= base

    return total_base_10

def convert(digits, base1, base2):

     # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    total_base_10 = decode(digits,base1)
    new_digits = encode(total_base_10,base2)

    return new_digits



#print(base_ten_to_two(8))
#print(base_ten_to_sixteen(263))
#print(base_10_to_x(255,3))
decode("r5",36)
print(convert("11111101",9,10))
