import sys
import unittest

import mdtime

class CPTTimeTestCase(unittest.TestCase):
    def testGetCPTTime(self):
        t = mdtime.get_cpt_time('test_files/test_case1_completed.cpt')
        self.assertEqual(t, 2000)

    def testGetCPTTimeNonexistentCPTFile(self):
        cpt_f = '____nonexistent____.cpt'
        self.assertRaisesRegexp(
            IOError, '{0} does not exist'.format(cpt_f), 
            mdtime.get_cpt_time, cpt_f)

    def testGetCPTTimeCorruptedCPTFile(self):
        cpt_f = 'test_files/corrupted.cpt'
        self.assertRaisesRegexp(
            IOError, '{0} is corrupted, see the above error'.format(cpt_f),
            mdtime.get_cpt_time, cpt_f)

class TPRTimeTestCase(unittest.TestCase):
    def testGetTPRTime(self):
        t = mdtime.get_tpr_time('test_files/test_case1.tpr')
        self.assertEqual(t, 2000)

    def testGetTPRTimeNonexistentTPRFile(self):
        tpr_f = '____nonexistent____.tpr'
        self.assertRaisesRegexp(
            IOError, '{0} does not exist'.format(tpr_f), 
            mdtime.get_tpr_time, tpr_f)

    def testGetTPRTimeCorruptedTPRFile(self):
        tpr_f = 'test_files/corrupted.tpr'
        self.assertRaisesRegexp(
            IOError, '{0} is corrupted, see the above error'.format(tpr_f), 
            mdtime.get_tpr_time, tpr_f)

class CPTLessThanTPRTestCase(unittest.TestCase):
    def testCPTTimeEqualTPRTime(self):
        cpt_f = 'test_files/test_case1_completed.cpt'
        tpr_f = 'test_files/test_case1.tpr'
        self.assertFalse(mdtime.cpt_less_than_tpr(cpt_f, tpr_f))

    def testCPTTimeLessThanTPRTime(self):
        cpt_f = 'test_files/test_case2_uncompleted.cpt'
        tpr_f = 'test_files/test_case2.tpr'
        self.assertTrue(mdtime.cpt_less_than_tpr(cpt_f, tpr_f))

class MainTestCase(unittest.TestCase):
    def testCompletedCPTTime(self):
        mdtime.main(['-f', 'test_files/test_case1_completed.cpt'])
        output = sys.stdout.getvalue()
        self.assertEqual(output, '2000') # unit: ns

    def testUncompletedCPTTime(self):
        mdtime.main(['-f', 'test_files/test_case2_uncompleted.cpt'])
        output = sys.stdout.getvalue()
        self.assertEqual(output, '52') # unit: ns

    def testTPRTime(self):
        mdtime.main(['-f', 'test_files/test_case1.tpr'])
        output = sys.stdout.getvalue()
        self.assertEqual(output, '2000') # unit: ns

    def testCPTTimeLessTPRTime(self):
        mdtime.main(['--comp', 
                     'test_files/test_case2_uncompleted.cpt',
                     'test_files/test_case2.tpr'])
        self.assertEqual(sys.stdout.getvalue(), 'True')

    def testCPTTimeEqualTPRTime(self):
        mdtime.main(['--comp', 
                     'test_files/test_case1_completed.cpt',
                     'test_files/test_case1.tpr'])
        self.assertEqual(sys.stdout.getvalue(), 'False')

if __name__ == "__main__":
    unittest.main()
