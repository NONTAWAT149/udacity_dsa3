def sort_012(input_list):
    """
    Function to sort 0, 1, 2 values
    value 0 moves to the left of list
    value 2 moves to the right of list
    value 1 stays at the middle of list

    Input: input list of number 0, 1, 2
    Return: Sorted values
    """

    # initialise pointer of position of value 0 and 2
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1
    traversal_index = 0

    while traversal_index <= next_pos_2:

        # Check if receive unexpected values
        if input_list[traversal_index] not in (0, 1, 2):
            return "Unexpected input value received"

        # If the pointer value is 0
        if input_list[traversal_index] == 0:

            # Switch value between traversal_index and next_pos_0
            input_list[traversal_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0

            # Move the position of pointers
            next_pos_0 += 1
            traversal_index += 1

        # If the pointer value is 2
        elif input_list[traversal_index] == 2:

            # Switch value between traversal_index and next_pos_2
            input_list[traversal_index] = input_list[next_pos_2]
            input_list[next_pos_2] = 2

            # Move the position of pointer
            next_pos_2 -= 1

        # If the pointer value is 1
        else:

            # Move the position of pointer
            traversal_index += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

    # Normal test
    print('normal test: ', sort_012([0, 0, 2, 2, 2, 1, 0, 1, 2, 0, 2]))

    # edge case test 1
    print('edge case test 1: ', sort_012([]))

    # edge case test 2
    print('edge case test 2: ', sort_012([0, 0, 2, 2, 2, 1, None, 1, 2, 0, 2]))

    # edge case test 3
    print('edge case test 3: ', sort_012([None]))