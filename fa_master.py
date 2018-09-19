import os
from finite_automaton_c import FA





# class FA_Master
# Purpose
#   TODO: feed all the FA definitions into fa_reader
#   TODO: feed input text to each FA
class FA_Master:
    file_prefix = 'm'                               # prefix of FA definition files
    file_suffix = '.fa'                             # suffix of FA definition files
    file_dir    = 'PJ01_runfiles/'                  # subdirectory of FA definition files





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



    
