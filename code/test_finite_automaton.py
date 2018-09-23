import os
from multiprocessing import Pool
import time
import threading
from finite_automaton import FA
# \description Test functionality of the FA class and other necessaries.



##################################################################################
#-----------------      TEST RUN
##################################################################################
# code

instrs = []
with open('../PJ01_runfiles/input_test.txt','r') as f:
    #instrs = list(f)
    instrs.append('12a12a12`a1 \n')

#defs = ["PJ01_runfiles/m02.fa","PJ01_runfiles/m01.fa","PJ01_runfiles/m00.fa","PJ01_runfiles/made_up.fa"]
defs = ["../PJ01_runfiles/made_up.fa"]

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
