#-*-coding:utf-8-*- 
# author :  王顺章
# school :  nuaa
# description   二叉树最大深度

'''递归'''

def maxDepth(self, root):
    if not root:
        return 0
    left=self.maxDepth(root.left)
    right=self.maxDepth(root.right)
    return max(left,right)+1



'''迭代'''
def maxDepth(self, root):
    stack = []
    if root is not None:
        stack.append((1, root))
    depth = 0
    while stack != []:
        current_depth, root = stack.pop()
        if root is not None:
            depth = max(depth, current_depth)
            stack.append((current_depth + 1, root.left))
            stack.append((current_depth + 1, root.right))
    return depth