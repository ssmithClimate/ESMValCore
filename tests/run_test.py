# coding=utf-8
"""
Script to run the tests and generating the code coverage report
"""
import coverage
import unittest
import os
work_path = os.path.abspath('.')
cov = coverage.Coverage(include=os.path.join(work_path, '..', '*'),
                        omit=os.path.join(work_path, '*'),)
cov.set_option("run:branch", True)
cov.set_option("html:title", 'Coverage report for ESMValTool')

cov.start()
suite = unittest.TestLoader().discover('.')
unittest.TextTestRunner(verbosity=2).run(suite)
cov.stop()

cov.save()
cov.report()
cov.html_report()
