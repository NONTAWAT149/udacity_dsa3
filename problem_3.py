def sort_a_little_bit(items, begin_index, end_index):
    """
    Support function to sort values in list by using pivot
    :param items:
    :param begin_index:
    :param end_index:
    :return: pivot_index, (partially) sorted items
    """

    # Initialise index
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    # Go loop until pivot index is left index
    while (pivot_index != left_index):

        # set item value (from left index) to replace at pivot index
        item = items[left_index]

        # If pivot value is already bigger than item value, do nothing
        # Then move the position of left index
        # Continue next loop
        if item <= pivot_value:
            left_index += 1
            continue

        # Move value before pivot value to left index
        items[left_index] = items[pivot_index - 1]

        # Move pivot value to the position of in front of pivot index
        items[pivot_index - 1] = pivot_value

        # Move item value to pivot index
        # This is the largest value
        items[pivot_index] = item

        # Move the position of pivot
        pivot_index -= 1

    return pivot_index, items

def sort_all(items, begin_index, end_index):
    """
    Support function to loop sorting process
    :param items:
    :param begin_index:
    :param end_index:
    :return: sorted items
    """

    # Stop the (sort) process if end_index <= begin_index
    if end_index <= begin_index:
        return

    # Sort values using pivot
    pivot_index, items = sort_a_little_bit(items, begin_index, end_index)
    #print('debug pivot_index: {}, items : {}'.format(pivot_index, items))

    # Sort values before pivot index (left side)
    sort_all(items, begin_index, pivot_index - 1)

    # Sort value after pivot index (right side)
    sort_all(items, pivot_index + 1, end_index)

    return items

def quicksort(items):
    """
    Support function to call sorting function
    :param items:
    :return: sorted items
    """
    return sort_all(items, 0, len(items) - 1)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list == None or input_list == []:
        return None

    # Sort values
    input_list = quicksort(input_list)

    # Initialise values
    sum_list = list()
    first_sum_number = ''
    second_sum_number = ''

    while len(input_list) > 0:

        # Select the biggest value for first number
        first_value = input_list.pop(-1)
        first_sum_number += str(first_value)

        if len(input_list) == 0:
            # Stop the process if no value in input list
            break
        else:
            # Select the remaining biggest value for second number
            second_value = input_list.pop(-1)
            second_sum_number += str(second_value)

    # Add first number and second number to list
    sum_list.append(int(first_sum_number))
    sum_list.append(int(second_sum_number))

    return sum_list


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list == None or input_list == []:
        return None

    # Sort values
    input_list = quicksort(input_list)

    # Initialise values
    sum_list = list()
    first_sum_number = ''
    second_sum_number = ''

    while len(input_list) > 0:

        # Select the biggest value for first number
        first_value = input_list.pop(-1)
        first_sum_number += str(first_value)

        if len(input_list) == 0:
            # Stop the process if no value in input list
            break
        else:
            # Select the remaining biggest value for second number
            second_value = input_list.pop(-1)
            second_sum_number += str(second_value)

    # Add first number and second number to list
    sum_list.append(int(first_sum_number))
    sum_list.append(int(second_sum_number))

    return sum_list
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

    # normal case
    print('normal case: ', rearrange_digits([9, 3, 4, 6, 8, 7]))

    # edge case test 1
    print('edge case test 1: ', rearrange_digits(None))

    # edge case test 2
    print('edge case test 2: ', rearrange_digits([]))
