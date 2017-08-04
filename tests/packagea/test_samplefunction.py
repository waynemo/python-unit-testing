import unittest
import packagea.samplefunction as module

class TestSampleModule(unittest.TestCase):

    def test_upperCase(self):
        str = 'abc'
        self.assertEqual(str.upper(), module.upperCase(str))

if __name__ == '__main__':
    unittest.main()
