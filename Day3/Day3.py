from re import finditer
import time

def processPart1(symbols, numbers):
    sum = 0
    for numberLineItt, numberLine in enumerate(numbers):
        for number in numberLine:
            sum += searchPart1(number, symbols[max(0,numberLineItt-1):numberLineItt+2])
    return sum

def processPart2(symbols, numbers):
    sum = 0
    for symbolLineItt, symbolLine in enumerate(symbols):
        for symbol in symbolLine:
            sum += searchPart2(symbol, numbers[max(0,symbolLineItt-1):symbolLineItt+2])
    return sum

def searchPart1(number, symbols):
    sum = 0
    for symbolsLine in symbols:
            for symbol in symbolsLine:
                leftSide = int(symbol[0][0])
                rightSide = int(symbol[0][1])
                if(leftSide <= number[0][1] and rightSide >= number[0][0]):
                    sum += int(number[1])
    return sum

def searchPart2(symbol, numbers):
    contactCount = 0
    gearRatio = 0
    for numbersLine in numbers:
        for number in numbersLine:
            leftSide = int(number[0][0])
            rightSide = int(number[0][1])
            value = int(number[1])
            if(leftSide <= symbol[0][1] and rightSide >= symbol[0][0]):
                contactCount += 1
                if gearRatio == 0:
                    gearRatio = value
                else:
                    gearRatio *= value
    if contactCount == 2:
        return gearRatio
    else:
        return 0

def getLineInfo(regex,line):
    lineInfo=[]
    for match in finditer(regex, line):
        lineInfo.append((match.span(), match.group()))
    return lineInfo


def readInputFile(path):
    f = open(path, "r")
    text = f.read()
    array = text.split("\n")
    return array

def runPart1():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day3Input.txt")
    count = 0
    numbers = []
    symbols = []
    for line in array:
        numbers.append(getLineInfo("\d+",line))
        symbols.append(getLineInfo("[^.0-9]+",line))
    
    count = processPart1(symbols, numbers)
    timeElapsed = (time.process_time_ns() - start_time)
    return [count, timeElapsed]

def runPart2():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day3Input.txt")
    count = 0
    numbers = []
    symbols = []
    for line in array:
        numbers.append(getLineInfo("\d+",line))
        symbols.append(getLineInfo("\*+",line))
    count = processPart2(symbols, numbers)
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