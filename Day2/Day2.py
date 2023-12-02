import re
import time

cubeLimit =  {"red" : 12, "green" : 13, "blue" : 14}

def processALinePart1(line):
    matchs = re.findall("(\d{2,}) (\D*)(,|;|$)",line)
    for m in matchs:
        countOfCubes = m[0]
        colorOfCubes = m[1]
        if(int(countOfCubes) > cubeLimit[colorOfCubes]):
            return 0
    id = re.search("(\d*):",line)[1]
    return int(id)


def processALinePart2(line):
    matchs = re.findall("(\d*) (\D*)(,|;|$)",line)
    cubeCount =  {"red" : 0, "green" : 0, "blue" : 0}
    for m in matchs:
        countOfCubes = int(m[0])
        colorOfCubes = m[1]
        if(countOfCubes > cubeCount[colorOfCubes]):
            cubeCount[colorOfCubes] = countOfCubes
    cubePower = cubeCount["red"] * cubeCount["green"] * cubeCount["blue"]
    return cubePower

def readInputFile(path):
    f = open(path, "r")
    text = f.read()
    array = text.split("\n")
    return array

def runPart1():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day2Input.txt")
    count = 0
    for line in array:
        count +=  processALinePart1(line)
    timeElapsed = (time.process_time_ns() - start_time)
    return [count, timeElapsed]

def runPart2():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day2Input.txt")
    count = 0
    for line in array:
        count +=  processALinePart2(line)
    timeElapsed = (time.process_time_ns() - start_time)
    return [count, timeElapsed]

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