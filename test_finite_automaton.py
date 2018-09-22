from finite_automaton import FA
# \description Test functionality of the FA class



##################################################################################
#-----------------      TEST RUN
##################################################################################
instrs = []
with open('PJ01_runfiles/input_test.txt','r') as f:
    instrs = list(f)
    #instrs.append('a\n')

defs = ["PJ01_runfiles/m02.fa","PJ01_runfiles/m01.fa","PJ01_runfiles/m00.fa","PJ01_runfiles/made_up.fa"]
#defs = ["PJ01_runfiles/m00.fa"]

fas = []

for d in defs:
    fas.append( FA(d) )

#for i in range(len(fas)):
#    fas[i].print_self()

for f in fas:
    for s in instrs:
        next
        f.process_string(s)
    f.finalize_fa()
