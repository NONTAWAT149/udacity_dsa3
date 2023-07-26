def square_value(value):
    """
    To calculate square value by using binary search
    :param value
    :return: answer (square value)
    """

    if not isinstance(value, int):
        raise Exception("input data must be integer")

    start = 0
    end = value

    while start <= end:
        mid = int((start + end)/2)

        if (mid*mid) == value:
            answer = mid
            break

        if (mid*mid) < value:
            start = mid + 1
            answer = mid

        else:
            end = mid - 1

    return answer

if __name__ == '__main__':
    print("Pass" if (3 == square_value(9)) else "Fail")
    print("Pass" if (0 == square_value(0)) else "Fail")
    print("Pass" if (4 == square_value(16)) else "Fail")
    print("Pass" if (1 == square_value(1)) else "Fail")
    print("Pass" if (5 == square_value(27)) else "Fail")

    # normal test
    print('normal test:')
    print(square_value(144))

    # edge case test 1 (float number)
    #print('edge case test 1 (float number):')
    #square_value(9.3)

    # edge case test 2 (String)
    #print('edge case test 2 (String):')
    #square_value("string")

    # edge case test 3 (long number)
    print('edge case test 3 (long number):')
    print(square_value(123400000000))
