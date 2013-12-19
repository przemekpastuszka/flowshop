'''
Created on Dec 19, 2013

@author: przemek
'''

def makespan(perm, times):
    job_count = len(perm)
    machine_count = len(times[0])
    
    makespan = [[0] * (machine_count + 1) for _ in range(0, job_count + 1)]
    for i, job in enumerate(perm):
        for machine in range(0, machine_count):
            makespan[i + 1][machine + 1] = max(makespan[i][machine + 1], makespan[i + 1][machine]) + times[job - 1][machine]
    
    return makespan[job_count][machine_count]