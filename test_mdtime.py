import unittest

import mdtime

class MDTimeTestCase(unittest.TestCase):
    # def testTPRTimeEqualCPTTime(self):
    def testGetCPTTime(self):
        f = 'test_files/test_case1_completed.cpt'
        assert mdtime.get_cpt_time(f) == '2000.00000'

    def testGetCPTTimeNonexistentCPTFile(self):
        f = '____nonexistent____.cpt'
        assert mdtime.get_cpt_time(f) == '{0} does not exist'.format(f)

    def testGetCPTTimeCorruptedCPTFile(self):
        f = 'corrupted.cpt'
        assert mdtime.get_cpt_time(f) == '{0} is corrupted'.format(f)


if __name__ == "__main__":
    unittest.main(exit=False)
