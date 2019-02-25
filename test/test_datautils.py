from unittest import TestCase

from datautils import hole_filter_str


class TestDataUtils(TestCase):

    def test_input_zero(self):
        self.f_input = []
        self.expected = []
        self.f_output = hole_filter_str(data_input=self.f_input, dt_format ='%Y-%m-%d')
        self.assertEqual(self.f_output, self.expected)

    def test_input_one(self):
        self.f_input = ["2018-01-01"]
        self.expected = []
        self.f_output = hole_filter_str(data_input=self.f_input, dt_format ='%Y-%m-%d')
        self.assertEqual(self.f_output, self.expected)

    def test_one_hole(self):
        self.f_input = ["2018-01-01", "2018-01-03"]
        self.expected = ["2018-01-02"]
        self.f_output = hole_filter_str(data_input=self.f_input, dt_format ='%Y-%m-%d')
        self.assertEqual(self.f_output, self.expected)

    def test_two_holes(self):
        f_input = ["2018-01-01", "2018-01-03", "2018-01-05"]
        expected = ["2018-01-02", "2018-01-04"]

        f_output = hole_filter_str(data_input=f_input, dt_format ='%Y-%m-%d')
        self.assertEqual(f_output, expected)



#             output, dict) or isinstance(output, list))
    #
    #         task = BackfillsDump(date=datetime.today())
    #         output = False
    #         try:
    #             output = task.output()
    #         except (RuntimeError, TypeError, NameError):
    #             pytest.fail("Output is not well behaved")
    #         assert (isinstance(output, luigi.target.Target) or isinstance(
    #             output, dict) or isinstance(output, list))