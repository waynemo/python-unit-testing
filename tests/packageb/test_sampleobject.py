import unittest
from packageb.sampleobject import SampleObject


class TestSampleObject(unittest.TestCase):
    def setUp(self):
        self.str = 'abc'
        self.sampleObject = SampleObject(self.str)
 
    def test_uppercase(self):
        self.assertEqual(self.sampleObject.uppercase(), self.str.upper())
 
if __name__ == '__main__':
    unittest.main()