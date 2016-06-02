class Set:

    def __init__(self):
        self.entries = []
        pass

    def add(self, entry):
        if (entry not in self.entries):
            self.entries.append(entry)

    def addAll(self, entries):
        for e in entries:
            self.add(e)

    def remove(self, entry):
        if (entry in self.entries):
            self.entries.remove(entry)

    def removeAll(self, entries):
        for e in entries:
            remove(e)

    def contains(self, entry):
        return entry in self.entries

    def isEmpty(self):
        return len(self.entries) == 0

    def size(self):
        return len(self.entries)

    def __str__(self):
        return str(self.entries)

    def __eq__(self, other):
        eq = isinstance(other, Set)
        eq = eq and self.size() == other.size()
        for e in self.entries:
            eq = eq and other.contains(e)
        return eq
