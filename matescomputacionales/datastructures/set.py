class Set:
    """ A simple set class that delegates its behaviour to a list"""

    def __init__(self, entries=[]):
        self.entries = []
        self.addAll(entries)
        pass

    def add(self, entry):
        """ If entry is not in set, add entry to set"""
        if (entry not in self.entries):
            self.entries.append(entry)

    def addAll(self, entries):
        """ Add all entries to set

        Keyword arguments:
        entries -- a list of objects to add to set.
        """
        for e in entries:
            self.add(e)

    def remove(self, entry):
        """ If entry is in set, remove it form set."""
        if (entry in self.entries):
            self.entries.remove(entry)

    def removeAll(self, entries):
        """ Remove all entries in set

        Keyword arguments:
        entries -- a list of objects to remove from set.
        """
        for e in entries:
            remove(e)

    def contains(self, entry):
        """ Return true if entry is in set. """
        return entry in self.entries

    def isEmpty(self):
        """ Return true if there are no elements in set """
        return len(self.entries) == 0

    def size(self):
        """ Return the number of elements in set"""
        return len(self.entries)

    # Return the string representation of self.entries
    def __str__(self):
        return str(self.entries)

    def __eq__(self, other):
        """ Return true if both entries are equal

        Two entries are equal if:
            - they are both of type set AND
            - have the same number of elements AND
            - all the entries in one are entries in the other"""
        eq = isinstance(other, Set)
        eq = eq and self.size() == other.size()
        for e in self.entries:
            eq = eq and other.contains(e)
        return eq
