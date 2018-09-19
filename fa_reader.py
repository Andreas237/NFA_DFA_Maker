
import os                       # Open files in a directory
import re                       # regex first line for validation
from finite_automaton import FA  # Import the structure of the FA










# class fa_reader
# Purpose:
# - Read an FA definition file
# -- check the accept states for validity
# -- pass each line to the FiniteAutomaton (FA) class to create accept states and transition functions
# - store a list of FAs
# - Read all FA definition files
# - Pass strings to each FA to check accept/reject
class fa_reader:
    file_prefix = 'made_up'
    file_suffix = '.fa'
    fas         = []









    # Run logic when fa_reader is created
    def __init__(self):
        self.run()









    # def check_accept_states(line)
    # check that the given line has curly braces and is formatted correctly
    # return 0 if valid first line
    # return 1 if invalid
    # Call internally
    def check_accept_states(self,line):
        exp = re.compile('\{[\d,]*\}',re.ASCII)
        if ('255' in line):
            return 1
        elif exp.match(line):
            return 0
        else:
            return 1









    # def do_file(self, filename)
    # Purpose:
    #   Open the file we're given
    #   Check that the file has valid accept states, cease processing if not
    #   Read in the transitions
    #   store the fa in fas
    #   close the file
    # Call internally
    def do_file(self, filename):

        try:
            with open(filename,'r') as f:

                fa = FA(filename)
                line = f.readline()

                # If the first line is invalid cease processing
                if self.check_accept_states(line) == 1:
                    return 1
                fa.set_accept_states((line).replace('{','').replace('\n','').replace('}','').split(','))

                # Read in the transitions
                for line in f:
                    line = line.replace('\n','')    # remove \n from the line
                    line = tuple(line.split(','))   # create a tuple from the line
                    fa.set_transition(line)         # add the transition to the table
                # end for line in f

                # Internally process the fa, validate, and set vars
                fa.process()

        # If the file can't be opened notify
        except PermissionError:
            print("Couldn't open %(f)s" % {'f':currentFile} )

        except FileNotFoundError:
            print("%(f)s doesn't exist!" % {'f':currentFile} )

        # If no errors add the FA to the list and close the file
        else:
            self.fas.append(fa)
            f.close()
    # end def do_file(self, filename)








    # def reset_fas
    # Purpose: reset each FA to accept a new input string
    #       Call externally
    def reset_fas(self):
        for fa in self.fas:
            fa.reset_self()
        # end for fa in self.fas
    # end def reset_fas(self)








    # def run(self)
    # Purpose:
    #   - run operations on the file we're intaking
    #   - create a list of FAs from the files
    #   - TODO: iterate through all files named 'm[0-9]*.fa'
    #   - TODO: feed the FAs strings to check for success
    # Call internally
    def run(self):
        if self.do_file('PJ01_runfiles/'+self.file_prefix+self.file_suffix):
            return 1
        if self.fas[0].typeCheck_FA():
            return 1
        self.fas[0].print_self()
    # end def run(self)
