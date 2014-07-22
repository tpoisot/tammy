#! /usr/bin/env python3

import unittest
import os

if __name__ == "__main__":
   testsuite = unittest.TestLoader().discover('./tests', pattern="*py")
   unittest.TextTestRunner(verbosity=1).run(testsuite)
