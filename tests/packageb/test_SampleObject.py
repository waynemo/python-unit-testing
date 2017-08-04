import unittest
from packageb.SampleObject import SampleObject
 
class TestSampleObject(unittest.TestCase):
    def setUp(self):
        self.str = 'abc'
        self.sampleObject = SampleObject(self.str)
 
    def test_upperCase(self):
        self.assertEqual(self.sampleObject.upperCase(), self.str.upper())
 
if __name__ == '__main__':
    unittest.main()