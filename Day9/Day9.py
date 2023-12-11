import math
import re
import time
from enum import Enum

def getNextValueInSequence(line):
    matchs = re.findall("-?\d+",line)
    sequences = []
    sequences.append([])
    for match in matchs:
        sequences[0].append(int(match))

    ended = False
    i = 0
    while not ended:
        sequences.append(getOneDepthOfSequence(sequences[i]))
        i=i+1
        max_value = max(sequences[i])
        min_value = min(sequences[i])
        #print(max_value, min_value)
        if min_value == 0 and max_value == 0:
            ended = True
    #print(sequences)

    newLastValue = 0
    while i >= 0:
        newLastValue = newLastValue + sequences[i][-1]
        i=i-1
    #print(newLastValue)
    return newLastValue

def getPreviousValueInSequence(line):
    matchs = re.findall("-?\d+",line)
    sequences = []
    sequences.append([])
    for match in matchs:
        sequences[0].append(int(match))

    ended = False
    i = 0
    while not ended:
        sequences.append(getOneDepthOfSequence(sequences[i]))
        i=i+1
        max_value = max(sequences[i])
        min_value = min(sequences[i])
        #print(max_value, min_value)
        if min_value == 0 and max_value == 0:
            ended = True
    #print(sequences)

    newFirstValue = 0
    while i >= 0:
        #print(newFirstValue, sequences[i][0])
        newFirstValue = (sequences[i][0] - newFirstValue)
        i=i-1
    #print(newFirstValue, sequences[0])
    return newFirstValue

def getOneDepthOfSequence(sequence):
    outSequence = []
    for i in range(len(sequence)-1):
        outSequence.append(sequence[i+1] - sequence[i])
    return outSequence

def readInputFile(path):
    f = open(path, "r")
    text = f.read()
    array = text.split("\n")
    return array

def runPart1():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day9Input.txt")
    count = 0

    for line in array:
        count = count + getNextValueInSequence(line)
    
    timeElapsed = (time.process_time_ns() - start_time)
    return [count, timeElapsed]

def runPart2():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day9Input.txt")
    count = 0

    for line in array:
        count = count + getPreviousValueInSequence(line)
    #line = array[10]
    #count = count + getPreviousValueInSequence(line)
    
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