import unittest
from TestScripts.test_login import LoginTest

# Get all TestScripts from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)


