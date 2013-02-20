import unittest
import subprocess


class RunTest(unittest.TestCase):
    def test_import(self):
        subprocess.check_call("wiw-smsgate --test --help", shell=True)

if __name__ == '__main__':
    unittest.main()
