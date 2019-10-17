# l = [3, 4, 8, 10, 1, 2, 5]
# #
# #
# # def func(n, val):
# #     if n <= 0:
# #         return l[n] + val
# #     elif n == 1:
# #         return val + max(l[0], l[1])
# #     else:
# #         a = func(n-1, val)
# #         b = func(n-2, val + l[n])
# #         return max(a, b)
# #
# # print func(len(l)-1, 0)

# l = [13,11,8,12,7,26,6,14,15,8,12,7,13,24,11]
l = [3, 2, 3, None, 3, None, 1]


class Node():
    def __init__(self, _v):
        self.v = _v
        self.l = None
        self.r = None

    def left_link(self, node):
        self.l = node

    def right_link(self, node):
        self.r = node

    def left(self):
        return self.l

    def right(self):
        return self.r

    def __repr__(self):
        s = ""
        s = "val:" + str(self.v)
        # s += " left:" + str(self.l)
        # s += " right:" + str(self.r)
        return s


tree = []
count = 0
for i in range(1, 3):
    row = []
    for j in range(i):
        row.append(Node(l[count]))
        count += 1
    tree.append(row)


for i in range(len(tree) - 1):
    for j in range(len(tree[i])):
        if tree[i][j].v is not None:
            tree[i][j].left_link(tree[i + 1][j])
            tree[i][j].right_link(tree[i + 1][j + 1])

for i in range(len(tree)):
    for j in range(len(tree[i])):
        print tree[i][j]
        print tree[i][j].l
        print tree[i][j].r
        print "_______________"


def func(node):
    if node is None:
        return 0
    elif node.l is None:
        if node.r is not None:
            return func(node.r)
    elif node.r is None:
        if node.l is not None:
            return func(node.l)
    elif node.r is None and node.l is None:
        return node.v
    else:
        a = 0
        a += node.v
        if node.l is not None:
            if node.l.l is not None:
                a += func(node.l.l)
            if node.l.r is not None:
                a += func(node.l.r)
        if node.r is not None:
            if node.r.l is not None:
                a += func(node.r.l)
            if node.r.r is not None:
                a += func(node.r.r)
        #
        b = 0
        if node.l is not None:
            b += func(node.l)
        if node.r is not None:
            b + func(node.r)

        return max(a, b)
        pass


# def func(node, val):
#     if node.l == None:
#         return val + node.v
#     else:
#         a = func(node.l, val + node.v)
#         b = func(node.r, val + node.v)
#         return max(a, b)
#
root = tree[0][0]
val = 0
# print func(root)

# print tree[2][1]
# for i in tree:
#     for j in i:
#         print j
#     print "\n"
