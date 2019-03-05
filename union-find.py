class UnionFind:

    def __init__(self, items):
        n = len(items)
        self.items = []
        self.item_to_index = {items[i]:i for i in range(n)}
        self.parent = [i for i in range(n)]
        self.weight = [0 for i in range(n)]
        
        
    def union(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        
        # weighted union
        if self.weight[ra] > self.weight[rb]:
            self.parent[rb] = ra
            self.weight[rb]+= self.weight[ra]
        else:
            self.parent[ra] = rb
            self.weight[ra]+= self.weight[rb]
        
        # quick union
        # self.parent[ra] = rb
        
        
    def find(self, a, b):
        return self.root(a) == self.root(b)
    
    def root(self, a):
        a = self.item_to_index[a]
        while self.parent[a] != a:
            # path compression
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a
     
def example1():
    items = ['a', 'b', 'c', 'd']
    
    u = UnionFind(items)
    print('Items: ', items)
    
    print('find  \t a - b: ', u.find('a','b'))
    
    print('union \t a - b')
    u.union('a', 'b')
    
    print('find  \t a - b: ', u.find('a','b'))
    print('union \t c - d')
    u.union('c', 'd')
    print('find  \t a - d: ', u.find('a','d'))
    print('union  \t b - c: ')
    u.union('b', 'c')
    
    print('find  \t a - d: ', u.find('a','d'))
    

if __name__ == "__main__":
    
    example1()
    