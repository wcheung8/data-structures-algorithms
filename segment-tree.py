import math


class SegmentTree:

    def __init__(self, items, operator, lazy=True):
        self.items = items
        self.n = len(items)

        # allocate tree array
        maxHeight = math.ceil(math.log(self.n, 2))
        self.segmentTree = [-1] * (2 ** (maxHeight + 1) - 1)
        self.operator = operator

        # allocate lazy update array
        self.lazy = lazy
        self.lazyBit = [False] * (2 ** (maxHeight + 1) - 1)

        # build tree
        self.buildTree(0, self.n - 1, 0)

    def buildTree(self, start, end, index):
        # range contains only one element, return self
        if start == end:
            self.segmentTree[index] = self.items[start]
            return self.segmentTree[index]

        # recurse after splitting
        mid = (start + end) // 2

        left = self.buildTree(start, mid, 2 * index + 1)
        right = self.buildTree(mid + 1, end, 2 * index + 2)

        # calculate node value
        self.segmentTree[index] = self.operator(left, right)

        return self.segmentTree[index]

    def query(self, queryStart, queryEnd):
        return self._query(queryStart, queryEnd, 0, self.n - 1, 0)

    def _query(self, queryStart, queryEnd, start, end, index):
        if queryStart <= start and queryEnd >= end:
            return self.segmentTree[index]

        if end < queryStart or start > queryEnd:
            return 0

        mid = (start + end) // 2
        left = self._query(queryStart, queryEnd, start, mid, 2 * index + 1)
        right = self._query(queryStart, queryEnd, mid + 1, end, 2 * index + 2)

        return self.operator(left, right)

    def update(self, i, value):
        return self._update(i, value, 0, self.n - 1, 0)

    def _update(self, i, value, start, end, index):
        if start == end:
            self.items = value
            self.segmentTree[index] = value
            return value

        if i < start or i > end:
            return self.segmentTree[index]

        mid = (start + end) // 2

        left = self.segmentTree[2 * index + 1]
        right = self.segmentTree[2 * index + 2]

        if i <= mid:
            left = self._update(i, value, start, mid, 2 * index + 1)
        else:
            right = self._update(i, value, mid + 1, end, 2 * index + 2)

        self.segmentTree[index] = self.operator(left, right)
        return self.segmentTree[index]


def example1():
    items = [1, 3, 5, 7, 9, 11, 1, 1, 2, 5]
    st = SegmentTree(items, lambda x, y: x + y)
    print(st.query(0, 3))
    st.update(0, 100)
    print(st.query(0, 3))


if __name__ == "__main__":
    example1()
