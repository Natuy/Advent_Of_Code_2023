import re
import time

def getPositionOfAllGalaxies(array):
    galaxies = []
    for lineCount, line in enumerate(array):
        for match in re.finditer("#", line):
            galaxies.append([lineCount, match.start()])
    return galaxies, [len(array),len(array[0])]

def expandFullUniverse(galaxies):
    allXValues = [x for x, y in galaxies]
    missingXValues = [x for x in set(range(min(allXValues), max(allXValues) + 1)) if x not in allXValues]
    allYValues = [y for x, y in galaxies]
    missingYValues = [y for y in set(range(min(allYValues), max(allYValues) + 1)) if y not in allYValues]
    
    for rowi in reversed(missingXValues):
        galaxies = expandUniverseRow(rowi, galaxies)
    for coli in reversed(missingYValues):
        galaxies = expandUniverseCol(coli, galaxies)
    return galaxies
 
globalUniverseIncrement = 1

def expandUniverseRow(r,galaxies):
    for i,galaxy in enumerate(galaxies):
        if galaxy[0] > r:
            galaxies[i][0] = galaxies[i][0]+globalUniverseIncrement
    return galaxies

def expandUniverseCol(c,galaxies):
    for i,galaxy in enumerate(galaxies):
        if galaxy[1] > c:
            galaxies[i][1] = galaxies[i][1]+globalUniverseIncrement
    return galaxies

def getDistance(galaxyA, galaxyB):
    return abs(galaxyA[0] - galaxyB[0]) + abs(galaxyA[1] - galaxyB[1])

def readInputFile(path):
    f = open(path, "r")
    text = f.read()
    array = text.split("\n")
    return array

def runPart1():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day11Input.txt")

    sumOfDistances = 0
    galaxies,universeSize = getPositionOfAllGalaxies(array)
    galaxies = expandFullUniverse(galaxies)
    for galaxyId, galaxy in enumerate(galaxies):
        galaxyA = galaxy
        for galaxyB in galaxies[galaxyId + 1:]:
            distance = getDistance(galaxyA,galaxyB)
            sumOfDistances = sumOfDistances + distance

    timeElapsed = (time.process_time_ns() - start_time)
    return [sumOfDistances, timeElapsed]

def runPart2():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day11Input.txt")
    
    global globalUniverseIncrement
    globalUniverseIncrement = 999999
    sumOfDistances = 0
    galaxies,universeSize = getPositionOfAllGalaxies(array)
    galaxies = expandFullUniverse(galaxies)
    for galaxyId, galaxy in enumerate(galaxies):
        galaxyA = galaxy
        for galaxyB in galaxies[galaxyId + 1:]:
            distance = getDistance(galaxyA,galaxyB)
            sumOfDistances = sumOfDistances + distance

    timeElapsed = (time.process_time_ns() - start_time)
    return [sumOfDistances, timeElapsed]

def executePuzzle(disablePart2 = False):
    print("Result of Part 1 :", runPart1()[0])
    if(not disablePart2):
        print("Result of Part 2 :", runPart2()[0])

def timePuzzle(nbItteration,disablePart2 = False):
    print("Timing for an execution, mean of",nbItteration,"itterations")
    t = 0
    for i in range(nbItteration):
        t += runPart1()[1]
    t = (t/nbItteration)/(10**9)
    print("Part 1 :",t,"seconds")

    if(not disablePart2):
        t = 0
        for i in range(nbItteration):
            t += runPart2()[1]
        t = (t/nbItteration)/(10**9)
        print("Part 2 :",t,"seconds")

noPart2 = False
executePuzzle(noPart2)
timePuzzle(1000,noPart2)