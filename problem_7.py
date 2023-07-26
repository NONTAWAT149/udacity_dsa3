## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        """
        Initialize the node with children as before,
        plus a handler
        """

        self.children = {}
        self.handler = None

    def insert(self, handler):
        """
        # Insert the node as before
        """

        # add node if it does not exist.
        if handler not in self.children:
            self.children[handler] = RouteTrieNode()


## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        """
        # Initialize the trie with an root node and a handler,
        this is the root path or home page node
        """

        self.root = RouteTrieNode()

    def insert(self, handler, path):
        """
        Similar to our previous example you will want to recursively add nodes
        Make sure you assign the handler to only the leaf (deepest) node of this path
        """

        # Initialise current node
        current_node = self.root

        # Add element from path to current node
        for element in path:
            current_node.insert(element)
            current_node = current_node.children[element]

        # Add handler at the end of child node
        current_node.handler = handler

    def find(self, path):
        """
        Starting at the root, navigate the Trie to find a match for this path
        Return the handler for a match, or None for no match
        """

        # Initialise current node
        current_node = self.root

        # Loop to find path
        for element in path:

            # Return None if path not found
            if element not in current_node.children:
                return None
            # Set new current node to move to next node
            current_node = current_node.children[element]

        # return handler (path if found)
        return current_node.handler


## The Router class will wrap the Trie and handle
class Router:

    def __init__(self, handler, handler_not_found = "handler_not_found"):
        """
        Create a new RouteTrie for holding our routes
        You could also add a handler for 404 page not found responses as well!
        """

        self.route = RouteTrie()
        self.route.insert(handler, "/") # handler and path
        self.not_found = handler_not_found

    def add_handler(self, route, handler):
        """
        Add a handler for a path
        You will need to split the path and pass the pass parts
        as a list to the RouteTrie
        """

        self.route.insert(handler, self.split_path(route))

    def lookup(self, route):
        """
        lookup path (by parts) and return the associated handler
        you can return None if it's not found or
        return the "not found" handler if you added one
        bonus points if a path works with and without a trailing slash
        e.g. /about and /about/ both return the /about handler
        """
        if route in (None, []):
            return "not found handler"

        return self.route.find(self.split_path(route)) or self.not_found


    def split_path(self, route):
        """
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        """

        if len(route) == 1:
            return ["/"]
        else:
            return route.strip("/").split("/")


if __name__ == '__main__':
    ## Here are some test cases and expected outputs you can use to test your implementation

    ## create the router and add a route
    router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    ## some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one

    # normal case
    print('normal case: ', router.lookup("/home/about/"))

    # edge case test 1
    print('edge case test 1: ', router.lookup("/home/about/."))

    # edge case test 2
    print('edge case test 2: ', router.lookup("/home/about."))

    # edge case test 3
    print('edge case test 3: ', router.lookup(""))

    # edge case test 4
    print('edge case test 4: ', router.lookup(None))

