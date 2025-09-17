"""
  Handling arguments
"""

import argparse

pars = argparse.ArgumentParser(description = 'Student performance analysis')
pars.add_argument('--file', type = str, nargs = '+', help = 'name db.csv')
pars.add_argument('--report', type = str, nargs = 1, help = 'report name',\
  default='student-performance')

args = pars.parse_args()
