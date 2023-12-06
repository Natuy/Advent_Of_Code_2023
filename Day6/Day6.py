import math
import re
import time

def processARace(maxTime,distance):
    countOfSuccess = 0

    for i in range(1,int(maxTime)):
        holdTime = i

        speed = holdTime
        timeLeft = int(maxTime) - holdTime
        distanceReached = speed * timeLeft
        if distanceReached > int(distance):
            print(holdTime)
            countOfSuccess+=1
    return countOfSuccess

def flatten(test_list):
    if isinstance(test_list, list):
        if len(test_list) == 0:
            return []
        first, rest = test_list[0], test_list[1:]
        return flatten(first) + flatten(rest)
    else:
        return [test_list]
    
def processARaceByDichotomy(maxTime,distance):
    countOfSuccess = 0
    maxTime = int(maxTime)
    distance = int(distance)
    holdTime = math.ceil(maxTime / 2)
    correctValues = []
    correctValues.append(raceStepByDichotomy(maxTime,distance,holdTime, 2))
    correctValues = flatten(correctValues)
    correctValues = [x for x in correctValues if x != None]
    correctValues.sort()
    print(correctValues)
    value = 1 + correctValues[-1] - correctValues[0]
    return value

def raceStepByDichotomy(maxTime,distance,holdTime, depth, direction=0):
    output = []
    newVals = DoDichotomy(holdTime, maxTime, depth)
    if newVals[0] >= newVals[1]:
        return
    if(isDistanceReached(maxTime,distance,holdTime)):
        print("Found")
        output.append(holdTime)
        if(direction >= 0):
            output.append(raceStepByDichotomy(maxTime,distance,newVals[1], depth+1, +1))
        if(direction <= 0):
            output.append(raceStepByDichotomy(maxTime,distance,newVals[0], depth+1, -1))
    else:
        if(direction >= 0):
            output.append(raceStepByDichotomy(maxTime,distance,newVals[0], depth+1, +1))
        if(direction <= 0):
            output.append(raceStepByDichotomy(maxTime,distance,newVals[1], depth+1, -1))
    return output

def isDistanceReached(maxTime,distance,holdTime):
    speed = holdTime
    timeLeft = int(maxTime) - holdTime
    distanceReached = speed * timeLeft
    if distanceReached > int(distance):
        return True
    return False


def DoDichotomy(val, rangeSize, depth):
    depth = 2**depth
    valLeft = math.floor(val - rangeSize/depth)
    valRight = math.ceil(val + rangeSize/depth)
    return [valLeft,valRight]


def parseInput(array):
    output = []
    for count, line in enumerate(array):
        matchs = re.findall("\s(\d+)",line)
        output.append(matchs)
    return output


def parseInputPart2(array):
    output = []
    for count, line in enumerate(array):
        matchs = re.findall("\s(\d+)",line)
        matchs = "".join(matchs)
        output.append(matchs)
    return output

def readInputFile(path):
    f = open(path, "r")
    text = f.read()
    array = text.split("\n")
    return array

def runPart1():
    start_time = time.process_time_ns()
    array = readInputFile("C:\\Users\conta\OneDrive\Bureau\AOC_2023\day6Input.txt")
    count = 1

    raceInfo = parseInput(array)

    for i in range(len(raceInfo[0])):
        count = count * processARace(raceInfo[0][i],raceInfo[1][i])
    timeElapsed = (time.process_time_ns() - start_time)
    return [count, timeElapsed]

def runPart2():
    start_time = time.process_time_ns()
    array = readInputFile("C:\\Users\conta\OneDrive\Bureau\AOC_2023\day6Input.txt")
    count = 1

    raceInfo = parseInputPart2(array)
    count =  processARaceByDichotomy(raceInfo[0],raceInfo[1])
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
timePuzzle(1,noPart2)