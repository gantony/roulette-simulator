# Need to add comments!
class Outcome(object):
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return "%s (%d:1)" % (self.name, self.odds)

    def winAmount(self, amount):
        return self.odds * amount
