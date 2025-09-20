"""
  Handling arguments
"""
import argparse

def argp():
    pars = argparse.ArgumentParser(prog="Report",\
                                     usage='%(prog)s [options]',\
                                     description = 'Generator report',\
                                     exit_on_error = False)
    pars.add_argument('--file', type = str, nargs = '+', help = 'name db.csv')
    pars.add_argument('--report', type = str, nargs = '+', help = 'report name\
                                                         [student-performance/\
                                                          teachers]')
    return pars
