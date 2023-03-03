from Node import AVLNode

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node: AVLNode):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node: AVLNode):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, node: AVLNode):
        left_node = node.left
        right_of_left = left_node.right

        left_node.right = node
        node.left = right_of_left

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        left_node.height = max(self.get_height(left_node.left), self.get_height(left_node.right)) + 1

        return left_node

    def rotate_left(self, node: AVLNode):
        right_node = node.right
        left_of_right = right_node.left

        right_node.left = node
        node.right = left_of_right

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        right_node.height = max(self.get_height(right_node.left), self.get_height(right_node.right)) + 1

        return right_node

    def insert_node(self, node: AVLNode, key):
        if node is None:
            self.root = AVLNode(key)
        elif key < node.key:
            node.left = self.insert_node(node.left, key)
        else:
            node.right = self.insert_node(node.right, key)

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def get_min_value_node(self, node: AVLNode):
        current = node

        # Find the leftmost leaf node
        while current.left is not None:
            current = current.left

        return current


    def delete_node(self, node: AVLNode, key):
        if node is None:
            return node

        elif key < node.key:
            node.left = self.delete_node(node.left, key)

        elif key > node.key:
            node.right = self.delete_node(node.right, key)

        else:
            # Node has one or no children
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # Node has two children, get the inorder successor
            temp = self.get_min_value_node(node.right)

            # Copy the inorder successor's value to this node
            node.key = temp.key

            # Delete the inorder successor
            node.right = self.delete_node(node.right, temp.key)

        # If the tree has only one node, return
        if node is None:
            return node

        # Update height of the current node
        node.height = 1 + max(self.get_height(node.left),
                            self.get_height(node.right))

        # Get the balance factor of this node
        balance = self.get_balance(node)

        # Left Left Case
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)

        # Left Right Case
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Right Case
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)

        # Right Left Case
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
