#!/usr/bin/env python3

from math import prod

def solveFirst(f):
    # transpose matrix (by values)
    f_t = [[line.split()[i] for line in f] for i in range(len(f[0].split()))]
    res = 0
    for line in f_t:
        if line[-1] == '+':
            res += sum([int(val) for val in line[:-1]])
        else:
            res += prod([int(val) for val in line[:-1]])
    print('First star:', res)

def solveSecond(f):
    # transpose matrix (by chars) without the symbols' row
    f_t = [[line[i] for line in f[:-1]] for i in range(len(f[0]))]
    symbols = f[-1].split()
    i, res = 0, 0
    # the starting value is the identity, 0 for the sum and 1 for the multiplication
    tmp = int(symbols[0] == '*')
    for line in f_t:
        if "".join(line).strip() == '':
            res += tmp
            i += 1
            tmp = int(symbols[i] == '*')
        else:
            val = int("".join(line))
            if symbols[i] == '+':
                tmp += val
            else:
                tmp *= val
    res += tmp
    print('Second star:', res)

def main():
    f = [line[:-1] for line in open('./inputs/06.txt', 'r').readlines()]
    solveFirst(f)
    solveSecond(f)

if __name__ == '__main__':
    main()

