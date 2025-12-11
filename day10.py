#!/usr/bin/env python3

from itertools import combinations
from functools import reduce  
from scipy.optimize import linprog

def solveFirst(f):
    res = 0
    for line in f:
        l = line.split(' ')
        lights = int(l[0][1 : -1].replace('.', '0').replace('#', '1')[ : : -1], base=2)
        buttons = []
        for el in l[1 : -1]:
            vec = 0
            for val in el[1 : -1].split(','):
                vec += 2 ** int(val)
            buttons.append(vec)
        i, found = 1, False
        while not found:
            for c in combinations(buttons, i):
                if reduce(lambda x, y: x ^ y, c) == lights:
                    found = True
            i += 1
        res += i - 1
    print('First star:', res)

# min z = x1 + x2 + ... + xn
# x1[0] + x2[0] + ... + xn[0] = j[0]
# ...

def solveSecond(f):
    res = 0
    for line in f:
        l = line.split(' ')
        joltage = l[-1][1 : -1].split(',')
        buttons = []
        for el in l[1 : -1]:
            b = [0 for _ in range(len(joltage))]
            for val in el[1 : -1].split(','):
                b[int(val)] = 1
            buttons.append(b)
        c = [1 for _ in range(len(buttons))] # x1, ..., xn coefficients in the equation
        A = [el for el in zip(*buttons)] # transposed buttons matrix 
        res += linprog(c, A_eq=A, b_eq=joltage, integrality=1).fun
    print('Second star:', int(res))

def main():
    f = [line.strip() for line in open('./inputs/10.txt', 'r').readlines()]
    solveFirst(f)
    solveSecond(f)
    
if __name__ == '__main__':
    main()

