import unittest
from Geotech.Soil.parse_boring_file import BoringFileParser
from Geotech.Soil.soil_boring import SoilBoring
from Geotech.Soil.soil_layer import SoilLayer
from Geotech.Soil.spt_sample import SplitSpoonSample


class MyTestCase(unittest.TestCase):

    # examples from ARDOT job number 080439
    boring_string = '1 107+91 536.6 3\' Left of Construction Centerline'
    soil_layer_string = '2  82 0 2.8 Brown and Gray Clay with Gravel and Cobbles (Sandstone Fragments)'
    spt_string = '3 2.8  2.8 10(0")'

    # sample test should have two borings with 2 and 1 layers respectively
    test_lines = [
        '1 100+00 100 3\' Left of Construction Centerline',
        '2 20 0 5 Clay',
        '3 2.5 3.0 8',
        '2 20 5 15 Sandy Clay',
        '3 7.5 8.0 15',
        '3 12.5 13.0 19',
        '1 125+00 96.0 Centerline Construction',
        '2 20 0 20 Brown Clay',
        '3 10 10.5 30'
    ]

    parser = BoringFileParser()

    def setUp(self) -> None:
        self.borings = [
            SoilBoring(10000, 100, '3\' Left of Construction Centerline'),
            SoilBoring(12500, 96, 'Centerline Construction')
        ]

        boring_one_soil_layers = [
            SoilLayer(0, 5, 'Clay'),
            SoilLayer(5, 15, 'Sandy Clay')
        ]

        boring_one_soil_layers[0].add_spt_samples([SplitSpoonSample(2.5, 3.0, 8)])
        boring_one_soil_layers[1].add_spt_samples(
            [SplitSpoonSample(7.5, 8.0, 15), SplitSpoonSample(12.5, 13.0, 19)]
        )

        boring_two_soil_layers = [
            SoilLayer(0, 20, 'Brown Clay')
        ]

        boring_two_soil_layers[0].add_spt_samples([SplitSpoonSample(10, 10.5, 30)])

        self.borings[0].add_soil_layers(boring_one_soil_layers)
        self.borings[1].add_soil_layers(boring_two_soil_layers)

    def test_parse_boring_location(self):
        expected = SoilBoring(10791, 536.6, '3\' Left of Construction Centerline')
        actual = self.parser._BoringFileParser__parse_boring_location(self.boring_string)
        self.assertEqual(expected, actual)

    def test_parse_soil_layer(self):
        expected = SoilLayer(0.0, 2.8, 'Brown and Gray Clay with Gravel and Cobbles (Sandstone Fragments)')
        actual = self.parser._BoringFileParser__parse_soil_layer(self.soil_layer_string)
        self.assertEqual(expected, actual)

    def test_parse_spt_sample(self):
        expected = SplitSpoonSample(2.8, 2.8, 10)
        actual = self.parser._BoringFileParser__parse_spt_sample(self.spt_string)
        self.assertEqual(expected, actual)

    def test_parse(self):
        expected = self.borings
        actual = self.parser.parse(self.test_lines)
        self.assertEqual(expected[0], actual[0])
        self.assertEqual(expected[1], actual[1])


if __name__ == '__main__':
    unittest.main()
