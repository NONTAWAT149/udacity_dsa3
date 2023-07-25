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
- Space complexity: O(n), which n is number of values in list. If there are 10 numbers in list, so n is 10.

---------------

### Problem 3: Rearrange Array Digits

#### Code Design:
Quick sort algorithm is implemented to sort array. Bubble sort is not considered because it takes time complexity O(n). 

#### Efficiency:
- Time complexity: O(nlog(n)), which n is number of values in list.
- Space complexity: O(n), which n is number of values in list. If there are 10 numbers in list, so n is 10.

---------------

### Problem 4: Dutch National Flag Problem

#### Code Design:
To sort 0, 1, 2 value, 0 will be moved to the left, 2 will move to the right. 1 stays at the middle of array. Single traversal process is chosen to move value in list.

#### Efficiency:
- Time complexity: O(n), which n is number of values in list.
- Space complexity: O(n), which n is number of values in list. If there are 10 numbers in list, so n is 10.

---------------

### Problem 5: Autocomplete with Tries

#### Code Design:
Nodes with tree structure is chosen to implement Autocomplete with Tries. It provides ability to store character of word in each node level.

To implement Autocomplete with Tries, 2 classes are implemented such as TrieNode() and Trie().
(1) TrieNode(): It is mainly used to store and find node of tree. Node is defined as children. 
- insert() method stores new node in children in dictionary format. 
- suffixes() method finds children node of current node. It uses "recursive function" to find children nodes until reach the end of node.
(2) Trie(): It is used to build tree structure of nodes. 
- insert() method adds characters into tree and define the end of path (leaf = True).
- find() method points to the current position of current node.

#### Efficiency:
- Time complexity: O(n), which n is number of characters.
- Space complexity: O(n), which n is number of characters.

---------------

### Problem 6: Unsorted Integer Array

#### Code Design:
Single traversal is used to compare each value of list to existing min and max value.

#### Efficiency:
- Time complexity: O(n), which n is number of value in list.
- Space complexity: O(n), which n is number of value in list. If there are 10 numbers in list, so n is 10.

---------------

### Problem 7: Request Routing in a Web Server with a Trie

#### Code Design:
Nodes with tree structure is chosen to implement Autocomplete with Tries. It provides ability to store sub path of http path.

To implement equest Routing in a Web Server with a Trie, 3 classes are implemented such as RouteTrieNode(), RouteTrie(), and Router().
(1) RouteTrieNode(): It is mainly used to store node of tree. Node is defined as children. 
- insert() method stores new node in children in dictionary format. 
(2) RouteTrie(): It is used to build tree structure of nodes. 
- insert() method adds characters into tree and define the end of path (handler).
- find() method points to the current position of current node.
(3) Router(): It is used to manage Trie and handle.
- add_handler() to add handler to path
- lookup() to search for path
- split_path() to split path

#### Efficiency:
- Time complexity: O(n), which n is number of path elements.
- Space complexity: O(n), which n is number of path elements.