# _*_ coding: utf-8 _*_
from collections import OrderedDict


# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
# class Solution(object):
#     def __init__(self):
#         self.m = {}
#
#     def rob(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root == None:
#             return 0
#         elif self.m.has_key(root):
#             return self.m[root]
#         elif root.left == None and root.right == None:
#             self.m[root] = root.val
#             return root.val
#         else:
#             a = 0
#             a += root.val
#             if root.left != None:
#                 a += self.rob(root.left.left)
#                 a += self.rob(root.left.right)
#             if root.right != None:
#                 a += self.rob(root.right.left)
#                 a += self.rob(root.right.right)
#             # self.m[root] = a
#
#             b = 0
#             if self.m.has_key(root.left):
#                 b += self.m[root.left]
#             else:
#                 self.m[root.left] = self.rob(root.left)
#                 b += self.m[root.left]
#             if self.m.has_key(root.right):
#                 b += self.m[root.right]
#             else:
#                 self.m[root.right] = self.rob(root.right)
#                 b += self.m[root.right]
#             # b = self.rob(root.left) + self.rob(root.right)
#             self.m[root] = max(a, b)
#             return max(a, b)
def fun(n):
    l = []
    for i in range(n):
        l.append(i)
    return l


def fun1():
    i = 0
    while i < 10:
        yield i
        i += 1


def main():
    # i = fun1()
    dic = OrderedDict()

    dic[1] = "xxx"
    dic[2] = "yyy"
    dic[3] = "vvv"
    dic[4] = "bbb"

    k, v = dic.popitem(False)
    print k, v
    for i in dic:
        print i

    # print i


if __name__ == "__main__":
    print __name__
    main()
    # m = {}
    # m.setdefault('a', []).append("33")

    # l = fun(10)
    # print l

    # for i in fun1(10):
    # i = fun1(10)
    # i = fun1(10)
