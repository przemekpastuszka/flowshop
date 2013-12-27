'''
Created on 27-12-2013

@author: pastuszka
'''

from random import shuffle, randrange

def genetic(times, population_size, num_of_epochs):
    job_count = len(times)
    population = [list(range(1, job_count + 1)) for _ in range(0, population_size)]
    for individual in population:
        shuffle(individual)

def translate(x, d):
    while x in d and x != d[x]:
        x = d[x]
    return x

def pmx(a, b):
    length = len(a)
    left = randrange(0, length + 1)
    right = randrange(left, length + 1)
    
    a2 = a[left:right]
    b2 = b[left:right]
    d = dict(zip(a2, b2))
    d_inv = dict(zip(b2, a2))
   
    child1 = map(lambda x: translate(x, d_inv), a[0:left]) + b2 + map(lambda x: translate(x, d_inv), a[right:length + 1])
    child2 = map(lambda x: translate(x, d), b[0:left]) + a2 + map(lambda x: translate(x, d), b[right:length + 1])
    
    return [child1, child2]

print pmx([1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 4, 6, 9, 2, 1, 7, 8, 3])        
    
    
        
    