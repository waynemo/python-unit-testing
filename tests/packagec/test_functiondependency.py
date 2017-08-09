import unittest
from mock import patch
import packagec.functiondependency as functiondependency


# Examples of mocking by patching
class TestFunctionDependency(unittest.TestCase):
    @patch('packagec.functiondependency.samplefunction_module')
    def test_uppercase_stubbed_function(self, samplefunctionmodulemock):
        # Arrange
        def uppercase(str):
            return str.upper()

        samplefunctionmodulemock.uppercase.side_effect = uppercase
        test_string = 'abc'

        # Act
        result = functiondependency.uppercase(test_string)

        # Assert
        self.assertEqual(result, test_string.upper())
        samplefunctionmodulemock.uppercase.assert_called_once_with(test_string)

    @patch('packagec.functiondependency.samplefunction_module')
    def test_uppercase_stubbed_value(self, samplefunctionmodulemock):
        # Arrange
        test_string = 'abc'
        samplefunctionmodulemock.uppercase.return_value = 'ABC'

        # Act
        result = functiondependency.uppercase(test_string)

        # Assert
        self.assertEqual(result, test_string.upper())
        samplefunctionmodulemock.uppercase.assert_called_once_with(test_string)

if __name__ == '__main__':
    unittest.main()