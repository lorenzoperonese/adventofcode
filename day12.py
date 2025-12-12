#!/usr/bin/env python3

def solveFirst(f):
    count = 0
    shapes = []
    trees = []
    i = 0
    while True:
        if i == len(f):
            break
        if f[i][1] == ':':
            shapes.append(f[i+1:i+4])
            i += 5
        else:
            l = [el.strip() for el in f[i].split(':')]
            trees.append([[int(el) for el in l[0].split('x')], [int(el) for el in l[1].split(' ')]])
            i += 1
    for t in trees:
        # unexpectedly this works, check if there are enough 3x3 squares on the floor
        # thank god no need to rotate or pack shapes (apparently this is an NP-complete problem)
        count += sum(t[1]) <= (t[0][0] // 3) * (t[0][1] // 3)
    print('First star:', count)

def solveSecond(f):
    print('The second star is free today! Merry Christmas!')

def main():
    f = [line.strip() for line in open('./inputs/12.txt', 'r').readlines()]
    solveFirst(f)
    solveSecond(f)
    
if __name__ == '__main__':
    main()
