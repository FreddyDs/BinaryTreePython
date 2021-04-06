class TreeNode:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

# add - Public function
# _add - Private function
    def add(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._add(value, self.root)

    def _add(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = TreeNode(value)
            else:
                self._add(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = TreeNode(value)
            else:
                self._add(value, cur_node.right)
        else:
            print(f"{value} - Already exists")
            return

# remove - Public function
# _remove - Private function
    def remove(self, value):
        self.root = self._remove(value, self.root)

    def _remove(self, value, cur_node):
        if not cur_node:
            print("Value not found!")
            return None
        if cur_node.value == value:
            if not cur_node.left and not cur_node.right:
                cur_node = None
                return cur_node
            elif not cur_node.left and cur_node.right:
                cur_node = cur_node.right
                return cur_node
            elif not cur_node.right and cur_node.left:
                cur_node = cur_node.left
                return cur_node
            else:
                pnt = cur_node.right
                while pnt.left:
                    pnt = pnt.left
                cur_node.value = pnt.value
                cur_node.right = self._remove(cur_node.value, cur_node.right)

        elif value < cur_node.value:
            cur_node.left = self._remove(value, cur_node.left)
        elif value > cur_node.value:
            cur_node.right = self._remove(value, cur_node.right)
        return cur_node

    #size - Public function
#_size - Private function
    def size(self):
        return self._size(self.root)

    def _size(self, cur_node):
        if not cur_node:
            return 0
        value_to_return = 1
        value_to_return += self._size(cur_node.right)
        value_to_return += self._size(cur_node.left)
        return value_to_return

    def depth(self):
        return self._depth(self.root)

    def _depth(self, cur_node):
        if not cur_node:
            return 0
        ldepth = 1 + self._depth(cur_node.left)
        rdepth = 1 + self._depth(cur_node.right)
        if ldepth > rdepth:
            return ldepth
        return rdepth


# Counting left nodes only
# count_left_nodes - Public Function
# _count_left_nodes - Private Function
    def count_left_nodes(self):
        print(self._count_left_nodes(self.root))

    def _count_left_nodes(self, cur_node):
        if not cur_node:
            return 0
        value = 0
        if cur_node.left:
            value += 1
        value += self._count_left_nodes(cur_node.left) + self._count_left_nodes(cur_node.right)
        return value

# Count Empty nodes only
# count_empty - Public Function
# _count_empty - Private Fucntion

    def count_empty(self):
        print(self._count_empty(self.root))
    def _count_empty(self, cur_node):
        if not cur_node:
            return 1
        return self._count_empty(cur_node.right) + self._count_empty(cur_node.left)


# Sum of the Depth
# depth_sum - Public Function
# _depth_sum - Private Function

    def depth_sum(self):

        print(self._depth_sum(self.root, 1))

    def _depth_sum(self, cur_node, level):
        if not cur_node:
            return 0
        value = level
        value *= cur_node.value
        value += self._depth_sum(cur_node.left, level+1) + self._depth_sum(cur_node.right, level+1)
        return value

#Count Even Branches
# count_even_branches - Public function
# _count_even_branches - Private function

    def count_even_branches(self):
        print(self._count_even_branches(self.root))
    def _count_even_branches(self, cur_node)  :
        if not cur_node:
            return 0
        if not cur_node.left and not cur_node.right:
            return 0
        value = 0
        if cur_node.value % 2 == 0:
            value += 1
        value += self._count_even_branches(cur_node.left) + self._count_even_branches(cur_node.right)
        return value

#Print Level
#print_level - Public Function
#print_level - Private Function

    def print_level(self, level):
        if level < 1:
            print("Level cannot be negative")
            return
        self._print_level(self.root, level, 1)
    def _print_level(self, cur_node, level, cur_level):
        if not cur_node:
            return
        if cur_level != level:
            self._print_level(cur_node.left, level, cur_level+1)
            self._print_level(cur_node.right, level, cur_level+1)
        else:
            print(cur_node.value)

# Print leaves
# print_leaves - Public function
# _print_leaves - Private function

    def print_leaves(self):
        if not self.root:
            print("No leaves")
        else:
            self._print_leaves(self.root)

    def _print_leaves(self, cur_node):
        if not cur_node:
            return
        if not cur_node.left and not cur_node.right:
            print(cur_node.value)
        else:
            self._print_leaves(cur_node.right)
            self._print_leaves(cur_node.left)

# Is it the tree full
# is_full - Public Function
# _is_full - Private Function

    def is_full(self):
        return self._is_full(self.root)
    def _is_full(self, cur_node):
        if not cur_node.left and not cur_node.right:
            return True
        elif cur_node.left and cur_node.right:
            return self._is_full(cur_node.left) and self._is_full(cur_node.right)
        else:
            return False

# Are these trees equal?
# equals - Public Method
# _equals - Private Method

    def equals(self, t):
        print(self._equals(self.root, t.root))

    def _equals(self, cur_node, t):
        if not cur_node and not t:
            return True
        if not cur_node or not t:
            return False
        value = cur_node.value == t.value
        value = self._equals(cur_node.left, t.left) == self._equals(cur_node.right, t.right)
        return value

# Double the positive nodes
# double_positives - Public Function
# _double_positives - Private Function

    def double_positives(self):
        self._double_positives(self.root)

    def _double_positives(self, cur_node):
        if not cur_node:
            return
        if cur_node.value > 0:
            cur_node.value *= 2
        self._double_positives(cur_node.right)
        self._double_positives(cur_node.left)

# Number the nodes!
# number_nodes - Public Function
# _number_nodes - Private Function

    def number_nodes(self):
        self._number_nodes(self.root, 1)

    def _number_nodes(self, cur_node, n):
        if not cur_node:
            return n
        cur_node.value = n
        value = self._number_nodes(cur_node.left, n+1)
        return self._number_nodes(cur_node.right, value)

# Remove leaves
# remove_leaves - Public Function
# _remove_leaves - Private Function

    def remove_leaves(self):
        self.root = self._remove_leaves(self.root)

    def _remove_leaves(self, cur_node):
        if not cur_node:
            return
        if not cur_node.left and not cur_node.right:
            return None
        cur_node.left = self._remove_leaves(cur_node.left)
        cur_node.right = self._remove_leaves(cur_node.right)
        return cur_node

# Complete the level
# complete_to_level - Public Function
# _complete_to_level - Private Function

    def complete_to_level(self, level):
        if level < 1:
            print("Level cannot be negative")
            return
        self._complete_to_level(self.root, level, 1)

    def _complete_to_level(self, cur_node, level, cur_level):
        if not cur_node:
            return
        if cur_level != level:
            self._complete_to_level(cur_node.left, level, cur_level + 1)
            self._complete_to_level(cur_node.right, level, cur_level + 1)
        else:
            if not cur_node.left:
                cur_node.left = TreeNode(-1)
            if not cur_node.right:
                cur_node.right = TreeNode(-1)

#Trim the tree
# trim - Public Function
# _trim - Private Function

    def trim(self, min, max):
        self.root = self._trim(self.root, min, max)
    def _trim(self, cur_node, min, max):
        if not cur_node:
            return None
        if cur_node.value < min:
            return self._trim(cur_node.right, min, max)
        elif cur_node.value > max:
            return self._trim(cur_node.left, min, max)
        cur_node.left = self._trim(cur_node.left, min, max)
        cur_node.right = self._trim(cur_node.right, min, max)
        return cur_node

# Tighten the tree
# tighten - Public Function
# _tighten - Private Function

    def tighten(self):
        self.root = self._tighten(self.root)

    def _tighten(self, cur_node):
        if not cur_node:
            return
        if not cur_node.right and not cur_node.left:
            return cur_node

        if not cur_node.right:
            return self._tighten(cur_node.left)
        if not cur_node.left:
            return self._tighten(cur_node.right)

        cur_node.left = self._tighten(cur_node.left)
        cur_node.right = self._tighten(cur_node.right)
        return cur_node
# Combine 2 trees in a specific way
# combine_with - Public method
# _combine_with - Private Method

    def combine_with(self, t):
        tree3 = BinarySearchTree()
        tree3.root = self._combine_with(self.root, t.root, tree3.root)
        return tree3

    def _combine_with(self, cur_node,  t, t3):
        if not cur_node and not t:
            return None
        if cur_node and not t:
            t3 = TreeNode(1)
            t3.left = self._combine_with(cur_node.left, None, t3.left)
            t3.right = self._combine_with(cur_node.right, None, t3.right)
        if not cur_node and t:
            t3 = TreeNode(2)
            t3.left = self._combine_with(None, t.left, t3.left)
            t3.right = self._combine_with(None, t.right, t3.right)
        if cur_node and t:
            t3 = TreeNode(3)
            t3.left = self._combine_with(cur_node.left, t.left, t3.left)
            t3.right = self._combine_with(cur_node.right, t.right, t3.right)
        return t3

# Tree to a in order list, what?
# in_order_list - Public Method
# _in_order_list - Private Method

    def in_order_list(self):
        return self._in_order_list(self.root, [])

    def _in_order_list(self, cur_node, lst):
        if not cur_node:
            return
        if not cur_node.left and not cur_node.right:
            lst.append(cur_node.value)
            return

        self._in_order_list(cur_node.left, lst)
        lst.append(cur_node.value)
        self._in_order_list(cur_node.right, lst)

        return lst

# Even Levels
# even_levels - Public Function
# _even_levels - Private Function

    def even_levels(self):
        self.root = self._even_levels(self.root, 1)

    def _even_levels(self, cur_node, level):
        if not cur_node:
            return
        if level % 2 != 0 and not cur_node.left and not cur_node.right:
            return None

        cur_node.left = self._even_levels(cur_node.left, level + 1)
        cur_node.right = self._even_levels(cur_node.right, level + 1)
        return cur_node

# Make Perfect
# perfect - Public Function
# _perfect - Private Function

    def perfect(self):
        if self.depth() == 0:
            self.root = TreeNode(0)
            return
        if self.depth() == 1:
            print("Nothing to perfect!")
            return

        self.root = self._perfect(self.root, 1, self.depth())

    def _perfect(self, cur_node, cur_level, depth):
        if cur_level == depth:
            return cur_node
        if not cur_node.left:
            cur_node.left = TreeNode(0)
        if not cur_node.right:
            cur_node.right = TreeNode(0)

        cur_node.left = self._perfect(cur_node.left, cur_level + 1, depth)
        cur_node.right = self._perfect(cur_node.right, cur_level + 1, depth)
        return cur_node

# Matches
# matches - Public Function
# _matches - Private Function
    def matches(self, t2):
        return self._matches(self.root, t2.root)

    def _matches(self, cur_node, t2):
        if not cur_node and not t2 or (not cur_node or not t2) or cur_node.value != t2.value:
            return 0
        return 1 + self._matches(cur_node.left, t2.left) + self._matches(cur_node.right, t2.right)

    def _traverse(self, cur_node):
        lst = []
        if not cur_node:
            return [None]
        if cur_node.left is None:
            lst.append(None)
        else:
            lst.append(self._traverse(cur_node.left))
        lst.append(cur_node.value)
        if cur_node.right is None:
            lst.append(None)
        else:
            lst.append(self._traverse(cur_node.right))
        return lst

    def represent(self):
        print(self._traverse(self.root))







tree = BinarySearchTree()
tree2 = BinarySearchTree()


tree.add(50)
tree.add(45)
tree.add(38)
tree.add(40)

tree2.add(50)
tree2.add(45)
tree2.add(55)
tree2.add(56)
tree2.add(38)
tree2.add(40)
print(tree.matches(tree2))
# tree2.add(6)

# for i in range(1, 11):
#     if i == 5:
#         continue
#     tree.add(i)
#     tree2.add(i)
# tree2.number_nodes()
# tree.add(6)
# tree.add(4)
# tree.add(7)
# tree.add(-2)
# tree.add(0)
# tree.add(5)
# tree.add(140)
# tree.add(160)
# tree.add(155)
# tree.add(130)

# print(tree.is_full())
# tree.remove(100)
# print(tree.size())
# tree.remove(6)
#
# print(tree.size())