'''
Created on 27-12-2013

@author: pastuszka
'''

from makespan import makespan
from cds import cds
from genetic import genetic
from neh import neh
from optimal import optimal
from time import time
        
def test(f, testcase):
    start = time()
    result = makespan(f(testcase), testcase)
    end = time()
    return (result, end - start)

for i in range(1,17):
    with open('testcases/bat' + str(i)) as f:
        testcase = eval(f.read())
        
        a = test(cds, testcase)
        b = test(neh, testcase)
        c = test(genetic, testcase)
        print ' '.join([str(x[0]) for x in [a, b, c]] + [str(x[1]) for x in [a, b, c]])
