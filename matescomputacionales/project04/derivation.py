class Derivation:
    """A class that stores derivations of a string in a cfg"""

    def __init__(self, entries=[]):
        self.__data = []
        self.addAll(entries)

    def add(self, string, variablePosition):
        self.__data.append((string, variablePosition))

    def addAll(self, entries):
        for e in entries:
            self.add(e[0], e[1])

    def pop(self):
        return self.__data.pop()

    def clear(self):
        self.__data = []

    def isEmpty(self):
        return len(self.__data) == 0

    def __str__(self):
        return str(self.__data)

    def __eq__(self, other):
        """ Return true if both entries are equal

        Two entries are equal if:
            - they are both of type set AND
            - their --data is the same
        """
        eq = isinstance(other, Derivation)
        eq = eq and self.__data == other.__data
        return eq
