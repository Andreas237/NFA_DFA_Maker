
import os                       # Open files in a directory
from FiniteAutomaton import FA  # Import the structure of the FA

file_prefix = 'made_up'
file_suffix = '.fa'




class fa_reader:
    file_prefix = 'made_up'
    file_suffix = '.fa'
    fas         = []

    def __init__(self):
        self.run()

    def do_file(self, filename):

        try:
            with open(filename,'r') as f:
                fa = FA(filename)
                fa.set_accept_states((f.readline()).replace('{','').replace('\n','').replace('}','').split(','))

                #TODO: check that the contents of the transition table are validself
                #TODO: finish "plant of attack" in sketchpad
                for line in f:
                    line = line.replace('\n','')    # remove \n from the line
                    line = tuple(line.split(','))   # create a tuple from the line
                    fa.set_transition(line)         # add the transition to the table


        except PermissionError:
            print("Couldn't open %(f)s" % {'f':currentFile} )

        except FileNotFoundError:
            print("%(f)s doesn't exist!" % {'f':currentFile} )
        else:
            self.fas.append(fa)
            f.close()


    def run(self):
        self.do_file('PJ01_runfiles/'+file_prefix+file_suffix)
        print("Length in fas: %(l)s" %{'l':(len(self.fas))} )

        self.fas[0].typeCheck_FA()
        self.fas[0].print_self()


x = fa_reader()
x.run()
print("Done")
