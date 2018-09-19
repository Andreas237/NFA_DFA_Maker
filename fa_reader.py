
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
    file_prefix = 'm'
    file_suffix = '.fa'
    file_dir    = 'PJ01_runfiles/'
    fake_file   = "PJ01_runfiles/made_up.fa"
    fas         = []









    # Run logic when fa_reader is created
    def __init__(self,test:int):
        # self.run() # no longer needed
        print("Send some FA definition files!")
        if(test == 1):
            self.test_run_file(2)
        else:
            #TODO: finish run all and call it here
            print("NEED TO RUN ALL")









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
                    if( len(line) > 1 ):
                        fa.set_transition(line)         # add the transition to the table
                # end for line in f

                # Internally process the fa, validate, and set vars
                fa.process()

        # If the file can't be opened notify
        except PermissionError:
            print("Couldn't open %(f)s" % {'f':filename} )

        except FileNotFoundError:
            print("%(f)s doesn't exist!" % {'f':filename} )

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








    # def run_file(self)
    # Purpose:
    #   - do_file creates an FA and adds it to our list of FAs
    #   - Check the type on the FA we just appended to the list
    # Call internally
    def run_file(self,filename):
        if self.do_file(filename):
            return 1
        if self.fas[ len(self.fas)-1 ].typeCheck_FA():
            return 1
        self.fas[ len(self.fas)-1 ].print_self()

    # end def run_file(self,filename)







    # def test_run_file(self):
    # Purpose: test the run_file(self,filename) function
    # Try the contrived made_up.fa; then several of the given files
    # Output:
    #   TODO: Count of FAs in self.fas = 3
    #   TODO: Print the alphabets accepted by the FA
    def test_run_file(self,count:int):

        if( count <= 1):
            self.run_file(self.fake_file)
        else:
            for i in range(count):
                #build the filename, then run it
                filename = self.file_dir + self.file_prefix
                if( i < 10):
                    filename = filename + str(0) + str(i)
                else:
                    filename = filename + str(i)
                filename = filename + self.file_suffix
                self.run_file(filename)

        print("CREATED %(n)d FAs\n" % { 'n':len(self.fas) })



    # end def test_run_file(self)
