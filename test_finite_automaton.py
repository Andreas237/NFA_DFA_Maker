from multiprocessing import Pool
import time
import threading
from finite_automaton import FA
# \description Test functionality of the FA class and other necessaries.



##################################################################################
#-----------------      TEST RUN
##################################################################################
instrs = []
with open('PJ01_runfiles/input_test.txt','r') as f:
    #instrs = list(f)
    instrs.append('12a12a12`a1 \n')

#defs = ["PJ01_runfiles/m02.fa","PJ01_runfiles/m01.fa","PJ01_runfiles/m00.fa","PJ01_runfiles/made_up.fa"]
defs = ["PJ01_runfiles/made_up.fa"]

fas = []

for d in defs:
    fas.append( FA(d) )


print("="*80)
start = time.time()
for f in fas:
    for s in instrs:
        t = threading.Thread(target=f.process_string, args=(s,))
        t.start()
    f.finalize_fa()
t.join()
print("Execution time with threading= {0:.5f}".format(time.time() - start))

fas.clear()
for d in defs:
    fas.append( FA(d) )


print("="*80)
start = time.time()
for f in fas:
    for s in instrs:
        f.process_string(s)
print("Execution time with for-loop= {0:.5f}".format(time.time() - start))



fas.clear()
for d in defs:
    fas.append( FA(d) )


print("="*80)
start = time.time()
with Pool(processes=len(fas)) as pool:  # start 4 worker processes
    result = pool.apply_async(f.process_string,[s])

print("Execution time with multiprocessing= {0:.5f}".format(time.time() - start))


#print("="*80)
#start = time.time()
#for i in range(len(fas)):
#    t = threading.Thread(target=fas[i].print_self())
#    t.start()
#t.join()
#print("Execution time with threading= {0:.5f}".format(time.time() - start))
#print("="*80)
#start = time.time()
#for i in range(len(fas)):
#    fas[i].print_self()

#print("Execution time without threading= {0:.5f}".format(time.time() - start))
