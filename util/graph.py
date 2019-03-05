from collections import defaultdict
def Graph(class):
    
    # adjacency matrix representation
    def __init__(self, vals, adj, type='matrix'):
        
        if type == 'matrix':
            self.adj = [[None] * len(vals) for i in range(len(vals))]
            self.vals = vals
        elif type == 'list':
            self.adj = defaultdict(set())
            self.vals = vals
            for a, b in adj:
                self.adj[a].add(b)
                self.adj[b].add(a)
    