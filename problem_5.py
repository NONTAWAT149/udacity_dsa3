from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

## Represents a single node in the Trie

class TrieNode:
    def __init__(self):
        """
        Initialize this node in the Trie
        """

        self.children = {}
        self.isleaf = False

    def insert(self, char):
        """
        Add a child node in this Trie
        """

        # add new char if it does not exists
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        """
        Recursive function that collects the suffix for
        all complete words below this point
        """

        # Initialise output list
        suffix_list = []

        # Add suffix to output list if found
        if self.isleaf and suffix != '':
            suffix_list.append(suffix)

        # Stop loop when end of child nodes
        if len(self.children) == 0:
            return suffix_list

        # Recursion to add more suffix
        for char in self.children:
            suffix_list.extend(self.children[char].suffixes(suffix=suffix + char))

        return suffix_list


## The Trie itself containing the root node and insert/find functions

class Trie:
    def __init__(self):
        """
        Initialize this Trie (add a root node)
        """

        self.root = TrieNode()

    def insert(self, word):
        """
        Add a word to the Trie
        """

        # set root node of current node
        current_node = self.root

        # loop to add new child node
        for char in word:

            # add new child node if is it not exist
            if char not in current_node.children:
                current_node.children[char] = TrieNode()

            # set current node
            current_node = current_node.children[char]

        # define end of child node
        current_node.isleaf = True

    def find(self, prefix):
        """
        Find the Trie node that represents this prefix
        """

        if not isinstance(prefix, str):
            return False

        if prefix == '':
            return False

        # define current node
        current_node = self.root

        # loop to get current node from prefix
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node


if __name__ == '__main__':

    print('CASE 1: Normal case')
    MyTrie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        MyTrie.insert(word)

    # normal case
    print('normal case - string a: ', ', '.join(MyTrie.find('a').suffixes()))
    # edge case test 1
    print('edge case test 1.1: ', MyTrie.find('antt/'))
    # edge case test 2
    print('edge case test 1.2: ', MyTrie.find(None))


    print('CASE 2: Edge Case 1 - empty list')
    MyTrie2 = Trie()
    wordList = []
    for word in wordList:
        MyTrie2.insert(word)

    # normal case
    print('normal case : ', MyTrie2.find(''))
    # edge case test 1
    print('edge case test 2.1: ', MyTrie2.find([]))
    # edge case test 2
    print('edge case test 2.2: ', MyTrie2.find(None))


    print('CASE 3: Edge Case 2 - first element with empty space')
    MyTrie3 = Trie()
    wordList = ['', 'bert', 'gpt3', 'gpt4']
    for word in wordList:
        MyTrie3.insert(word)

    # normal case
    print('normal case - string g: ', ', '.join(MyTrie3.find('g').suffixes()))
    # edge case test 1
    print('edge case test 3.1: ', MyTrie2.find([]))
    # edge case test 2
    print('edge case test 3.2: ', MyTrie2.find(None))