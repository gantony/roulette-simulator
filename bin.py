class Bin(object):
    def __init__(self, * outcomes):
        self.outcomes = frozenset(outcomes)

    def add(self, outcome):
        self.outcomes |= frozenset([outcome])

    def __str__(self):
        return "[%s]" % ", ".join(map(str, self.outcomes))
