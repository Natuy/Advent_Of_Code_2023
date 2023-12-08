import math
import re
import time
from enum import Enum

def parseInput(array):
    instructions = array[0]
    network = []
    for line in array:
        matchs = re.findall("(\w+) = \((\w+), (\w+)",line)
        if matchs and len(matchs[0]) >= 2:
            source = matchs[0][0]
            left  = matchs[0][1]
            right = matchs[0][2]
            network.append([source, left, right])
    network.sort()
    output = {}
    for act in network:
        output[act[0]] = [act[1],act[2]]
    return instructions,output


def parseInput2(array):
    instructions = array[0]
    network = []
    startingPositions = []
    for line in array:
        matchs = re.findall("(\w+) = \((\w+), (\w+)",line)
        if matchs and len(matchs[0]) >= 2:
            source = matchs[0][0]
            left  = matchs[0][1]
            right = matchs[0][2]
            network.append([source, left, right])
            if source[2] == "A":
                startingPositions.append(source)
    network.sort()
    output = {}
    for act in network:
        output[act[0]] = [act[1],act[2]]
    return instructions, output, startingPositions

def exploreAllDesert(instructions,network,startPosition):
    count = 0
    currentPosition = startPosition
    ended = False
    while not ended:
        currentInstruction = instructions[count%len(instructions)]
        if(currentInstruction == "L"):
            currentPosition = network[currentPosition][0]
        else:
            currentPosition = network[currentPosition][1]
        count = count + 1
        if currentPosition == "ZZZ":
            ended = True
    return count

def exploreAllDesertB(instructions,network,startPosition):
    count = 0
    currentPosition = startPosition
    ended = False
    while not ended:
        currentInstruction = instructions[count%len(instructions)]
        if(currentInstruction == "L"):
            currentPosition = network[currentPosition][0]
        else:
            currentPosition = network[currentPosition][1]
        count = count + 1
        if currentPosition[2] == "Z":
            ended = True
    
    #print(startPosition, count, currentPosition)
    return count

def readInputFile(path):
    f = open(path, "r")
    text = f.read()
    array = text.split("\n")
    return array

def runPart1():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day8Input.txt")

    instructions,network = parseInput(array)
    startPosition = "AAA"
    count = exploreAllDesert(instructions,network,startPosition)
    
    timeElapsed = (time.process_time_ns() - start_time)
    return [count, timeElapsed]

def runPart2():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day8Input.txt")
    
    instructions, network, startingPositions = parseInput2(array)
    counts = []
    for startPosition in startingPositions:
        counts.append(exploreAllDesertB(instructions,network,startPosition))

    count = math.lcm(*counts)
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