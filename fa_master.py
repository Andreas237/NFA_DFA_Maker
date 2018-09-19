import os
from enum import Enum
from fa_reader import fa_reader





# class FA_Master
# Purpose
#   TODO: feed all the FA definitions into fa_reader
#   TODO: feed input text to each FA
class FA_Master:

    class Bool:
        TEST = 0                                    # Run with limited files, verbose messages
        PROD = 1                                    # Run with all files, limited messages





    mode                    = Bool.TEST             # Default test mode.  Limited files
    test_file              = ['made_up.fa']         # test FA definition files
    f_range                 = 5                     # number of real definition files to read








    # def __init__(self)
    # Purpose: no need to set init behavior...
    def __init__(self):
        print("It shall be done")
        self.mode = Boole.TEST
        self.run()
    #end def __init__(self)








    # def read_fa_def_files
    #
    def read_fa_def_files(self):
        # If test mode:
        #   Create a fa_reader
        #   Read files in: test_file, and other .fa files up to self.f_range
        if( self.mode == "TEST"):
            fas = fa_reader()
            #TODO: pass the FA a filename.  Need to write that function... fas.
            #   NOTE: once passed a filename fa_reader should create an FA and add
            #           to the list.
            #TODO: pass fa_reader() lines of input.  It should process each input line separately


    # end def read_fa_def_files







    # def run(self)
    # Purpose:
    #   Run the class based on the the mode
    #       IF TEST TRUE
    #           Use the test functions in fa_reader
    #       IF TEST FALSE
    #           #TODO: read the files in the class and and process everything
    def run(self):
        fas = fa_reader()
        print("in fa_master.run()")
        if(self.mode == Boole.TEST):
            print("MODE: %(m)s" % {'m':self.mode})
            fas.test_run_file()
        elif(Boole.PROD):
            print("MODE: %(m)s" % {'m':self.mode})
        else:
            print("ERROR: No mode selected.  Set in fa_master.__init()__")


    # end def run(self):







x = fa_reader(1)
# x.reset_fas()
# y = FA_Master()

print("Done")
