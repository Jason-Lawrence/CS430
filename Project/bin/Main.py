import sys
import Utility
import Instance
import Greedy
import os


def init():
    """ Setup function. Checks sys arguments

        Args:
            None

        Returns:
            instance     (Instance.Instance)   - Instance object that holds all of the relevant data from the Instance file.
            Algorithm    (Str)                 - The requested Algorithm to run

        Globals:
            None

        Called By:
            Main()

        Calls:
            Utility.init()
    """
    try:
        if len(sys.argv) != 2:
            print("[ERROR] Not enough arguments")
            return -1

        instanceDir = sys.argv[1]
        return instanceDir

    except EnvironmentError:
        print("[ERROR] Invalid Instance file given")
        return -1

def main():
    """ Main function. Calls initailizing functions and then calls the requested Algorithm

        Args:
            None

        Returns:
            None

        Globals:
            None

        Called By:
            cmd.exe

        Calls:
            init()
            Greedy.init()
    """
    instanceDir = init()
    if instanceDir == -1:
        return -1

    for file in os.listdir(instanceDir):
        instance = Utility.init(instanceDir, file)
        result = Greedy.main(instance)
        Utility.outputFileGenerator(result, file)

if __name__ == '__main__':
	main()
