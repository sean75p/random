def list_to_int(value):
    """
    function to remove leading zeros from a list and turn it into an int
    example: [0, 0, 1, 1, 1] will return 111
    :param value: list
    :return: int
    """
    value = map(str, value)
    value = ''.join(value)
    value = int(value)
    return value


def int_to_list(value):
    """
    Transform an int into a list of single digits; this is used for binary number mathematics
    example: 1001 will return [1, 0, 0, 1]
    :param value: int
    :return: list
    """
    value = [int(i) for i in str(value)]
    return value


if __name__ == "__main__":
    output = list_to_int([0, 0, 1, 0, 1])
    print(output)
    print(type(output))
    output = int_to_list(101)
    print(output)
    print(type(output))
