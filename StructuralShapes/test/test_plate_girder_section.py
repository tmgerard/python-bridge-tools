import unittest


from StructuralShapes.BuiltUpShapes.plate_girder_section import PlateGirderSection
from StructuralShapes.BuiltUpShapes.plate_section import PlateSection


class TestPlateGirderSection(unittest.TestCase):
    pg = PlateGirderSection(PlateSection(12.0, 1.0),
                            PlateSection(1.0, 42.0),
                            PlateSection(13.0, 1.0))

    def test_area(self):
        expected = 67.0
        actual = self.pg.area
        self.assertEqual(expected, actual)

    def test_base_to_centroid(self):
        expected = 21.68
        actual = self.pg.base_to_centroid
        self.assertAlmostEqual(expected, actual, 2)

    def test_cw(self):
        expected = 149035.52
        actual = self.pg.cw
        self.assertAlmostEqual(expected, actual, 2)

    def test_depth(self):
        expected = 44.0
        actual = self.pg.depth
        self.assertEqual(expected, actual)

    def test_ix(self):
        expected = 17725.43
        actual = self.pg.ix
        self.assertAlmostEqual(expected, actual, 2)

    def test_iy(self):
        expected = 330.58
        actual = self.pg.iy
        self.assertAlmostEqual(expected, actual, 2)

    def test_j(self):
        expected = 22.33
        actual = self.pg.j
        self.assertAlmostEqual(expected, actual, 2)

    def test_rx(self):
        expected = 16.27
        actual = self.pg.rx
        self.assertAlmostEqual(expected, actual, 2)

    def test_ry(self):
        expected = 2.22
        actual = self.pg.ry
        self.assertAlmostEqual(expected, actual, 2)


if __name__ == '__main__':
    unittest.main()
