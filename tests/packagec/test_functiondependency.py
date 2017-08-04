import unittest
import sys
from mock import patch, MagicMock
import packagec.functiondependency as functiondependency

# Examples of mocking by patching
class TestFunctionDependency(unittest.TestCase):
    @patch('packagec.functiondependency.module')
    def test_upperCase_stubbed_function(self, samplefunctionmodulemock):
        # Arrange
        def upperCase(str):
            return str.upper()

        samplefunctionmodulemock.upperCase.side_effect = upperCase
        testString = 'abc'

        # Act
        result = functiondependency.upperCase(testString)

        # Assert
        self.assertEqual(result, testString.upper())
        samplefunctionmodulemock.upperCase.assert_called_once_with(testString)

    @patch('packagec.functiondependency.module')
    def test_upperCase_stubbed_value(self, samplefunctionmodulemock):
        # Arrange
        testString = 'abc'
        samplefunctionmodulemock.upperCase.return_value = 'ABC'

        # Act
        result = functiondependency.upperCase(testString)

        # Assert
        self.assertEqual(result, testString.upper())
        samplefunctionmodulemock.upperCase.assert_called_once_with(testString)

if __name__ == '__main__':
    unittest.main()