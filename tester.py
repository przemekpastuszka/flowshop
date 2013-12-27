'''
Created on 27-12-2013

@author: pastuszka
'''

from makespan import makespan
from cds import cds

for i in range(1,17):
    with open('testcases/bat' + str(i)) as f:
        testcase = eval(f.read())
        
        print "Test case ", i
        best_perm = cds(testcase)
        print "CDS result: ", makespan(best_perm, testcase)