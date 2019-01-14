#!/usr/bin/python3
# The file recorded on-site (in train) is without commas.
# Also, constants for single journey like date, day of week and
# AM or PM are not recorded on every line to save time, but they
# are written as a before the corresponding journey begins.
# This program reads those comments, appends the information on
# every line, and writes a separate .csv file

from os import chdir as cd

cd('/media/anand/Chiba/Users/Anand/Documents/home/python/self/TokyoMetro/textori')


filnam = 'TokyoMetro_20180914E.txt'
f0 = open(filnam, 'r')


s0 = f0.readlines()
ni = len(s0)
f0.close()

outfil = filnam[:filnam.index('.')] + '_modify.csv'
f1 = open(outfil, 'w')


for i in range(ni):
    s1 = (s0[i])[:-1]
#    print(s1)

    if (s1[0] == '#'):
        if (s1[1:5] != '2018'):
            continue
        else:
            s1 = s1[1:]
            s2 = s1.split(',')
            try:
                yymmdd = s2[0]
                DoW = s2[1]
                ampm = s2[2]
            except NameError:
                break
    else:
        nj = len(s1)
        s3 = yymmdd + ',' + DoW + ',' + ampm + ','
        #
        for j in range(nj):
            if ((s1[j] != ',') and (s1[j] != ' ')):
                s3 += s1[j] + ','
        s3 = s3[:-1] + '\n'
        
        f1.write(s3)

f1.close()