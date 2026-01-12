import unittest
from unittest.mock import patch, Mock

from main import (greet_person, is_cold_f, TEMPERATURE_THRESHOLD)

class TestMainApp(unittest.TestCase):

    @patch('builtins.input', side_effect=['alice'])
    @patch('builtins.print')

    # def test_greetperson(self) -> None:
    #     '''Say hello to alice !'''
    #     greet_person()
    #     expected_calls = [
    #         unittest.mock.call("Howdy, alice !")
    #     ]
    #     mock_print.assert_has_calls(expected_calls)
    
    def test_is_cold_f_70(self) -> None:
        '''Tests is_cold_f for 70'''
        self.assertFalse(is_cold_f(TEMPERATURE_THRESHOLD+2))
    
    def test_is_cold_f_freezing(self) -> None:
        '''Tests is_cold_f for 32'''
        self.assertTrue(is_cold_f(32))

    def test_is_cold_f_boiling(self) -> None:
        '''Tests is_cold_f for 212'''
        self.assertFalse(is_cold_f(212))

if __name__ == "__main__":
    unittest.main()