import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod #Run once (like creating a database)
    def setUpClass(cls):
        print('setupClass')
    
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
    def setUp(self): #Runs for every test case
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue','Smith', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'


        self.assertEqual(self.emp_1.email,'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email,'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname,'Corey Schafer')
        self.assertEqual(self.emp_2.fullname,'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'            

        self.assertEqual(self.emp_1.fullname,'John Schafer')
        self.assertEqual(self.emp_2.fullname,'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

#Mocking: To test things out of your control (like broken URLs)
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule,'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule,'Bad Response!')


if __name__ == '__main__':
    unittest.main()


"""
BEST PRACTICES

* Tests should be isolated
    -> Your test shouldn't rely on other tests or affect other tests
    -> Your test should run independent of other tests

* Test-driven development
    -> Write the test cases first and then develop code which passes it
    -> Sounds odd, but it's good
    -> Not mandatory
"""