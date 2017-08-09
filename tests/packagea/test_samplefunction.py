import unittest
import packagea.samplefunction as samplefunction_module


class TestSampleModule(unittest.TestCase):

    def test_uppercase(self):
        str = 'abc'
        self.assertEqual(str.upper(), samplefunction_module.uppercase(str))

if __name__ == '__main__':
    unittest.main()
