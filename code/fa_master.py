"""
@package fa_master

Author: Andreas Slovacek

Main function for PJ01, see PJ01.pdf for project spec. Order of operations:
    Creates the FAs with self.build_fas()
    Processes strings with

Lessons learned:
    - Opening files using "with open(...)" automatically closes the file at the
        end of the statement
    - list(f) on an open file returns a list with each line
    - globs, see list_definition_files, allow you to get all the files in a dir
using a regex
"""



import glob
import os
import time
from finite_automaton import FA
from progress_bar import loadingBar





class FA_Master:
    """
    fa_master handles directory operations such as finding the definition files,
    passing definition filenames to an FA, keeping track of FAs, passing FAs strings
    to process.  Order of operations:
    Build all the FAs
    Pass the FAs strings
    Ask the FAs to log themselves
    Print exit message
    Have test functionality to handle a portion of the data

    Running this file with >>python3 fa_master.py will execute the script at the bottom of the file.
    """
    ## prefix of FA definition files
    file_prefix     = '../PJ01_runfiles/m'
    ## suffix of FA definition files
    file_suffix     = '.fa'
    ## file containing test strings
    test_str_file   = '../PJ01_runfiles/input.txt'





    ##  Set instance vars
    # @param self pointer to self
    def __init__(self):
        ## Files read into FAs
        self.files          = []
        ## List of FAs from .fa file
        self.fa_list        = []
        ## prefix of FA definition files
        self.file_prefix    = 'm'
        ## suffix of FA definition files
        self.file_suffix    = '.fa'
        ## subdirectory of FA definition files
        self.file_dir       = '../PJ01_runfiles/'
        ## Strings to pass to FAs
        self.in_strings     = []
    #end def __init__(self)







    ## Build the list of FAs and their associated file
    # @param self pointer to self
    def build_fas(self):
        definition_files = self.list_definition_files()
        print("Building FAs")
        for file in definition_files:
            temp_fa = FA(file)
            self.fa_list.append(temp_fa)

        print("FA_MASTER.build_fas():    Read %(ct)d FAs from defintion files.\nContinuing process." %{'ct':len(self.fa_list)})
    # end def build_fas(self)







    ## Gets all input file strings and stores them in self.in_strings
    # @param self pointer to self
    # @param[in] self.in_strings list[] of strings from input.txt
    # @return boolean 1 if file successfully read into self.in_strings, 0 otherwise
    def get_input_strings(self,input_file):
        try:
            with open(input_file,'r') as f:
                self.in_strings = list(f)

        except PermissionError as e:
            print("ERROR: Couldn't open " + in_file )
            return 0

        except FileNotFoundError as e:
            print("ERROR: " + in_file + " doesn't exist!")
            return 0
        else:
            return 1
    # end def get_input_strings(self,input_file)







    ##  return a list of all FA definition files in PJ01_runfiles/
    # @param self pointer to self
    # @param[in] self.file_dir directory where the definition files are stored
    def list_definition_files(self):
        files = []
        # mathch .fa files in PJ01_runfiles/
        for file in glob.glob(self.file_dir+'*.fa'):
            files.append(file)
        return files
    # end def list_definition_files(self)







    ## List definition file for each FA, print_self function
    # @param self pointer to self
    # @param[in] self.fa_list list of the FAs built from definition files.
    def print_built_fas(self):
        for fa in self.fa_list:
            fa.print_self()
    # end def print_built_fas(self)







    ##  Builds the FAs, get the input strings, try all strings in all FAs.
    # Show updates in the CLI to confirm it hasn't crashed.
    # @param self pointer to self
    def run(self):
        # START tracks the beginning of the process
        start = time.time()

        #
        self.build_fas()


        # Get the input strings from file
        print("Getting input strings")
        if self.get_input_strings(self.test_str_file) != 1:
            raise NameError('ERROR:  fa_master.get_input_strings() failed to open input text')



        # TOTAL  and COUNT used for the progress bar
        total = len(self.fa_list)*len(self.in_strings)
        count = 0


        # For each FA in self.fa_list pass it all the strings extracted from
        # input.txt
        print("Running input strings through FAs:")
        for fai in range(len(self.fa_list)):
            for ts in range(len(self.in_strings)):
                count += 1                  # used for loadingBar
                loadingBar(count,total,1)   # so you know the program hasn't frozen
                self.fa_list[fai].process_string(self.in_strings[ts])
            # Finalize executes logging
            self.fa_list[fai].finalize_fa()
        print()
        # Print the total execution time to the CLI
        print("Execution time= {0:.5f}".format(time.time() - start))
    # end def run(self)







# TEST RUN
x = FA_Master()
x.run()
