#!/usr/bin/env python3

from shapely.geometry import Polygon, box # is this cheating?

def solveFirst(f):
    res = 0
    for i in range(len(f)):
        for j in range(i + 1, len(f)):
            res = max(res, (1 + abs(f[i][0] - f[j][0])) * (1 + abs(f[i][1] - f[j][1])))
    print('First star:', res)

def solveSecond(f):
    poly = Polygon(f)
    res = 0
    for i in range(len(f)):
        for j in range(i + 1, len(f)):
            x1, y1, x2, y2 = f[i] + f[j]
            rect = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
            if poly.contains(rect):
                res = max(res, (1 + abs(f[i][0] - f[j][0])) * (1 + abs(f[i][1] - f[j][1])))
    print('Second star', res)


def main():
    f = [[int(el.strip()) for el in line.split(',')] for line in open('./inputs/09.txt', 'r').readlines()]
    solveFirst(f)
    solveSecond(f)
    
if __name__ == '__main__':
    main()

