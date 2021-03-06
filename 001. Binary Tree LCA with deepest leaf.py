'''
Problem: 

给一个Binary Tree, 求最深节点的最小公共父节点。最深的节点可以只有一个，那就返回节点本身。

Follow-up:
1. Recursive and Iterative (指向母点的指针)
2. Each node has multiple children

* Similar to 236. Lowest Common Ancestor of a Binary Tree 

Example 1:

         1
        /  \
       2    3 
           /  \
          5    6
   最深的节点是5 和 6. 他们的公共节点是3。return 3。
 
 
Example 2:

         1
        /  \
       2    3 
      /    /  \
     4    5    6

    return 1。
'''

'''
Solution 1: Recursive

对于root，每个孩子遍历一遍，如果孩子深度大于max，就更新max，然后返回的是孩子，如果等于max，说明有多个孩子深度一样，那么返回root

Time complexity: O(n), Space complexity: O(h), height of the tree
'''

def findLCARecursive(TreeNode root):
    if not root:
        return (None, 0)   # tuple(node, depth)

    left = findLCARecursive(root.left)
    right = findLCARecursive(root.right)
    depth = max(left[1], right[1])+1

    # 两边一样深,root 是公共
    if left[1] == right[1]:
        return (root, depth)
    # 左边深
    elif left[1] > right[1]:
        return (left[0], depth)
    # 右边深
    else:
        return (right[0], depth)
        
        
'''
Solution 2: Iterative
 
Use a hashmap to record the parent of every node. 
Do BFS and record the most left node and most right node of every level.
Then we have most left and right node of last level.
Search into the hashmap util we find the same parent which is the lca.
Time complexity: O(n), space complexity: O(n) -- hashmap has all the node
''' 

def findLCAIterative(TreeNode root):
    if not root:
        return None


    # BFS traversal and record child to parent map
    childToParent = {}
    q = deque()
    q.append(root)
    while len(q):
        size = len(q)
        for i in range(size):
            cur = q.popleft()
            # record the most left and right node of last level
            if i == 0: left = cur
            if i == size - 1: right = cur
            if cur.left:
                q.append(cur.left)
                childToParent[left] = cur
            if cur.right:
                q.append(cur.right)
                childToParent[right] = cur

    # Search from left most child and right most child go up 
    # util we find the same parent which is the lca.
    while left != right:
        left = childToParent[left]
        right = childToParent[right]

    return left



'''
Solution 3: With multiple children

Time complexity: O(n), Space complexity: O(h), height of the tree
'''

def findLCAMulti(TreeNode root):

    if not root:
        return (None,0)    # tuple(node, depth)

    next = []
    for child in root.children:
        next.append(findLCAMulti(child))

    deepest, deepest2 = (None, 0), (None, 0)
    for result in next:
        if result[1] > deepest[1]:
            deepest2 = deepest
            deepest = result
    depth = 1 + deepest[1]

    if deepest[1] == deepest2[1]:
        return (root, depth)
    else: 
        return (deepest[0], depth)

