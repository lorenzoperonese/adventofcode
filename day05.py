#!/usr/bin/env python3

def updateList(fresh, s, e):
    for i, (s2, e2) in enumerate(fresh):
        if s <= e2 and s2 <= e:
            fresh.pop(i)
            updateList(fresh, min(s, s2), max(e, e2))
            return
    fresh.append([s, e])

def solveFirst(f):
    count = 0
    fresh = []
    for i, line in enumerate(f):
        if line == '':
            f = f[i + 1 : ]
            break
        fresh.append(line.split('-'))
    for line in f:
        for s, e in fresh:
            if int(s) <= int(line) <= int(e):
                count += 1
                break
    print('First star:', count)

def solveSecond(f):
    fresh = []
    for line in f:
        if line == '':
            break
        updateList(fresh, *[int(el) for el in line.split('-')])
    res = sum([e - s + 1 for s, e in fresh])
    print('Second star:', res)

def main():
    f = [line.strip() for line in open('./inputs/05.txt', 'r').readlines()]
    solveFirst(f)
    solveSecond(f)
    
if __name__ == '__main__':
    main()
