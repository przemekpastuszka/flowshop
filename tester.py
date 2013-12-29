'''
Created on 27-12-2013

@author: pastuszka
'''

from makespan import makespan
from cds import cds
from genetic import genetic
from neh import neh

for i in range(1,17):
    with open('testcases/bat' + str(i)) as f:
        testcase = eval(f.read())
        
        print "Test case ", i
        print "CDS result: ", makespan(cds(testcase), testcase)
        #print "genetic result: ", makespan(genetic(testcase, 100, 100), testcase)
        print "NEH result: ", makespan(neh(testcase), testcase)