##################################################################################
#-----------------      CLASS: FA_Logger
##################################################################################
# Purpose:  meet the requirements defined in the project spec for
#           "Log file - basename.log"
#           "Output file - basename.txt"
# Logs the following:
#   "Valid: " and the FA classification
#   "States: " number of states in the FA, plus state 255
#   "Alphabet: " and every character read in the alphabet.  REMOVE "`" from alphabet
#   "Accepted strings: " "a / m" where a = count(accepted strings) m = count(input strings)
#        NOTE: 0/0 for INVALID FAs


class FA_Logger:

    def __init__(self):
        print("logging...")
        self.basename = ''
        self.logfile = ''
        self.txt = ''

    # def log_FA
    # Purpose: takes an FA and creates a file with the specified format
    def log_FA(self,FA):
        self.set_filenames(FA.from_file)
        print("FA NAME: " = self.basename)
        print("")







    # def remove_previous_log(self)
    # Purpose: If there is an existing logfile, delete it
    def remove_previous_files(self):
        # Remove last txt and log file
        try:
            os.remove(self.basename+'.txt')
            os.remove(self.basename+'.log')
        except Exception FileNotFoundError:
            print("didn't find %(log)s or %(txt)s." % {} )
    # end def remove_previous_log(self)







    # def set_filenames(self,filename)
    # set the names of the files we will use
    def set_filenames(self,filename):
        self.basename = filename.replace('.fa')
        self.logfile = self.basename + '.log'
        self.txt = self.basename + '.txt'
    # end # def set_filenames(self,filename)

# end  class FA_Logger:
