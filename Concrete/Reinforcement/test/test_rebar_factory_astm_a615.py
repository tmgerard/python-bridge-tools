import unittest

from Concrete.Reinforcement.rebar_factory_astm_a615 import RebarFactoryASTM_A615
from Concrete.Reinforcement.deformed_rebar import DeformedRebar


class TestRebarFactoryASTM_A615(unittest.TestCase):
    number_four_bar = DeformedRebar(4, 0.668, 0.500, 0.20, 1.571)

    def test_get_number_4_bar(self):
        factory = RebarFactoryASTM_A615()
        actual = factory.get_rebar_designation(4)

        self.assertEqual(self.number_four_bar, actual)


if __name__ == '__main__':
    unittest.main()
