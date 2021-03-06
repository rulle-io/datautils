import datetime
from unittest import TestCase

from datautils import date_hole_printer, generate_dt_list


class TestDataUtils(TestCase):

    def test_generate_date_list(self):
        start_p = datetime.date(2018, 1, 1)
        end_p = datetime.date(2018, 1, 3)
        expected = [datetime.date(2018, 1, 1), datetime.date(2018, 1, 2)]
        f_output = generate_dt_list(period_start_dt=start_p, period_end_dt=end_p, units='days')
        self.assertEqual(f_output, expected)

    def test_input_empty_interval(self):
        f_input = None
        with self.assertRaises(ValueError):
            date_hole_printer(dates_list=f_input, period_start="2018-01-01", period_end="2018-01-02")

    def test_input_invalid_input(self):
        f_input = ["one", "stop", "shop"]
        with self.assertRaises(ValueError):
            date_hole_printer(dates_list=f_input, period_start="2018-01-01", period_end="2018-01-01")

    def test_input_invalid_unit(self):
        f_input = []
        with self.assertRaises(ValueError):
            date_hole_printer(dates_list=f_input, period_start="2018-01-01", period_end="2018-01-03", units='weeks')

    def test_input_one(self):
        p_start = "2018-01-01"
        p_end = "2018-01-02"
        f_input = ["2018-01-01"]
        expected = []
        f_output = date_hole_printer(dates_list=f_input, period_start=p_start, period_end=p_end)
        self.assertEqual(f_output, expected)

    def test_one_hole(self):
        p_start = "2018-01-01"
        p_end = "2018-01-03"
        f_input = ["2018-01-01"]
        expected = ["2018-01-02"]
        f_output = date_hole_printer(dates_list=f_input, period_start=p_start, period_end=p_end)
        self.assertEqual(f_output, expected)

    def test_one_month(self):
        f_input = ['2020-12-01', '2020-12-02', '2020-12-03', '2020-12-04', '2020-12-05', '2020-12-06', # '2020-12-07',
                   '2020-12-08', '2020-12-09', '2020-12-10', '2020-12-11', '2020-12-12', '2020-12-13', '2020-12-14',
                   '2020-12-15', '2020-12-16', '2020-12-17', '2020-12-18', '2020-12-19', '2020-12-20', # '2020-12-21',
                   '2020-12-22', '2020-12-23', '2020-12-24', '2020-12-25', '2020-12-26', '2020-12-27', '2020-12-28',
                   '2020-12-29', '2020-12-30']
        expected = ['2020-12-07', '2020-12-21']
        f_output = date_hole_printer(dates_list=f_input)
        self.assertEqual(f_output, expected)

    def test_one_hole_hours(self):
        p_start = "2018-01-01T08"
        p_end = "2018-01-01T10"
        f_input = ["2018-01-01T08"]
        expected = ["2018-01-01T09"]
        f_output = date_hole_printer(dates_list=f_input, period_start=p_start, period_end=p_end, dt_format='%Y-%m-%dT%H',
                                     units='hours')
        self.assertEqual(f_output, expected)


# '2020-12-01', '2020-12-02', '2020-12-03', '2020-12-04', '2020-12-05', '2020-12-06', '2020-12-07', '2020-12-08', '2020-12-09', '2020-12-10', '2020-12-11', '2020-12-12', '2020-12-13', '2020-12-14', '2020-12-15', '2020-12-16', '2020-12-17', '2020-12-18', '2020-12-19', '2020-12-20', '2020-12-21', '2020-12-22', '2020-12-23', '2020-12-24', '2020-12-25', '2020-12-26', '2020-12-27', '2020-12-28', '2020-12-29', '2020-12-30'
    def test_one_hole_diff_format(self):
        p_start = "20180101"
        p_end = "20180103"
        f_input = ["20180101"]
        expected = ["20180102"]
        f_output = date_hole_printer(dates_list=f_input, period_start=p_start, period_end=p_end, dt_format='%Y%m%d')
        self.assertEqual(f_output, expected)

    def test_two_holes(self):
        p_start = "2018-01-01"
        p_end = "2018-01-05"
        f_input = ["2018-01-01", "2018-01-03"]
        expected = ["2018-01-02", "2018-01-04"]
        f_output = date_hole_printer(dates_list=f_input, period_start=p_start, period_end=p_end)
        self.assertEqual(f_output, expected)

    def test_one_hole_no_start_end(self):
        f_input = ["2018-01-01", "2018-01-03"]
        expected = ["2018-01-02"]
        f_output = date_hole_printer(dates_list=f_input)
        self.assertEqual(f_output, expected)

    def test_one_hole_no_start_end(self):
        f_input = ["2018-01-05", "2018-01-03", "2018-01-01"]
        expected = ["2018-01-02", "2018-01-04"]
        f_output = date_hole_printer(dates_list=f_input, is_sorted=False)
        self.assertEqual(f_output, expected)
        
#if __name__ == '__main__':
#    unittest.main()