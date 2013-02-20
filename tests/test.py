import unittest
import subprocess


class RunTest(unittest.TestCase):
    def test_import(self):
        proc = subprocess.Popen("./wiw-smsgate --help", shell=True,
                                stdout=subprocess.PIPE)
        test = proc.communicate()[0]

if __name__ == '__main__':
    unittest.main()
