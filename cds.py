'''
Created on Dec 19, 2013

@author: przemek
'''

from johnson import johnson
from makespan import makespan
    
def cds(times):
    jobs_count = len(times)
    machine_count = len(times[0])
    
    perms = []
    times_merged = [[0, sum(job_times)] for job_times in times]
    for i in range(0, machine_count-1):
        for k in range(0, jobs_count):
            times_merged[k][0] += times[k][i];
            times_merged[k][1] -= times[k][i];
        perms.append(johnson(times_merged))
     
    return min(perms, key=lambda p: makespan(p, times))
