import random

def get_min_max(ints):
    """
    To find max and min value of values in list
    :param ints:
    :return: tuple(min, max)
    """

    # Initialise values of min and max
    min = ints[0]
    max = ints[0]

    # Loop for each value and check for max and min value
    for value in ints:

        # Check if receive unexpected values
        if not isinstance(value, int):
            return "Unexpected value received"

        # if new min is found, update the min
        if value < min:
            min = value

        # if new max is found, update the max
        if value > max:
            max = value

    return (min, max)


if __name__ == '__main__':

    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    # edge case test 1
    print('edge case test 1: ', get_min_max([1, "string", 5, 6, 0]))

    # edge case test 2
    print('edge case test 2: ', get_min_max([1, 3, None, 6, 0]))