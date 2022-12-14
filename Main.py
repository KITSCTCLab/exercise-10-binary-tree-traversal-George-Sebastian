""" binary tree """

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def insert(root, new_value) -> BinaryTreeNode:
    
    if not root:
        root = BinaryTreeNode(new_value)
        return root
    if new_value < root.data:
         if root.left_child:
            insert(root.left_child, new_value)
         else:
            root.left_child = BinaryTreeNode(new_value)
    else:
        if root.right_child:
            insert(root.right_child, new_value)
        else:
            root.right_child = BinaryTreeNode(new_value)

def inorder(root) -> None:
    if root is None:
        return
    inorder(root.left_child)
    print(root.data, end = " ")
    inorder(root.right_child)

def preorder(root) -> None:
    if root is None:
        return
    print(root.data, end = " ")
    preorder(root.left_child)
    preorder(root.right_child)

def postorder(root) -> None:
    if root is None:
        return
    postorder(root.left_child)
    postorder(root.right_child)
    print(root.data, end = " ")


    
# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
