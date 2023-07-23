## Udacity Data Structure and Algorithm - Project 3 Basic Algorithm Problems

### Problem 1: Square Root of an Integer

#### Code Design:
Binary search is implemented to find square value. With nature of Binary search algorithm, it provides O(log(n)) for time complexity.

#### Efficiency:
- Time complexity: O(log(n)), which n is input value. Bigger input value is bigger n.
- Space complexity: O(1), only input value, starting value, ending value, and middle values are stored.

---------------

### Problem 2: Search in a rotated sorted array

#### Code Design:
Binary search is implemented to find index of target value in list.

#### Efficiency:
- Time complexity: O(log(n)), which n is number of values in list.
- Space complexity: O(n), which n is number of values in list.

---------------

### Problem 3: Rearrange Array Digits

#### Code Design:
Quick sort algorithm is implemented to sort array. Bubble sort is not considered because it takes time complexity O(n). 

#### Efficiency:
- Time complexity: O(nlog(n)), which n is number of values in list.
- Space complexity: O(n), which n is number of values in list.

---------------

### Problem 4: Dutch National Flag Problem

#### Code Design:
To sort 0, 1, 2 value, 0 will be moved to the left, 2 will move to the right. 1 stays at the middle of array. Single traversal process is chosen to move value in list.

#### Efficiency:
- Time complexity: O(n), which n is number of values in list.
- Space complexity: O(n), which n is number of values in list.

---------------

### Problem 5: Autocomplete with Tries

#### Code Design:
Nodes with tree structure is chosen to implement Autocomplete with Tries. It provides ability to store character of word in each node level.

#### Efficiency:
- Time complexity: O(n), which n is number of characters.
- Space complexity: O(n), which n is number of characters.

---------------

### Problem 6: Unsorted Integer Array

#### Code Design:
Single traversal is used to compare each value of list to existing min and max value.

#### Efficiency:
- Time complexity: O(n), which n is number of value in list.
- Space complexity: O(n), which n is number of value in list.

---------------

### Problem 7: Request Routing in a Web Server with a Trie

#### Code Design:
Nodes with tree structure is chosen to implement Autocomplete with Tries. It provides ability to store sub path of http path.

#### Efficiency:
- Time complexity: O(n), which n is number of characters.
- Space complexity: O(n), which n is number of characters.