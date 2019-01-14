#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import chdir as cd


cd('/media/anand/Chiba/Users/Anand/Documents/home/python/self/TokyoMetro/textori')


filnam = 'TokyoMetro_20180914E_modify.csv'
a0 = pd.read_csv(filnam, header=None)

Didx = ['date', 'DoW', 'ampm', 'sex', 'age', 'TDR', 'book', 'mobi', 
        'scrn', 'ears', 'line']
a0.columns = Didx

DoWR = ['M', 'T', 'W', 'H', 'F', 'A', 'U']
ampmR = ['M', 'E'];  sexR = ['M', 'F']
ageR = [str(i) for i in range(10)]
TDRR = ['T', 'D', 'R']
bookR = mobiR = scrnR = ['Y', 'N']
earsR = ['W', 'L', 'N'];  lineR = ['T', 'C']

condiR = ((~a0['DoW'].isin(DoWR)) | (~a0['ampm'].isin(ampmR)) | 
            (~a0['sex'].isin(sexR)) | (~a0['age'].isin(ageR)) | 
            (~a0['TDR'].isin(TDRR)) | (~a0['book'].isin(bookR)) |
            (~a0['mobi'].isin(mobiR)) | (~a0['scrn'].isin(scrnR)) | 
            (~a0['ears'].isin(earsR)) | (~a0['line'].isin(lineR)))

r0 = a0.loc[condiR].index.values

a1 = a0.drop(r0)


timMorn = a1.loc[a1['ampm'] == 'M']
timEven = a1.loc[a1['ampm'] == 'E']

aX = [timMorn, timEven]


for i in range(2):
    aY = aX[i]

    niM = aY['sex'].loc[aY['sex'] == 'M'].count()
    niF = aY['sex'].loc[aY['sex'] == 'F'].count()

    rxM = aY.loc[aY['sex'] == 'M']
    rxF = aY.loc[aY['sex'] == 'F']
    
    xpos = [i for i in range(3)]
    
    # for men
    M_book_Y = int(rxM['book'].loc[rxM['book'] == 'Y'].count())/niM * 100
    ###M_book_N = int(rxM['book'].loc[rxM['book'] == 'N'].count())/niM * 100
    M_book_N = 100 - M_book_Y
    #
    M_mobi_Y = int(rxM['mobi'].loc[rxM['mobi'] == 'Y'].count())/niM * 100
    M_mobi_N = 100 - M_mobi_Y
    #
    M_ears_Y = int(rxM['ears'].loc[rxM['ears'].isin(['W','L'])].count())/niM * 100
    M_ears_N = 100 - M_ears_Y
    #
    M_Y = (M_book_Y, M_mobi_Y, M_ears_Y)
    M_N = (M_book_N, M_mobi_N, M_ears_N)
    
    
    # for women
    F_book_Y = int(rxF['book'].loc[rxF['book'] == 'Y'].count())/niF * 100
    ###F_book_N = int(rxF['book'].loc[rxF['book'] == 'N'].count())/niF * 100
    F_book_N = 100 - F_book_Y
    #
    F_mobi_Y = int(rxF['mobi'].loc[rxF['mobi'] == 'Y'].count())/niF * 100
    F_mobi_N = 100 - F_mobi_Y
    #
    F_ears_Y = int(rxF['ears'].loc[rxF['ears'].isin(['W','L'])].count())/niF * 100
    F_ears_N = 100 - F_ears_Y
    #
    F_Y = (F_book_Y, F_mobi_Y, F_ears_Y)
    F_N = (F_book_N, F_mobi_N, F_ears_N)
    
    
    fig, ax = plt.subplots()
    
    xidx, bwd = np.arange(3), 0.4
    
    
    rcp1 = ax.bar(xidx-0.2, M_Y, bwd, alpha=0.8, color='b', label='Men')
    #rcp2 = ax.bar(xidx, M_N, bwd, alpha=0.4, color='b', label='Men N')
    rcp3 = ax.bar(xidx+0.2, F_Y, bwd, alpha=0.8, color='r', label='Women')
    #rcp4 = ax.bar(xidx+0.4, F_N, bwd, alpha=0.4, color='r', label='Women N')
    
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(['book', 'mobile', 'headset'])
    ax.legend()
    fig.tight_layout()

    plt.ylabel('percentage')
    plt.ylim(0,72)
    plt.show()


