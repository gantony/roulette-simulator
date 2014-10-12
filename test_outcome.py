import unittest
from outcome import Outcome


class TestOutcome(unittest.TestCase):
    def setUp(self):
        self.output = Outcome("Red", 11)
        self.same = Outcome("Red", 11)
        self.different = Outcome("Black", 11)

    def testWinAmount(self):
        payout = self.output.winAmount(3)
        self.assertEqual(payout, 3*11)

    def testEquality(self):
        self.assertEqual(self.output, self.same)
        self.assertNotEqual(self.output, self.different)

    def testHashEquality(self):
        self.assertEqual(hash(self.output), hash(self.same))
        self.assertNotEqual(hash(self.output), hash(self.different))

    def testStr(self):
        self.assertEqual("%s" % self.output, "Red (11:1)")

if __name__ == '__main__':
    unittest.main()
