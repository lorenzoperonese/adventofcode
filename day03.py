#!/usr/bin/env python3

def solveFirst(f):
    count = 0
    for line in f:
        first = max(line[ : -1])
        index = line.index(first)
        second = max(line[index + 1 : ])
        count += int(str(first) + str(second))
    print('First star:', count)

def solveSecond(f):
    count = 0
    for line in f:
        joltage = []
        for i in range(12):
            joltage.append(max(line[ : (i - 11 if i != 11 else None)]))
            index = line.index(joltage[-1])
            line = line[index + 1 : ]
        count += int("".join([str(el) for el in joltage]))
    print('Second star', count)

def main():
    f = [[int(el) for el in list(line.strip())] for line in open('./inputs/03.txt', 'r').readlines()]
    solveFirst(f)
    solveSecond(f)
    
if __name__ == '__main__':
    main()
