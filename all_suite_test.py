import unittest
from unittest.loader import makeSuite
from test_cases.invalid_login_to_the_system import TestInvalidLoginPage
from test_cases.add_a_player import TestAddPlayer
from test_cases.edit_match_player import TestEditMatchPlayer
from test_cases.sign_out import TestSignOut
from test_cases.add_match_to_last_created_player import TestAddMatchPlayer
from test_cases.add_a_player_change_leg import TestAddPlayerChange
from test_cases.login_to_the_system import TestLoginPage
from test_cases.change_language import TestLoginPageChangeLanguage
from test_cases.framework import TestMediumPage
def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestInvalidLoginPage))
   test_suite.addTest(makeSuite(TestAddPlayer))
   test_suite.addTest(makeSuite(TestEditMatchPlayer))
   test_suite.addTest(makeSuite(TestSignOut))
   test_suite.addTest(makeSuite(TestAddMatchPlayer))
   test_suite.addTest(makeSuite(TestAddPlayerChange))
   test_suite.addTest(makeSuite(TestLoginPageChangeLanguage))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestMediumPage))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())
