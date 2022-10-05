import unittest
from Geotech.Soil.soil_layer import SoilLayer
from Geotech.Soil.spt_sample import SplitSpoonSample


class TestSoilLayer(unittest.TestCase):
    layer = SoilLayer(0, 10, "Stiff clay")
    equal_layer = SoilLayer(0, 10, "Stiff clay")
    not_equal_layer = SoilLayer(10, 15, "Sand")
    samples = [
        SplitSpoonSample(1.0, 1.5, 10),
        SplitSpoonSample(5.0, 5.5, 12)
    ]

    def setUp(self) -> None:
        self.layer.add_spt_samples(self.samples)
        self.equal_layer.add_spt_samples(self.samples)
        self.not_equal_layer.add_spt_samples(self.samples)

    def test_length(self):
        expected = 10
        self.assertAlmostEqual(expected, self.layer.length(), 1)

    def test_equal(self):
        self.assertTrue(self.layer == self.equal_layer)

    def test_not_equal(self):
        self.assertFalse(self.layer == self.not_equal_layer)


if __name__ == '__main__':
    unittest.main()
