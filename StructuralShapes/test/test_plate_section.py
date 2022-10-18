import unittest


from StructuralShapes.BuiltUpShapes.plate_section import PlateSection


class TestPlateSection(unittest.TestCase):

    plate = PlateSection(6.0, 2.0)

    def test_ix(self):
        expected = 4.0
        actual = self.plate.ix
        self.assertEqual(expected, actual)

    def test_iy(self):
        expected = 36.0
        actual = self.plate.iy
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
