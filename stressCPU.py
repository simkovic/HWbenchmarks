from multiprocessing import Pool,cpu_count
import sys, commands,datetime,time,subprocess

'''
Usage: sudo python stressCPU.py [NTHREADS] [NREPS] [DUR]
uses turbostat for monitoring - you need to install turbostat
sudo is required by turbostat

NTHREADS - number of threads/jobs to run in parallel, default: max thread count
NREPS - number of replications/blocks
DUR - length of a stress block in minutes
'''
OUTDIR='~/bench/' # write the turbostat output here
def work(wid): 
    try:
        while True: res=1+1 # forget primes, keep it simple
    except KeyboardInterupt: sys.exit(1)
if __name__=='__main__':
    try: nthreads=int(sys.argv[1])
    except: nthreads=cpu_count()
    try: nreps=int(sys.argv[2])
    except: nreps=10
    try: dur=int(sys.argv[3])
    except: dur=3
    dt=datetime.datetime.now().isoformat()[:16]
    for i in range(nreps):
        print i
        commands.getstatusoutput('rm %stemp.res'%OUTDIR)
        commands.getstatusoutput('modprobe msr') #required by turbostat
        cmd='turbostat -S -i 1 >> %stemp.res'%OUTDIR
        mon=subprocess.Popen([cmd],shell=True,stdin=None, 
            stdout=None, stderr=None, close_fds=True)
        time.sleep(10)
        pool=Pool(processes=nthreads)
        res=pool.map_async(work,range(nthreads))
        time.sleep(dur*60)
        pool.terminate()
        time.sleep(10)
        mon.kill()
        a=commands.getstatusoutput('cp %stemp.res '%OUTDIR+
            '%spy%dr%02dd%s.csv'%(OUTDIR,nthreads,i,dt))
        commands.getstatusoutput('rm %stemp.res'%OUTDIR)
        time.sleep(40)
