#!/usr/bin/env python3

def solveFirst(f):
    connected = [[el] for el in range(len(f))]
    distances = []
    circuits = [el for el in range(len(f))] # box x is part of the circuit[x]
    for i in range(len(f)):
        for j in range(i + 1, len(f)):
            distances.append((i, j, sum([(f[i][k] - f[j][k]) ** 2 for k in range(3)])))
    distances.sort(key=lambda x: x[2])
    for _ in range(1000):
        i, j, val = distances.pop(0)
        # if the values are part of different circuits, move all the boxes from circuit j to circuit i
        if circuits[i] != circuits[j]: 
            diff = list(set(connected[circuits[j]]) - set(connected[circuits[i]]))
            connected[circuits[i]] += diff
            connected[circuits[j]] = []
            for el in diff:
                circuits[el] = circuits[i]
    size = sorted([len(val) for val in connected], reverse=True)
    print('First star:', size[0] * size[1] * size[2])

def solveSecond(f):
    connected = [[el] for el in range(len(f))]
    distances = []
    circuits = [el for el in range(len(f))]
    for i in range(len(f)):
        for j in range(i + 1, len(f)):
            distances.append((i, j, sum([(f[i][k] - f[j][k]) ** 2 for k in range(3)])))
    distances.sort(key=lambda x : x[2])
    last = (-1, -1)
    while len(set(circuits)) != 1:
        i, j, val = distances.pop(0)
        if circuits[i] != circuits[j]:
            last = (i, j)
            diff = list(set(connected[circuits[j]]) - set(connected[circuits[i]]))
            connected[circuits[i]] += diff
            connected[circuits[j]] = []
            for el in diff:
                circuits[el] = circuits[i]
    print('Second star:', f[i][0] * f[j][0])

def main():
    f = [[int(el.strip()) for el in line.split(',')] for line in open('./inputs/08.txt', 'r').readlines()]
    solveFirst(f)
    solveSecond(f)
    
if __name__ == '__main__':
    main()

