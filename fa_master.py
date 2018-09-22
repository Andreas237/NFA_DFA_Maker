import glob
import os
from finite_automaton import FA





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

    file_prefix = 'PJ01_runfiles/m'                 # prefix of FA definition files
    file_suffix = '.fa'                             # suffix of FA definition files





    # \fn def __init__(self)
    # \purpose no need to set init behavior...
    def __init__(self):
        self.test_file               = ['made_up.fa']        # test FA definition files
        self.files                   = []                    # Files read into FAs
        self.fa_list                 = []                # {filename:FA} pairs
        self.file_prefix = 'm'                               # prefix of FA definition files
        self.file_suffix = '.fa'                             # suffix of FA definition files
        self.file_dir    = 'PJ01_runfiles/'                  # subdirectory of FA definition files
        self.fake_file   = "PJ01_runfiles/made_up.fa"        # Made up file for testing FA definition

    #end def __init__(self)







    # \fn def build_fas(self)
    # \purpose build the dict of FAs and their associated file
    def build_fas(self):
        definition_files = self.list_definition_files()

        for file in definition_files[22:26]:
            temp_fa = FA()
            temp_fa.process_def(file)
            self.fa_list.append(temp_fa)

        self.print_built_fas()
    # end def build_fas(self)







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







    # \fn def process_input_file(self)
    # \brief find the input file in the directory and process it with all FAs
    def process_input_file(self, fa_in:FA, f_pointer):
        for line in f_pointer:
            line = f_pointer.readline()
            fa_in.process_string( line )
            print("FA from %(name)s processed line %(line)s" %{'line':line, 'name':fa_in.from_file})
    # end def process_input_file(self)







    # \fn def run(self):
    # \brief builds the FAs, opens the input text, process FA, close file
    def run(self):

        self.build_fas()


        in_file = 'PJ01_runfiles/input.txt'
        try:
            f_pointer = open(in_file, 'r')

        except PermissionError as e:
            print("Couldn't open %(f)s" % {'f':in_file} )

        except FileNotFoundError as e:
            print("%(f)s doesn't exist!" % {'f':in_file} )
        # Process FAs
        else:
            for fa in self.fa_list:
                # Make sure the file pointer is at the beginning
                print(type(f_pointer))
                f_pointer.seek(0,0)
                self.process_input_file(fa,f_pointer)
                fa.finalize_fa()
            f_pointer.close()
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
