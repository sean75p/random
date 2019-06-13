
def logical_xor(a, b):
    if a == b:
        return 0
    else:
        return 1

def binary_to_decimal(binary):
    sum = 0
    number = str(binary)
    number_of_bits = len(number)

    for i in number:
        subtotal = int(i) * (2**(number_of_bits-1))
        number_of_bits = number_of_bits - 1
        sum = sum + subtotal

    return sum

#print(binary_to_decimal(1011000))

def find_exponent(num):
    # find the highest exponent for 2^x
    exponent = 0
    while num >= 2**exponent:
        exponent += 1
    return exponent

def decimal_to_binary_old(num):

    exp = find_exponent(num)
    remainder = num - 2** (exp-1)
    number = 10 ** (exp - 1)
    print(number, remainder)

    while remainder > 0:
        exp = find_exponent(remainder)
        remainder = remainder - 2**(exp-1)
        number = number + 10**(exp-1)

    return number

def decimal_to_binary(num):

    number = 0
    remainder = num

    while remainder != 0:
        exp = find_exponent(remainder)
        remainder = remainder - 2**(exp-1)
        number = number + 10**(exp-1)

    return number

def calculate_xor_and_shift(key, data_word, remainder=0):
    length_of_data_word = len(str(data_word))
    zero_list = [0] * length_of_data_word
    number_of_bits = len(str(key))

    # add n-1 extra zeros to the end of the data word
    data_word = data_word * 10 ** (number_of_bits - 1) + remainder

    # turn the data word into a list of strings
    data_word = [int(x) for x in str(data_word)]

    k = 0
    while data_word[:-3] != zero_list:

        j = k
        xor_result = []

        for i in (str(key)):
            # let's compare the data word against the key and do an XOR operation
            output = logical_xor(int(i), data_word[j])
            xor_result.append(output)
            data_word[j] = output
            j = j + 1

        if xor_result == [0, 0, 0, 0]:
            # if all the XOR values are zeros, move to the next 1 value
            k = k + 4
        elif (xor_result[1] == 0 and xor_result[2] == 0):
            # if the 0th, 1st, and 2nd bits are zero, move 3 spots to the next '1'
            k = k + 3
        elif xor_result[1] == 0:
            # if the 0th and 1st bits are zero, move 2 spots to the next '1'
            k = k + 2
        else:
            # default is to move one spot to the next '1'
            k += 1

        print('nth iteration:', k)
        print('data_word:', data_word)
        print('xor result:', xor_result)
        print('------------------------')

    print('data word final answer:', data_word)
    print('data word without remainder', data_word[:-3])
    check_sum_remainder = data_word[length_of_data_word:]
    print('remainder:', check_sum_remainder)
    return check_sum_remainder

def convert_list_to_number(value):
    """
    function to convert a list of numbers into a number
    leading zeros in the list will be omitted
    for example [0, 0, 1, 0, 1] will return 101
    :param value: list
    :return: number: int
    """
    value.reverse()
    number = 0
    for i, j in enumerate(value):
        number = number + j*(10**i)
    return number


if __name__ == "__main__":
    # generator polynomial
    # x^3 + X + 1 ==>> 1011

    # key = 1011
    # original_data_word = 11010011101100

    data_word = 11010011101100
    key = 1011

    check_sum_remainder = calculate_xor_and_shift(key, data_word)
    print('--------------------------------------------------------------------')

    rem = convert_list_to_number(check_sum_remainder)
    final_remainder = calculate_xor_and_shift(key, data_word, remainder = rem)

    if final_remainder == [0] * len(final_remainder):
        print('Your checksum is correct!')
