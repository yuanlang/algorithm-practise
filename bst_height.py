# Function Description
# Complete the getHeight or height function in the editor. 
# It must return the height of a binary tree as an integer.
# getHeight or height has the following parameter(s):
# root: a reference to the root of a binary tree.
# Note - The Height of binary tree with single node is taken as zero.
# input(stdin)
# 7
# 3 5 2 1 4 6 7
# Expected Output
# 3
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
    def print_tree(self, node):
        if node == None:
            return
        if node != None:
            print(node.info)
        self.print_tree(node.left)
        self.print_tree(node.right)


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''


def height_old(root):
    l = 0
    r = 0
    if root == None:
        return 0
    if root.left != None:
        l = 1 + height(root.left)
    if root.right != None:
        r = 1 + height(root.right)
    return 1 + max(l, r)

# Note:
# when root == None, it need to return -1, not 0
# Because when only have a root tree's height is 0
def height(root):
    if root == None:
        return -1
    return 1 + max(height(root.left), height(root.right))

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])
tree.print_tree(tree.root)

print(height(tree.root))
