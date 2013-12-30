'''
Created on 30-12-2013

@author: pastuszka
'''

from itertools import permutations
from makespan import makespan

def optimal(times):
    job_count = len(times)
    return min(permutations(range(job_count)), key = lambda x: makespan(x, times))
        