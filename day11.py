#!/usr/bin/env python3

class CableManagement:

    def __init__(self, f):
        self.graph = {}
        for line in f:
            self.graph[line[0:3]] = line[5:].split(' ')

    def dfs(self, s, e, intermediate, memo):
        if s == e:
            return intermediate == []
        if s in memo and memo[s][1] == intermediate:
            return memo[s][0]
        if s in intermediate:
            intermediate.pop(intermediate.index(s))
        total = 0
        for adj in self.graph[s]:
            total += self.dfs(adj, e, intermediate.copy(), memo)
        memo[s] = [total, intermediate]
        return total

    def countPaths(self, s, e, intermediate=[]):
        memo = {} # [isValidPath, [intermediate nodes not found yet]]
        return self.dfs(s, e, intermediate, memo)

def solveFirst(f):
    s = CableManagement(f)
    print('First star:', s.countPaths('you', 'out'))
    
def solveSecond(f):
    s = CableManagement(f)
    print('Second star:', s.countPaths('svr', 'out', ['dac', 'fft']))

def main():
    f = [line.strip() for line in open('./inputs/11.txt', 'r').readlines()]
    solveFirst(f)
    solveSecond(f)
    
if __name__ == '__main__':
    main()
