from collections import defaultdict


class Node:

    def __init__(self, value):
        self.value = value
        self.valid = False
        self.children = {}


class Trie:

    def __init__(self, items):
        self.items = items
        self.buildTrie()

    def buildTrie(self):

        self.root = Node(None)

        for w in self.items:
            self.insert(w)

    def insert(self, word):

        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]

        curr.valid = True

    def query(self, word):

        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.valid


def example1():
    items = ["hi", "hill", "hello"]
    t = Trie(items)

    t.insert('the')
    print(t.query('hell'))
    print(t.query('hello'))
    t.insert('hell')
    print(t.query('hell'))


if __name__ == "__main__":
    example1()
