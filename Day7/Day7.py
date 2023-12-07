import re
import time
from enum import Enum

class TYPE(Enum):
    HIGH = 1
    PAIR = 2
    TWO  = 3
    THREE = 4
    FULL = 5
    FOUR = 6
    FIVE = 7

def getType(hand):
    alreadyFoundHand = {}
    for i in hand:
        if i in alreadyFoundHand:
            alreadyFoundHand[i] += 1
        else:
            alreadyFoundHand[i] = 1

    hasAThree = False
    hasAPair = False
    for key in alreadyFoundHand:
        val = alreadyFoundHand[key]
        if val == 5:
            return TYPE.FIVE
        if val == 4:
            return TYPE.FOUR
        if val == 3:
            hasAThree = True
            if hasAPair:
                return TYPE.FULL
        if val == 2:
            if hasAPair:
                return TYPE.TWO
            if hasAThree:
                return TYPE.FULL
            hasAPair = True
    if hasAThree:
        return TYPE.THREE
    if hasAPair:
        return TYPE.PAIR
    return TYPE.HIGH

def getTypeWithJoker(hand):
    alreadyFoundHand = {}
    for i in hand:
        if i in alreadyFoundHand:
            alreadyFoundHand[i] += 1
        else:
            alreadyFoundHand[i] = 1

    hasAThree = False
    hasAPair = False
    jokerCount = 0
    currentType = TYPE.HIGH
    for key in alreadyFoundHand:
        val = alreadyFoundHand[key]
        if key == "1":
            jokerCount = val
        if val == 5:
            currentType = TYPE.FIVE
        if val == 4:
            currentType = TYPE.FOUR
        if val == 3:
            hasAThree = True
        if val == 2:
            if hasAPair:
                currentType = TYPE.TWO
            hasAPair = True
    if currentType == TYPE.HIGH:
        if hasAThree:
            currentType = TYPE.THREE
        if hasAPair:
            currentType = TYPE.PAIR
        if hasAThree and hasAPair:
            currentType = TYPE.FULL
    
    if jokerCount == 0:
        return currentType
    elif jokerCount == 1:
        if currentType == TYPE.HIGH:
            return TYPE.PAIR
        if currentType == TYPE.PAIR:
            return TYPE.THREE
        if currentType == TYPE.TWO:
            return TYPE.FULL
        if currentType == TYPE.THREE:
            return TYPE.FOUR
        if currentType == TYPE.FOUR:
            return TYPE.FIVE
    elif jokerCount == 2:
        if currentType == TYPE.PAIR:
            return TYPE.THREE
        if currentType == TYPE.TWO:
            return TYPE.FOUR
        if currentType == TYPE.THREE:
            return TYPE.FIVE
        if currentType == TYPE.FULL:
            return TYPE.FIVE
    elif jokerCount == 3:
        if currentType == TYPE.PAIR:
            return TYPE.FIVE
        if currentType == TYPE.THREE:
            return TYPE.FOUR
        if currentType == TYPE.FULL:
            return TYPE.FIVE
    elif jokerCount == 4:
            return TYPE.FIVE
    elif jokerCount == 5:
            return TYPE.FIVE

def parseInput(array):
    output = {}
    for line in array:
        matchs = re.findall("\w+",line)
        hand = matchs[0]
        hand = hand.replace("A", "F")
        hand = hand.replace("K", "E")
        hand = hand.replace("Q", "D")
        hand = hand.replace("J", "C")
        hand = hand.replace("T", "B")
        type = getType(hand)
        if type in output:
            output[type].append([hand,int(matchs[1])])
        else:
            output[type] = [[hand,int(matchs[1])]]
    return output

def parseInputPart2(array):
    output = {}
    for line in array:
        matchs = re.findall("\w+",line)
        hand = matchs[0]
        hand = hand.replace("A", "F")
        hand = hand.replace("K", "E")
        hand = hand.replace("Q", "D")
        hand = hand.replace("J", "1")
        hand = hand.replace("T", "B")
        type = getTypeWithJoker(hand)
        if type in output:
            output[type].append([hand,int(matchs[1])])
        else:
            output[type] = [[hand,int(matchs[1])]]
    return output

def readInputFile(path):
    f = open(path, "r")
    text = f.read()
    array = text.split("\n")
    return array

def runPart1():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day7Input.txt")
    count = 0

    handPerType = parseInput(array)
    rankCounter = 1
    for type in TYPE:
        if type in handPerType:
            handOfThisType = handPerType[type]
            handOfThisType.sort()
            for hand in handOfThisType:
                count += hand[1] * rankCounter
                rankCounter = rankCounter + 1
    timeElapsed = (time.process_time_ns() - start_time)
    return [count, timeElapsed]

def runPart2():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day7Input.txt")
    count = 0

    handPerType = parseInputPart2(array)
    rankCounter = 1
    for type in TYPE:
        if type in handPerType:
            handOfThisType = handPerType[type]
            handOfThisType.sort()
            for hand in handOfThisType:
                count += hand[1] * rankCounter
                rankCounter = rankCounter + 1
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