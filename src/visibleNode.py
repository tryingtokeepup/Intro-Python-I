class Node:
    def __init__(self, x, l=None, r=None):
        self.data = x
        self.l = l
        self.r = r


def Helper(T, maxInt):

    if (T == None):
        return 0

    count = 0

    if T.data >= maxInt:
        count += 1
        maxInt = T.data

    return count + Helper(T.l, maxInt) + Helper(T.r, maxInt)


tree1 = Node(5, Node(3, Node(20), Node(21)), Node(10, Node(1)))
tree2 = Node(8, Node(2, Node(8), Node(7)), Node(6))

print(Helper(tree1, 0))
print(Helper(tree2, 0))
