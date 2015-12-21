import pylab as plt
import numpy as np
import os,sys

'''
usage: python plotFigs.py [ID]
ID - string included in each of the target data outputs

Requires matplotlib: apt-get install python-matplotlib
'''
try: target=sys.argv[1]
except: target='example'
clock=[];ctemp=[]
fns=os.listdir('.')
fns.sort()
for fn in fns:
    if fn.count(target):
        dat=[]
        f=open(fn,'r')
        for line in f.readlines()[1:]:
            words=line.rsplit(' ')
            dat.append(map(float,filter(len,words)))
        dat=np.array(dat)
        f.close()
        clock.append(dat[:,1])
        ctemp.append(dat[:,8])
        plt.subplot(3,1,1)
        plt.ylabel('clock [ghz]')
        plt.plot(dat[:,1],'k',alpha=0.3)
        plt.ylim([3.0,4.0])
        plt.subplot(3,1,2)
        plt.ylabel('temp [deg C]')
        plt.plot(dat[:,9],'k',alpha=0.3)
        #plt.subplot(4,1,4)
        #plt.plot(dat[:,9],dat[:,1],'k.',alpha=0.3)
        #plt.ylim([3,4])
        plt.subplot(3,1,3)
        plt.plot(dat[:,15],'k',alpha=0.3)
        plt.ylim([35,60])
        plt.ylabel('power draw [W]')
        plt.xlabel('time [sec]')
plt.show()
