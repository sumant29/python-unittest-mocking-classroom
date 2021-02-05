from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper

class Helper(TestCase):
    def setUp(self):
        self.db = DbHelper()

    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self,Mockdbhelper):
        dbhelper = Mockdbhelper()

        dbhelper.get_maximum_salary.return_value = 50000
        dbhelper.get_minimum_salary.return_value = 5000

        self.assertGreater(dbhelper.get_maximum_salary(),dbhelper.get_minimum_salary())
