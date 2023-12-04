import time

def processPart1(line):
    count = 0
    
    x = line.replace("  ", " ")
    splitted = x.split(":")
    numbers = splitted[1].split("|")
    winningNumbers = numbers[0].split()
    myNumbers = numbers[1].split()

    for number in myNumbers:
        if number in winningNumbers:
            if count == 0:
                count = 1
            else:
                count = count * 2
    return count

def processPart2(line, list, lineCount, multiplier = 1):
    count = 0
    
    x = line.replace("  ", " ")
    splitted = x.split(":")
    numbers = splitted[1].split("|")
    winningNumbers = numbers[0].split()
    myNumbers = numbers[1].split()

    for number in myNumbers:
        if number in winningNumbers:
            count = count + 1
            list[lineCount + count] = list[lineCount + count] + multiplier
    return  list

def readInputFile(path):
    f = open(path, "r")
    text = f.read()
    array = text.split("\n")
    return array

def runPart1():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day4Input.txt")
    count = 0
    for line in array:
        count += processPart1(line)
    
    timeElapsed = (time.process_time_ns() - start_time)
    return [count, timeElapsed]

def runPart2():
    start_time = time.process_time_ns()
    array = readInputFile(r"C:\Users\telle\Desktop\AOC_2023\day4Input.txt")
    list = [1] * len(array)
    count = 0
    for lineCount, line in enumerate(array):
        list = processPart2(line,list, lineCount, list[lineCount])
        count += list[lineCount]
    
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