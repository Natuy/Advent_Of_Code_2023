import re
import time

def parseSeeds(line):
    return re.findall("\s(\d*)",line)

def parseSeedsPart2(line):
    pairs = re.findall("\s(\d*) (\d*)",line)
    seeds = []
    for pair in pairs:
        seeds.append([int(pair[0]),int(pair[0])+int(pair[1])])
    return seeds

def parseDestinationCategory(array):
    destinationCategory = []
    stepCounter = -1
    for line in array:
        if(len(line) > 0 and line[0].isalpha()):
            stepCounter+=1
            destinationCategory.append([])
            continue
        stuff = re.findall("(\d*) (\d*) (\d*)", line)
        if len(stuff) > 0:
            dstRangeStart = int(stuff[0][0])
            srcRangeStart = int(stuff[0][1])
            rangeLength = int(stuff[0][2])

            srcRangeEnd = srcRangeStart+rangeLength
            srcToDest = dstRangeStart-srcRangeStart
            destinationCategory[stepCounter].append([srcRangeStart,srcRangeEnd,srcToDest])
    return destinationCategory

def getDestination(strSeed,map):
    seed = int(strSeed)
    #srcRangeStart,srcRangeEnd,srcToDest
    for m in map:
        srcRangeStart = int(m[0])
        srcRangeEnd = int(m[1])
        srcToDest = int(m[2])
        if srcRangeStart <= seed:
            if srcRangeEnd > seed:
                calculatedValue = seed + srcToDest
                return calculatedValue
    return seed

def getMin(currentMin,myList):
    minValue = currentMin
    for l in myList:
        while isinstance(l, list):
            l = l[0]
        minValue = min(l,minValue)
    return minValue

def half_flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(item)
        else:
            flat_list.append(item)
    return flat_list

def isInRange(value,rangeStart,rangeEnd):
    if rangeStart <= value:
        if rangeEnd > value:
            return True
    return False

def getDestinationPart2(seed,map):
    while isinstance(seed[0], list):
        seed = seed[0]
    seedStart = seed[0]
    seedEnd = seed[1]
    outputSeedList = []
    for m in map:
        srcRangeStart = int(m[0])
        srcRangeEnd = int(m[1])
        srcToDest = int(m[2])
        seedStartInRange =isInRange(seedStart,srcRangeStart,srcRangeEnd)
        seedEndInRange =isInRange(seedEnd,srcRangeStart,srcRangeEnd)
        if seedStartInRange:
            if seedEndInRange:
                outputSeedList.append([seedStart+srcToDest,seedEnd+srcToDest])
            else:
                outputSeedList.append(getDestinationPart2([seedStart,srcRangeEnd-1],map))
        else:
            if seedEndInRange:
                outputSeedList.append(getDestinationPart2([srcRangeStart,seedEnd],map))
                continue
            elif isInRange(srcRangeStart,seedStart,seedEnd) and isInRange(srcRangeEnd,seedStart,seedEnd):
                outputSeedList.append(getDestinationPart2([srcRangeStart,srcRangeEnd-1],map))
                continue
    if(len(outputSeedList)<= 0):
        outputSeedList.append(seed)
    return outputSeedList

def readInputFile(path):
    f = open(path, "r")
    text = f.read()
    array = text.split("\n")
    return array

def runPart1():
    start_time = time.process_time_ns()
    array = readInputFile("C:\\Users\conta\OneDrive\Bureau\AOC_2023\day5Input.txt")
    count = 0
    destinationCategory = []

    seeds = parseSeeds(array[0])
    destinationCategory = parseDestinationCategory(array)
    
    min = 999999999999999999
    for seed in seeds:
        val = seed
        for category in range(1,len(destinationCategory)):
            val = getDestination(val, destinationCategory[category])
            #print(seed,"==>",category,"=>",val)
        if(val < min):
            min = val
    count = min
    timeElapsed = (time.process_time_ns() - start_time)
    return [count, timeElapsed]

def runPart2():
    start_time = time.process_time_ns()
    array = readInputFile("C:\\Users\conta\OneDrive\Bureau\AOC_2023\day5Input.txt")
    count = 0
    destinationCategory = []

    seeds = parseSeedsPart2(array[0])
    
    destinationCategory = parseDestinationCategory(array)
    min = 999999999999999999
    for seed in seeds:
        val = [seed]
        for category in range(1,len(destinationCategory)):
            newVal = []
            for v in val:
                newVal.append(getDestinationPart2(v, destinationCategory[category]))
                val = half_flatten_list(newVal)
        min = getMin(min,val)
    count = min
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