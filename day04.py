#!/usr/bin/env python3

def solveFirst(f):
    count = 0
    for i in range(1, len(f) - 1):
        for j in range(1, len(f[i]) - 1):
            if f[i][j] == '@':
                adj = 0
                for k in range(-1, 2):
                    for h in range(-1, 2):
                        adj += int(f[i + h][j + k] == '@')
                count += int(adj <= 4)
    print('First star:', count)
    
def solveSecond(f):
    count = 0
    while True:
        new_count = count
        for i in range(1, len(f) - 1):
            for j in range(1, len(f[i]) - 1):
                if f[i][j] == '@':
                    adj = 0
                    for k in range(-1, 2):
                        for h in range(-1, 2):
                            adj += int(f[i + h][j + k] == '@')                       
                    if adj <= 4:
                        new_count += 1
                        f[i][j] = '.'
        if new_count == count:
            break
        count = new_count
    print('Second star:', count)
 

def main():
    # add one level of padding to avoid OutOfBound errors
    f = [['.'] + list(line.strip()) + ['.'] for line in open('./inputs/04.txt', 'r').readlines()]
    f = [['.'] * len(f[0])] + f + [['.'] * len(f[0])]
    solveFirst(f)
    solveSecond(f)
    
if __name__ == '__main__':
    main()
