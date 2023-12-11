import re
import time
from enum import Enum
from textwrap import wrap

class DIRECTION(Enum):
    NORTH = 0
    EAST  = 1
    SOUTH = 2
    WEST  = 3

connectingPipes = [["S","|","7","F"],
                   ["S","-","J","7"],
                   ["S","|","L","J"],
                   ["S","-","L","F"],
                   ]

def parseInput(array):
    lineLength = len(array[0]) + 1
    fullLabyrinth = "\n".join(array)
    matchS = re.search("S",fullLabyrinth)

    positionOfS = matchS.start()
    linePosition = positionOfS // lineLength
    rowPosition  = positionOfS % lineLength

    startingPosition = [linePosition, rowPosition]
    
    return fullLabyrinth, lineLength, startingPosition

def exploreLabyrinth(fullLabyrinth, lineLength, startingPosition):
    newLabyrinth = "."*(lineLength+2)*(len(fullLabyrinth) // lineLength)
    currentPosition = startingPosition
    inputDirection = DIRECTION.NORTH
    
    ended = False
    count = 0
    
    while not ended:
        count = count + 1
        currentPosition, inputDirection = getNextPosition(fullLabyrinth, lineLength, currentPosition, inputDirection)
        
        index = currentPosition[1] + (currentPosition[0]*lineLength)
        newLabyrinth = newLabyrinth[:index] + fullLabyrinth[index] + newLabyrinth[index + 1:]
        if currentPosition == startingPosition:
            ended = True
    return count/2


def exploreLabyrinthPart2(fullLabyrinth, lineLength, startingPosition):
    newLabyrinth = "."*(lineLength+2)*(len(fullLabyrinth) // lineLength)
    currentPosition = startingPosition
    inputDirection = DIRECTION.NORTH
    
    ended = False
    count = 0
    
    while not ended:
        count = count + 1
        currentPosition, inputDirection = getNextPosition(fullLabyrinth, lineLength, currentPosition, inputDirection)
        
        index = currentPosition[1] + (currentPosition[0]*lineLength)
        newLabyrinth = newLabyrinth[:index] + fullLabyrinth[index] + newLabyrinth[index + 1:]
        if currentPosition == startingPosition:
            ended = True
    '''
    lineCount =  len(newLabyrinth) // lineLength
    for i in range(0,lineCount+2):
        print(newLabyrinth[(lineLength*i):lineLength*(i+1)-1])
    '''
    return exploreNewLabyrinth(newLabyrinth, lineLength)

def exploreNewLabyrinth(newLabyrinth, lineLength):
    
    lineCount =  len(newLabyrinth) // lineLength
    insideCount = 0
    for lineItt in range(lineCount):
        northWallCount = 0
        southWallCount = 0
        for rowItt in range(lineLength-1):
            positionValue = newLabyrinth[rowItt + (lineItt*lineLength)]
            if positionValue in connectingPipes[DIRECTION.SOUTH.value]: #Wall towards North
                northWallCount = northWallCount + 1
            if positionValue in connectingPipes[DIRECTION.NORTH.value]: #Wall towards South
                southWallCount = southWallCount + 1
            if positionValue in ["."]:
                #print("Found An Empty Space",[lineItt, rowItt], positionValue, northWallCount, southWallCount)
                if northWallCount %2 == 1:
                    insideCount = insideCount + 1
                    #print("Inside?",insideCount)
    return insideCount


def getNextPosition(fullLabyrinth, lineLength, startingPosition, lastInputDirection):
    startingPositionValue = fullLabyrinth[startingPosition[1] + (startingPosition[0]*lineLength)]

    for dir in DIRECTION:
        if startingPositionValue in connectingPipes[(dir.value+2)%4]:
            #print("Trying to go",dir,dir.value != (lastInputDirection.value+2)%4)
            if dir.value != (lastInputDirection.value+2)%4:
                if dir == DIRECTION.NORTH:
                    currentPosition = [startingPosition[0]-1, startingPosition[1]]
                elif dir == DIRECTION.SOUTH:
                    currentPosition = [startingPosition[0]+1, startingPosition[1]]
                if dir == DIRECTION.WEST:
                    currentPosition = [startingPosition[0], startingPosition[1]-1]
                elif dir == DIRECTION.EAST:
                    currentPosition = [startingPosition[0], startingPosition[1]+1]
                currentPositionValue = fullLabyrinth[currentPosition[1] + (currentPosition[0]*lineLength)]
                #print("Trying to go in direction",dir," from cell",startingPosition,fullLabyrinth[startingPosition[1] + (startingPosition[0]*lineLength)],"to cell",currentPosition,currentPositionValue)
                if currentPositionValue in connectingPipes[dir.value]:
                    #print("I can go",dir,"from cell",startingPosition,fullLabyrinth[startingPosition[1] + (startingPosition[0]*lineLength)],"to cell",currentPosition,currentPositionValue)
                    #print(startingPosition,fullLabyrinth[startingPosition[1] + (startingPosition[0]*lineLength)]," -- ",currentPosition,currentPositionValue)
                    return currentPosition, dir
    print("I'm Lost!",startingPosition, lastInputDirection)

def readInputFile(path):
    f = open(path, "r")
    text = f.read()
    array = text.split("\n")
    return array

def runPart1():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day10Input.txt")
    count = 0

    fullLabyrinth, lineLength, startingPosition = parseInput(array)
    count = exploreLabyrinth(fullLabyrinth, lineLength, startingPosition)
    
    timeElapsed = (time.process_time_ns() - start_time)
    return [count, timeElapsed]

def runPart2():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day10Input.txt")

    fullLabyrinth, lineLength, startingPosition = parseInput(array)
    count = exploreLabyrinthPart2(fullLabyrinth, lineLength, startingPosition)

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