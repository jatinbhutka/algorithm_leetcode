# Lowest Common Ancestor in a Binary Tree (Not Binary Search Tree, Both are different):
# Given a binary tree (not a binary search tree) and two values say n1 and n2, 
# write a program to find the least common ancestor.


# The LCA of n1 and n2 in T is the shared ancestor of n1 and n2 
# that is located farthest from the root.


"""
Computation of lowest common ancestors may be useful, 
for instance, as part of a procedure for determining 
the distance between pairs of nodes in a tree: 
    the distance from n1 to n2 can be computed as the 
    distance from the root to n1, plus the distance from
    the root to n2, minus twice the distance from the 
    root to their lowest common ancestor.
    
    
# Method 1 (By Storing root to n1 and root to n2 paths):
Following is simple O(n) algorithm to find LCA of n1 and n2.
1) Find path from root to n1 and store it in a vector or array.
2) Find path from root to n2 and store it in another vector or array.
3) Traverse both paths till the values in arrays are same. 
    Return the common element just before the mismatch.
"""

# Binary tree Node:
class Node():
    # Constructor to create a new binary node
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None
    
# Finds the path from root node to given root of the tree. 
# Stores the path in a list path[], returns true if path  
# exists otherwise false     
def findPath(root, path, n):
    
    # Baes Case 
    if root is None:
        return False

    # Store this node is path vector. The node will be 
    # removed if not in path from root to k 
    path.append(root.val)

    # See if the k is same as root's key 
    if root.val == n:
        return True
    
    # Check if k is found in left or right sub-tree 
    if (root.left != None and findPath(root.left, path, n)) or (root.right != None and findPath(root.right, path, n)):
        return True

    # If not present in subtree rooted with root, remove 
    # root from path and return False 
    path.pop()
    return False
    

# Returns LCA if node n1 , n2 are present in the given 
# binary tre otherwise return -1 
def findLCA(root, n1, n2):
    if root is None:
        return False

    # To store paths to n1 and n2 fromthe root     
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2. 
    # If either n1 or n2 is not present , return -1  
    if not findPath(root, path1, n1):
        return -1
    if not findPath(root, path2, n2):
        return -1

    # Compare the paths to get the first different value  
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]


# Driver program to test above function 
# Let's create the Binary Tree shown in above diagram 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7)         

print "LCA(4, 5) = %d" %(findLCA(root, 4, 99,)) 
print "LCA(4, 6) = %d" %(findLCA(root, 4, 6)) 
print "LCA(3, 4) = %d" %(findLCA(root,3,4)) 
print "LCA(2, 4) = %d" %(findLCA(root,2, 4)) 
