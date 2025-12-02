#!/usr/bin/env python3

def isInvalid(val):
    l = len(str(val))
    divisors = []
    for i in range(1, l//2 + 1):
        if l % i == 0:
            divisors.append(i)
    for div in divisors:

        # split the value in substrings with length = div, 
        # then convert the list in a set and check if the length of the set is 1
        # (this works because the set structure has no duplicates)

        substr = [str(val)[i : i + div] for i in range(0, l, div)]
        if len(set(substr)) == 1:
               return True
    return False

def solveFirst(f):
    sum = 0
    for val in f:
        for i in range(int(val[0]), int(val[1]) + 1):
            l = len(str(i))
            if l % 2 == 0 and str(i)[ : l // 2] == str(i)[l // 2 : ]:
                sum += i
    print('First star:', sum)

def solveSecond(f):
    sum = 0
    for val in f:
        for i in range(int(val[0]), int(val[1]) + 1):
            if isInvalid(i):
                sum += i
    print('Second star:', sum)

def main():
    f = [line.split('-') for line in open('./inputs/02.txt', 'r').readline().split(',')]
    solveFirst(f)
    solveSecond(f)
    
if __name__ == '__main__':
    main()
