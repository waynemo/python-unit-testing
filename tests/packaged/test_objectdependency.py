import unittest
from mock import patch
import packaged.objectdependency as objectdependency


class TestSampleObject(unittest.TestCase):

    @patch('packaged.objectdependency.SampleObject')
    def test_uppercase_mock_object(self, sampleobjectmock):
        # Arrange
        test_string = 'abc'
        sampleobjectmock.return_value.uppercase.return_value = 'ABC'

        # Act
        result = objectdependency.uppercase(test_string)

        # Assert
        self.assertEqual(result, test_string.upper())
        sampleobjectmock.assert_called_once_with(test_string)

if __name__ == '__main__':
    unittest.main()