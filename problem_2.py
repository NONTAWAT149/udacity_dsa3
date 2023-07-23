def rotated_array_search(num_list, target):
    """
    To find index of target value on list of numbers
    :param num_list
    :param target
    :return: index of target value
    """

    if not isinstance(target, int):
        raise Exception("target must be integer")

    left_index = 0
    right_index = len(num_list) - 1

    while right_index >= left_index:

        mid_index = (right_index + left_index)//2

        # if target index is found, return the index
        if target == num_list[mid_index]:
            return mid_index

        else:

            # For left side is sorted
            if num_list[left_index] <= num_list[mid_index]:
                if (target > num_list[mid_index]) or (target < num_list[left_index]):
                    left_index = mid_index + 1
                else:
                    right_index = mid_index - 1

            # For right side is sorted
            else:
                if (target < num_list[mid_index]) or (target > num_list[right_index]):
                    right_index = mid_index - 1
                else:
                    left_index = mid_index + 1

    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])

    # edge case test 1
    #rotated_array_search([6, 7, 8, 1, 2, 3, 4], None)

    # edge case test 2
    #rotated_array_search([6, 7, 8, 1, 2, 3, 4], "string")

