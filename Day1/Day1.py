import re
import time

def transformLetterDigitToNumber(out):
    match out:
        case "nine":
            return "9"
        case "eight":
            return "8"
        case "seven":
            return "7"
        case "six":
            return "6"
        case "five":
            return "5"
        case "four":
            return "4"
        case "three":
            return "3"
        case "two":
            return "2"
        case "one":
            return "1"
        case _:
            return out

def getFirstNumberFromString(string):
    x = re.search("^\D*(\d)",string)
    return x.group(1)

def getLastNumberFromString(string):
    x = re.search("(\d)\D*$",string)
    return x.group(1)

def getFirstNumberFromStringPart2(string):
    x = re.search("(nine|eight|seven|six|five|four|three|two|one|\d)(?!nine|eight|seven|six|five|four|three|two|one|\d)*.*$",string)
    return transformLetterDigitToNumber(x.group(1))

def getLastNumberFromStringPart2(string):
    x = re.search("^.*(nine|eight|seven|six|five|four|three|two|one|\d)(?!nine|eight|seven|six|five|four|three|two|one|\d)*",string)
    return transformLetterDigitToNumber(x.group(1))

def makeDoubleDigit(digit1, digit2):
    x = int(digit1 + digit2)
    return x

def readInputFile(path):
    f = open(path, "r")
    text = f.read()
    array = text.split("\n")
    return array

def runPart1():
    start_time = time.process_time_ns()
    array = readInputFile(r"<REDACTED_PATH>")
    count = 0
    for line in array:
        count = count + makeDoubleDigit(getFirstNumberFromString(line), getLastNumberFromString(line))
    #print("Result Part 1 = " + str(count))
    timeElapsed = (time.process_time_ns() - start_time)
    #print(secondsElapsed, "seconds")
    return [count, timeElapsed]

def runPart2():
    start_time = time.process_time_ns()
    array = readInputFile(r"<REDACTED_PATH>")
    count = 0
    for line in array:
        count = count + makeDoubleDigit(getFirstNumberFromStringPart2(line), getLastNumberFromStringPart2(line))
    #print("Result Part 2 = " + str(count))
    timeElapsed = (time.process_time_ns() - start_time)
    #print(secondsElapsed, "seconds")
    return [count, timeElapsed]

def executePuzzle():
    print("Result of Part 1 : ", runPart1()[0])
    print("Result of Part 2 : ", runPart2()[0])

def timePuzzle(nbItteration):
    print("Timing for an execution, mean of",nbItteration,"itterations")
    t = 0
    for i in range(nbItteration):
        t += runPart1()[1]
    t = (t/nbItteration)/(10**9)
    print("Part 1 :",t,"seconds")

    t = 0
    for i in range(nbItteration):
        t += runPart2()[1]
    t = (t/nbItteration)/(10**9)
    print("Part 2 :",t,"seconds")

executePuzzle()
timePuzzle(1000)