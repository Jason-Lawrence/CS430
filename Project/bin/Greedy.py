import Instance
import math

def countPointers(instance):
    """ Counts uncovered points in the Instance that aren't covered by a center in the Set.
        Runtime: O(C * P) amount of Pointers times the amount of Centers (n^2)

        Args:
            instance  (Instance.Instance)    - Instance object with the points to count.

        Returns:
            None

        Globals:
            None

        Called By:
            greedy()

        Calls:
            None
    """
    for C in instance.Centers:
        count = 0
        for P in instance.Pointers:
            distance = math.sqrt(math.pow((P.x - C.x), 2) + math.pow((P.y - C.y), 2))
            if distance >= 0 and distance <= 1 and P.covered == False:
                count += 1
                P.list.append(C)
        C.count = count

def findMax(instance):
    """ Finds the Center with the most amount of points.
        Runtime: O(C) (amount of centers)

        Args:
            instance  (Instance.Instance)    - Instance object with the points to count.

        Returns:
            maxID     (Int)                  - The id of the Center.

        Globals:
            None

        Called By:
            greedy()

        Calls:
            None
    """
    max = -1
    maxID = -1
    for C in instance.Centers:
        if C.count > max:
            maxID = C.id
            max = C.count
    return maxID

def coverPoints(Center, instance):
    """ Covers all of the that the given Center covers.
        Runtime: O(P) (amount of points)
        Args:
            Center    (Instance.Center)      - Center object that covers most of the points.
            instance  (Instance.Instance)    - Instance object with the points to count.

        Returns:
            None

        Globals:
            None

        Called By:
            greedy()

        Calls:
            None
    """
    for P in instance.Pointers:
        if Center in P.list and P.covered == False:
            P.covered = True

def checkStatus(instance):
    """ Checks to see if all of the points have been covered.
        Runtime: O(P) (amount of points)

        Args:
            instance  (Instance.Instance)    - Instance object with the points to count.

        Returns:
            Boolean   (Booleam)              - True or False depending on whether all of the points are covered.

        Globals:
            None

        Called By:
            greedy()

        Calls:
            None
    """
    for P in instance.Pointers:
        if P.covered == False:
            return False

    return True

def greedy(instance):
    """ Algorithm to determine the Centers that cover all of the points.
        Runtime: O((C^2)P)

        Args:
            instance  (Instance.Instance)    - Instance object with the points to count.

        Returns:
            Set       (List)                 - A list of centers that cover all of the Points or an empty set is no solution was found

        Globals:
            None

        Called By:
            main()

        Calls:
            countPointers()
            findMax()
            coverPoints()
            checkStatus()
    """
    Set = []
    while True:
        countPointers(instance)
        Center = instance.Centers[findMax(instance)]
        Set.append(Center)
        coverPoints(Center, instance)
        if checkStatus(instance):
            break

        elif len(Set) == len(instance.Centers): ## All centers have been used and there are still uncovered points.
            print("[ERROR] No Solution Found")
            return []

    return Set

def main(instance):
    """ Main Function for the Greedy Library. Initiates the greedy algorithm.

        Args:
            instance  (Instance.Instance)    - Instance object with the points to count.

        Returns:
            None

        Globals:
            None

        Called By:
            Main.main()

        Calls:
            greedy()
    """
    Set = []
    Set = greedy(instance)
    return Set
