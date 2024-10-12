from statistics import *
f = open('result.csv','r') #response times from odns cluster
lines = f.readlines()
f.close()
w = open('analysis_result_1006.txt','a+')
fwd = []
reso = []
i = 0
reso_num = 0
existing = []
for line in lines:
    if line[:-1] == 'new_cluster':
        w.write(f'{i}\n')
        w.write(f'new_cluster\n')
        continue
    i = i+1
    line_sp = line[:-1].split(',')[:-1]
    ip = line_sp[0]

    first = {}
    mea = {}
    var = {}
    num = {}
    delays = {}

    for delay_group in line_sp[1:len(line_sp)]:
        group = delay_group.split(':')
        if len(group) > 1:
            delay_domain = group[0]
            delay = group[1]
        else:
            delay_domain = group[0]
            delay = '10'
        
        if not delay_domain in first.keys():
            first[delay_domain] = eval(delay)
            mea[delay_domain] = 0
            var[delay_domain] = 0
            num[delay_domain] = 0
            delays[delay_domain] = []
        else:
            #print(ip,delay)
            delay_num = eval(delay)
            if delay_num < 10:
                delays[delay_domain].append(delay_num)
    
    if len(first.keys())<1:
        continue
    w.write(f'{ip}')
    for delay_domain in first.keys():
        if len(delays[delay_domain]) > 1:
            mea[delay_domain] = mean(delays[delay_domain])
            var[delay_domain] = stdev(delays[delay_domain])
        elif len(delays[delay_domain]) > 0:
            mea[delay_domain] = delays[delay_domain][0]
            var[delay_domain] = 0
        

        if not delay_domain in existing:
            existing.append(delay_domain)
            w.write(f',0') #new_trigger
            #w.write(f'{first[delay_domain]}:{mea[delay_domain]}:{var[delay_domain]}')
        elif first[delay_domain] > mea[delay_domain] + 3 * var[delay_domain]:
            w.write(f',1') #type1
            #w.write(f'{first[delay_domain]}:{mea[delay_domain]}:{var[delay_domain]}')
        else:
            w.write(f',2') #type2
            #w.write(f'{first[delay_domain]}:{mea[delay_domain]}:{var[delay_domain]}')
    w.write(f'\n')

    

    
