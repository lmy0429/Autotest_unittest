import unittest

discover = unittest.defaultTestLoader.discover(
    start_dir='./testcase',
    pattern='*.py'
)
runner = unittest.TextTestRunner()
runner.run(discover)
