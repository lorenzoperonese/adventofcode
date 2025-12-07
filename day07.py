#!/usr/bin/env python3

class TachyonManifold:
    
    def __init__(self, f):
        self.graph = {} 

        # Graph build
        f_t = [[line[i] for line in f] for i in range(len(f[0]))] # transpose matrix
        self.addSplit('S', f'{len(f_t)//2}_2')
        for i in range(len(f_t)):
            splits = [m for m, val in enumerate(f_t[i]) if val == '^'] # find all '^'
            for match in splits:
                for k in [-1, 1]: # check the row above and the one below
                    if '^' in f_t[i + k][match + 1 : ]:
                        # add edges
                        dst_index = f_t[i + k][match + 1 : ].index('^') + match + 1
                        name_s = f"{str(i)}_{str(match)}"
                        name_d = f"{str(i + k)}_{str(dst_index)}"
                    else:
                        # connect final nodes to the 'E' node
                        name_s = f"{str(i)}_{str(match)}"
                        name_d = 'E' 
                    self.addSplit(name_s, name_d)

    def addSplit(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, [])

    def returnGraph(self):
        return self.graph

    def splitsUsed(self): # Breadth-first search
        reachables = set()
        queue = ['S']
        while queue != []:
            val = queue.pop(0)
            childs = list(self.graph[val])
            for el in childs:
                if(el not in reachables and el != 'E'):
                    queue.append(el)
                    reachables.add(el)
        return len(reachables)

    def countTimelines(self, src, memo): # Depth-first search with cache
        if src == 'E':
            return 1
        if src in memo:
            return memo[src]
        total = 0
        for adj in self.graph[src]:
            total += self.countTimelines(adj, memo)
        memo[src] = total
        return total

    def findAllPaths(self):
        memo = {}
        return self.countTimelines('S', memo)

def solveFirst(f):
    graph = TachyonManifold(f)
    print('First star:', graph.splitsUsed())

def solveSecond(f):
    graph = TachyonManifold(f)
    print('Second star:', graph.findAllPaths())

def main():
    f = [line.strip() for line in open('./inputs/07.txt', 'r').readlines()]
    solveFirst(f)
    solveSecond(f)
    
if __name__ == '__main__':
    main()
