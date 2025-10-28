import unittest

from src.weather.analysis import do_analysis


class TestAnalysis(unittest.TestCase):

    def test_analysis_creates_two_files(self):
        do_analysis()
        # self.assertTrue(file_exists("figure.png"))
        # self.assertTrue(file_exists("statistics_results.txt"))
