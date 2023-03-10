"""
Enumerable Magic - Does My List Include This?

Create a method that accepts a list and an item, and returns true if the item belongs to the list, otherwise false.

Categories: Fundamentals
"""

def include(arr, item):
    return item in arr  # in operator of arr


# TODO
# learn __import__

"""
Observations:
include = list.__contains__                         # Clever use
from operator import contains as include            # Another clever use
include = lambda a,i: i in a                        # Lambda usage
include = lambda arr,item: arr.count(item) == 0     # use of count method of list
include = __import__("operator").contains           # Check the TODO item(s)
"""