import unittest

from src.weather.hypothesis_1 import draw_conclusion


class TestHypothesis1(unittest.TestCase):

    def test_draw_conclusion_creates_a_file(self):
        draw_conclusion()
        self.assertTrue(file_exists("hypothesis_1_results.txt"))
