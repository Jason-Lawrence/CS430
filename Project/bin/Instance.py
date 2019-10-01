"""
This file holds the objects to use for the project.
"""

class Instance:
    def __init__(self):
        self.Centers = []      ##List of centers on the disk
        self.Pointers = []     ##List of points outside the disk

class Centers:
    def __init__(self, id, x, y):
        self.id = id           ##Center Identifier
        self.x = x             ## X coordinate
        self.y = y             ## Y coordinate
        self.count = 0         ## Number of pointers covered by the center

class Points:
    def __init__(self, x, y):
        self.x = x              ## X coordinates
        self.y = y              ## Y coordinate
        self.covered = False    ## If the point is covered by a Center in the set
        self.list = []          ##
