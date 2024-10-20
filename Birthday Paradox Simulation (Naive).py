# Veryfying Birthday Paradox Using Python Ramdom Module

import random
total_num_exp = 2
exp_performed = 0
num_favorable_event = 0
while exp_performed < total_num_exp:
    l = []

    for i in range (23):
        l.append(random.randint(0,366))
    l.sort()
    print(l)
    for i in range (22):
        if l[i] == l[i+1]:
            num_favorable_event += 1
            print(l[i],'is repeating')
            break
    exp_performed += 1

print('Probability of Repetition =',(num_favorable_event/total_num_exp))
        
