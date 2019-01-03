usage = '''

Expense Tracker CLI.

Usage:
  spent_driver.py init
  spent_driver.py view [<view_category>] [<view_profile>]
  spent_driver.py <amount> <category> [<message>]

'''

from docopt import docopt
from spent import *
from tabulate import tabulate

args = docopt(usage)

if args['init']:
    init()
    print("User Profile Created")

if args['view']:
    category = args['<view_category>']
    profile = args['<view_profile>']
    amount, results = view(category, profile)
    print("Total expense: ", amount)
    print(tabulate(results))

if args['<amount>']:
    try:
        amount = float(args['<amount>'])
        log(amount, args['<category>'], args['<message>'])
    except:
        print(usage)
