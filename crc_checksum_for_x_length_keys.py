from utils import int_to_list
from utils import list_to_int


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


def convert_list_to_number(value):
    """
    function to convert a list of numbers into a number
    :param value: list
    :return: number: int
    """
    value.reverse()
    number = 0
    for i, j in enumerate(value):
        number = number + j*(10**i)
    return number


def calculate_xor_and_shift(key, data_word, remainder=0):
    # calculate constants
    length_of_data_word = len(str(data_word))
    zero_list = [0] * length_of_data_word
    key_bit_length = len(str(key))
    zero_pad_length = key_bit_length - 1

    # add n-1 extra zeros to the end of the data word
    data_word = data_word * 10 ** (zero_pad_length) + remainder

    # turn the data word into a list of strings
    data_word = [int(x) for x in str(data_word)]

    k = 0
    while data_word[:-(zero_pad_length)] != zero_list:
        print(data_word[:-(zero_pad_length)])

        j = k
        xor_result = []

        string_key = str(key)

        for i in (string_key):

            # let's compare the data word against the key and do an XOR operation
            output = logical_xor(int(i), data_word[j])
            print(i, j)
            xor_result.append(output)
            data_word[j] = output
            j = j + 1

        xor1 = list_to_int(xor_result)
        length_xor1 = len(xor_result)
        print('xor1:', xor1)
        how_many_zeros_removed = length_xor1 - len(int_to_list(xor1))
        print('zeros removed', how_many_zeros_removed)

        if xor_result == [0] * key_bit_length:
            # if all the XOR values are zeros, move to the right by the key bit length
            k = k + key_bit_length
        else:
            # else move to the right by how many leading zeros there are in the XOR'ed list
            k = k + how_many_zeros_removed

        print('nth iteration:', k)
        print('data_word:', data_word)
        print('xor result:', xor_result)
        print('------------------------')

    print('data word final answer:', data_word)
    print('data word without remainder', data_word[:-3])
    check_sum_remainder = data_word[length_of_data_word:]
    print('remainder:', check_sum_remainder)
    return check_sum_remainder


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
    final_remainder = calculate_xor_and_shift(key, data_word, remainder=rem)

    if final_remainder == [0] * len(final_remainder):
        print('Your checksum is correct!')

