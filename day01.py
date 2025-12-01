#!/usr/bin/env python3

def solveFirst(f):
    pos = 50
    count = 0
    for line in f:
        direction = 1 if line[0] == 'R' else -1
        steps = int(line[1:])
        pos = (pos + direction * steps) % 100
        if pos == 0:
            count += 1
    print('First star:', count)

"""
def solveSecondBruteforce(f):
    pos = 50
    count = 0
    for line in f:
        direction = 1 if line[0] == 'R' else -1 
        steps = int(line[1:])
        for _ in range(steps):
            pos = (pos + direction) % 100
            if pos == 0:
                count += 1
    print('Second star:', count)
"""

def solveSecond(f):

    # there are two edge cases when we go left, 
    # caused by the integer division of a negative number

    pos = 50
    count = 0
    for line in f:
        direction = 1 if line[0] == 'R' else -1
        steps = int(line[1:])

        # edge case 1, if the initial position is 0, that 0 should not count
        # e.g. start at 0, L50:
        # pos = -50, abs(-50 // 100) = 1, but we did not touch the 0!
        if pos == 0 and direction == -1:
            count -= 1

        pos += direction * steps
        count += abs(pos // 100)
        pos %= 100

        # edge case 2, if the final position is 0, that 0 should count
        # e.g start at 50, L50:
        # pos = 0, abs(0 // 100) = 0, but we did touch the 0!
        if pos == 0 and direction == -1:
            count += 1
    
    print('Second star:', count)


def main():
    f = [line.strip() for line in open('./inputs/01.txt', 'r').readlines()]
    solveFirst(f)
    # solveSecondBruteforce(f)
    solveSecond(f)

if __name__ == '__main__':
    main()
