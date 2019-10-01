import Instance
import sys
import os
import time
sys.path.append("..\\Instances")

def parser(line):
    """Support function. Takes in a line from a file and parses the contents into x and y coordinates

        Args:
            line        (Str)     - The line from the file to parse

        Returns:
            x           (Float)   - The x Coordinate
            y           (Float)   - The y Coordinate

        Globals:
            None

        Called By:
            Constructor

        Calls:
            None
    """
    line = line.split(' ')
    x = float(line[0].strip())
    y = float(line[1].strip())
    return x, y

def Constructor(file, instance):
    """ Constructor function. Reads a file and builds the Instance Object.

        Args:
            file      (File)                 - The instance file to base the instance object off of.
            instance  (Instance.Instance)    - The instance object to be built

        Returns:
            instance  (Instance.Instance)    - The built instance object

        Globals:
            None

        Called By:
            init()

        Calls:
            parser()
    """
    start = file.readline()
    for id in range(int(start)):
        line = file.readline()
        x, y = parser(line)
        instance.Centers.append(Instance.Centers(id, x, y))
        print(str(instance.Centers[id].x) + ", " + str(instance.Centers[id].y))

    line = file.readline()
    for x in range(int(line)):
        line = file.readline()
        x, y = parser(line)
        instance.Pointers.append(Instance.Points(x,y))

    return instance

def init(instanceDir, file):
    """ Setup function. Calls the Instance Constructor.

        Args:
            instanceDir    (Dir)                  - The Directory containig the instance files to use to build the instance objects.
            file           (Str)                  - The file to use.

        Returns:
            instance        (Instance.Instance)     - The instance object built

        Globals:
            None

        Called By:
            Main.init()

        Calls:
            Constructor
    """
    instance = Instance.Instance()
    filepath = instanceDir + "\\" + file
    with open(filepath, 'r') as inst:
        Constructor(inst, instance)

    inst.close()
    return instance

def getInstanceNum(file):
    """ Output function helper. Retrieves the instance number from the input file.

        Args:
            file         (Str)          - The file name

        Returns:
            num          (Str)          - The instance Number

        Globals:
            None

        Called By:
            outputFileGenerator()

        Calls:
            None
    """
    num = ""
    nums = ''
    list = file.split('.')
    x = len(list[0])
    file = list[0]
    while file[x-1].isdigit():
        nums += file[x-1]
        x -= 1
    x = len(nums) - 1
    while x != -1:
        num += nums[x]
        x -= 1
    return num

def outputFileGenerator(result, file):
    """ Output function. Generates the output File according to the guidelines set in the PDF

        Args:
            result          (list)          - List of Centers.
            file            (Str)           - File name

        Returns:
            None                            - Generates an output file.

        Globals:
            None

        Called By:
            Main.main()

        Calls:
            None
    """
    num = getInstanceNum(file)
    file = "..\\Results\\solution" + num + ".txt"
    outputFile = open(file, "w+")
    outputFile.write("greedy " + str(len(result)) + "\n")
    if len(result) == 0:           ## the algorithm couldn't find a list of centers that could cover all of the points
        outputFile.write("No solution was found\n")

    else:
        for center in result:
            outputFile.write(str(center.id + 1) + "\n") ## The "+1" accounts for the difference in starting points. I start at 0 instead of 1.
