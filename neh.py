'''
Created on 29-12-2013

@author: pastuszka
'''

from makespan import makespan

def neh(times):
    jobs_with_total_times = [(job_id, sum(job)) for job_id, job in enumerate(times)]
    order = []
    for job in sorted(jobs_with_total_times, key=lambda x: x[1], reverse = True):
        candidates = []
        for i in range(0, len(order) + 1):
            candidate = order[:i] + [job[0]] + order[i:]
            candidates.append((candidate, makespan(candidate, times)))
        order = min(candidates, key = lambda x: x[1])[0]
    return order