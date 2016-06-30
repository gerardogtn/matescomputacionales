class Derivation:
    """A class that stores derivations of a string in a cfg"""

    def __init__(self):
        self.__data = []

    def add(self, string, variablePosition):
        self.__data.append((string, variablePosition))

    def pop(self):
        return self.__data.pop()

    def clear(self):
        self.__data = []
    
    def isEmpty(self):
        return len(self.__data) == 0
