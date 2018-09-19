import os
from enum import Enum
from fa_reader import fa_reader





# class FA_Master
# Purpose
#   TODO: feed all the FA definitions into fa_reader
#   TODO: keep track of all FAs
#   TODO: feed input text to each FA
class FA_Master:

    class Bool:
        FALSE = 0
        TRUE = 1





    mode                    = "TEST"                # TEST means limit to test files, and limited range
    test_files              = ['made_up.fa']        # test FA definition files
    f_range                 = 5                     # number of real definition files to read








    # def __init__(self)
    # Purpose: no need to set init behavior...
    def __init__(self):
        print("It shall be done")
        print(self.Bool.FALSE)
        print(self.Bool.TRUE)
    #end def __init__(self)








    # def read_fa_def_files
    #
    def read_fa_def_files(self):
        # If test mode:
        #   Create a fa_reader
        #   Read files in: test_files, and other .fa files up to self.f_range
        if( self.mode == "TEST"):
            fas = fa_reader()
            #TODO: pass the FA a filename.  Need to write that function... fas.
            #   NOTE: once passed a filename fa_reader should create an FA and add
            #           to the list.
            #TODO: pass fa_reader() lines of input.  It should process each input line separately


    # end def read_fa_def_files





x = fa_reader()
x.reset_fas()
y = FA_Master()

print("Done")
