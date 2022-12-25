# set removes duplicates
# IN BST EACH NODE HAVE AT MOST TWO CHILDREN
# IN BST ELEMETS MAINTAIN SOME KIND OF ORDER
# SEARCH COMPLEXITY O(log n)
# INSERTION COMPLEXITY O(log n)
# SEARCHING/TRAVERSING THROUGH A TREE --> BFS(BREADTH FIRST SEARCH)
#                                     --> DFS(DEPTH FIRST SEARCH)
# IN ORDER,PRE ORDER,POST ORDER TRAVERSAL

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def build_child_node(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:
            if self.left:
                self.left.build_child_node(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.build_child_node(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

        # Visit Left subtree, then Root node and finally Right subtree
        # Visit Left subtree, then Root node and finally Right subtree

    def in_order_traversal(self):  # Left - Root - Right
        elements = []
        # Getting all elements of the Left Subtree
        if self.left:
            elements += self.left.in_order_traversal()  # Recursively get all the elements of the left subtree and add them into the list
        elements.append(self.data)  # Adding the root node to the list
        # Getting all elements of the Right Subtree
        if self.right:
            elements += self.right.in_order_traversal()  # Recursively get all the elements of the right subtree and add them into the list
        return elements

    # Get all elements from the Root node then the left subtree and finanally the Right subtree
    def pre_order_traversal(self):  # Root - Left - Right
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()  # Recursively get all the elements of the left subtree and add them into the list
        if self.right:
            elements += self.right.pre_order_traversal()  # Recursively get all the elements of the right subtree and add them into the list
        return elements  # get the Root node element

    # Get all elements from the Right subtree then the left subtree and finally the Root node
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()  # Recursively get all the elements of the left subtree and add them into the list
        if self.right:
            elements += self.right.post_order_traversal()  # Recursively get all the elements of the right subtree and add them into the list
        elements.append(self.data)  # Get the Root node element
        return elements


    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum


def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.build_child_node(elements[i])
    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    # numbers = [15,12,7,14,27,20,23,88 ]

    numbers_tree = build_tree(numbers)
    print("Input numbers:", numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("search:", numbers_tree.search(18))
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())
