import os
from finite_automaton import FA





# class FA_Master
# Purpose:  fa_master handles directory operations such as finding the definition files,
#           passing definition filenames to an FA, keeping track of FAs, passing FAs strings
#           to process
# Outline:
#   Build all the FAs.  Store them in a dict[filename, FA]
#   Pass the FAs strings
#   Ask the FAs to log themselves
#   Print exit message
#   Have test functionality to handle a portion of the data
#   TODO: feed all the FA definitions into fa_reader
#   TODO: feed input text to each FA
class FA_Master:
    file_prefix = 'PJ01_runfiles/m'                 # prefix of FA definition files
    file_suffix = '.fa'                             # suffix of FA definition files





    # def __init__(self)
    # Purpose: no need to set init behavior...
    def __init__(self):
        self.test_file               = ['made_up.fa']        # test FA definition files
        self.files                   = []                    # Files read into FAs
        self.fa_list                 = dict()                # {filename:FA} pairs
        self.file_prefix = 'm'                               # prefix of FA definition files
        self.file_suffix = '.fa'                             # suffix of FA definition files
        self.file_dir    = 'PJ01_runfiles/'                  # subdirectory of FA definition files
        self.fake_file   = "PJ01_runfiles/made_up.fa"        # Made up file for testing FA definition

    #end def __init__(self)







    # def build_fas(self)
    # Purpose:
    #
    def build_fas(self):
