import unittest
from Geotech.Soil.spt_sample import SplitSpoonSample


class TestSplitSpoonSample(unittest.TestCase):
    spt = SplitSpoonSample(5, 5.5, 30)
    equal_spt = SplitSpoonSample(5, 5.5, 30)
    not_equal_spt = SplitSpoonSample(10, 10.5, 18)

    def test_length(self):
        expected = 0.5
        self.assertAlmostEqual(expected, self.spt.length, 1)

    def test_equal(self):
        self.assertEqual(self.spt, self.equal_spt)

    def test_not_equal(self):
        self.assertNotEqual(self.spt, self.not_equal_spt)


if __name__ == '__main__':
    unittest.main()
