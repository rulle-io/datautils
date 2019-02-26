from unittest import TestCase

from datautils import hole_filter_str


class TestDataUtils(TestCase):

    def test_input_zero(self):
        f_input = []
        expected = []
        f_output = hole_filter_str(data_input=f_input)
        self.assertEqual(f_output, expected)

    def test_input_invalid(self):
        f_input = ["one", "stop", "shop"]
        with self.assertRaises(ValueError):
            hole_filter_str(data_input=f_input)

    def test_input_unsorted(self):
        f_input = ["2018-01-05", "2018-01-01"]
        with self.assertRaises(ValueError):
            hole_filter_str(data_input=f_input)

    def test_input_one(self):
        f_input = ["2018-01-01"]
        expected = []
        f_output = hole_filter_str(data_input=f_input)
        self.assertEqual(f_output, expected)

    def test_one_hole(self):
        f_input = ["2018-01-01", "2018-01-03"]
        expected = ["2018-01-02"]
        f_output = hole_filter_str(data_input=f_input)
        self.assertEqual(f_output, expected)

    def test_one_hole_hours(self):
        f_input = ["2018-01-03T08", "2018-01-03T10"]
        expected = ["2018-01-03T09"]
        f_output = hole_filter_str(data_input=f_input, dt_format ='%Y-%m-%dT%H', units='hours')
        self.assertEqual(f_output, expected)

    def test_one_hole_unsorted(self):
        f_input = ["2018-01-03", "2018-01-01"]
        expected = ["2018-01-02"]
        f_output = hole_filter_str(data_input=f_input, is_sorted=False)
        self.assertEqual(f_output, expected)

    def test_one_hole_diff_format(self):
        f_input = ["20180101", "20180103"]
        expected = ["20180102"]
        f_output = hole_filter_str(data_input=f_input, dt_format ='%Y%m%d')
        self.assertEqual(f_output, expected)

    def test_two_holes(self):
        f_input = ["2018-01-01", "2018-01-03", "2018-01-05"]
        expected = ["2018-01-02", "2018-01-04"]
        f_output = hole_filter_str(data_input=f_input)
        self.assertEqual(f_output, expected)
