# \author:   Andreas Slovacek
# \description: Main function for PJ01, see PJ01.pdf for project spec.
#               creates the FAs with self.build_fas()
#               processes strings with


# Lessons learned:
# - Opening files using "with open(...)" automatically closes the file at the
#   end of the statement
# - list(f) on an open file returns a list with each line
# - globs, see list_definition_files, allow you to get all the files in a dir
#   using a regex

import glob
import os
from finite_automaton import FA
from progress_bar import loadingBar





# class FA_Master
# \purpose  fa_master handles directory operations such as finding the definition files,
#           passing definition filenames to an FA, keeping track of FAs, passing FAs strings
#           to process
# \description Build all the FAs
#   Pass the FAs strings
#   Ask the FAs to log themselves
#   Print exit message
#   Have test functionality to handle a portion of the data
#   TODO: feed all the FA definitions into fa_reader
#   TODO: feed input text to each FA
class FA_Master:

    file_prefix     = 'PJ01_runfiles/m'                 # prefix of FA definition files
    file_suffix     = '.fa'                             # suffix of FA definition files
    test_str_file   = 'PJ01_runfiles/input_test.txt'         # file containing test strings





    # \fn def __init__(self)
    # \purpose no need to set init behavior...
    def __init__(self):
        self.files                  = []                # Files read into FAs
        self.fa_list                = []                # {filename:FA} pairs
        self.file_prefix            = 'm'               # prefix of FA definition files
        self.file_suffix            = '.fa'             # suffix of FA definition files
        self.file_dir               = 'PJ01_runfiles/'  # subdirectory of FA definition files
        self.in_strings             = []                # Strings to pass to FAs

    #end def __init__(self)







    # \fn def build_fas(self)
    # \purpose build the dict of FAs and their associated file
    def build_fas(self):
        definition_files = self.list_definition_files()

        for file in definition_files:
            temp_fa = FA(file)
            self.fa_list.append(temp_fa)

        print("FA_MASTER.build_fas():    FAs read from defintion file.\nContinuing process.\n")
    # end def build_fas(self)







    # \fn def get_input_strings(self,input_file)
    # \brief gets all input file strings and stores them in self.in_strings
    # \return 1 if file successfully read into in_strings, 0 otherwise
    def get_input_strings(self,input_file):
        try:
            with open(input_file,'r') as f:
                self.in_strings = list(f)

        except PermissionError as e:
            print("ERROR: Couldn't open %(f)s" % {'f':in_file} )
            return 0

        except FileNotFoundError as e:
            print("ERROR: %(f)s doesn't exist!" % {'f':in_file} )
            return 0
        else:
            return 1
    # end def get_input_strings(self,input_file)







    # \fn def list_definition_files(self)
    # \purpose return a list of all FA definition files in PJ01_runfiles/
    def list_definition_files(self):
        files = []
        # mathch .fa files in PJ01_runfiles/
        for file in glob.glob(self.file_dir+'*.fa'):
            files.append(file)
        return files
    # end def list_definition_files(self)







    # \fn def print_built_fas(self)
    # \brief list definition file for each FA, print_self function
    def print_built_fas(self):
        for fa in self.fa_list:
            fa.print_self()
    # end def print_built_fas(self)







    # \fn def run(self):
    # \brief builds the FAs, get the input strings, try all strings in all FAs
    def run(self):

        self.build_fas()

        successful_fas = []
        failed_fas = []

        # Get the input strings from file
        if self.get_input_strings(self.test_str_file) != 1:
            raise NameError('ERROR:  fa_master.get_input_strings() failed to open input text')




        total = len(self.fa_list)*len(self.in_strings)
        count = 0
        for fai in range(len(self.fa_list)):
            for ts in range(len(self.in_strings)):
                count += 1
                loadingBar(count,total,1)
                self.fa_list[fai].process_string(self.in_strings[ts])
            self.fa_list[fai].finalize_fa()



    # end def run(self)






##################################################################################
#-----------------      TEST RUN
##################################################################################


x = FA_Master()
#y.process_def("PJ01_runfiles/made_up.fa")
#y.process_string('1a1`0 1 b a')
#y.finalize_fa()

#x.list_definition_files()
x.run()
