import unittest
from outcome import Outcome
from bin import Bin


class TestBin(unittest.TestCase):
    def setUp(self):
        self.output = Outcome("Red", 11)
        self.other = Outcome("Red-ish", 10)
        self.different = Outcome("Black", 11)

    def testConstructBinWithOneOutcome(self):
        binSingleOutcome = Bin(self.output)
        self.assertEqual(len(binSingleOutcome.outcomes), 1)

    def testConstructBinWithMultipleOutcomes(self):
        binMultipleOutcome = Bin(self.output, self.other, self.different)
        self.assertEqual(len(binMultipleOutcome.outcomes), 3)

    def testCanAddOutcomeToBin(self):
        testBin = Bin()
        self.assertEqual(len(testBin.outcomes), 0)
        testBin.add(self.output)
        self.assertEqual(len(testBin.outcomes), 1)

    def testStrSingleOutcome(self):
        binSingleOutcome = Bin(self.output)
        self.assertEqual("%s" % self.output, "Red (11:1)")

    def testStrMultipleOutcomes(self):
        binMultipleOutcome = Bin(self.output, self.other, self.different)
        self.assertEqual("%s" % binMultipleOutcome, "[Black (11:1), Red-ish (10:1), Red (11:1)]")

if __name__ == '__main__':
    unittest.main()
