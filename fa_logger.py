import os
import sys  # determine platform for directory operations
#   "States: " number of states in the FA, plus state 255
##################################################################################
# CLASS: FA_Logger
##################################################################################
# \purpose Meet the requirements defined in the project spec for
#           "Log file - basename.log"
#           "Output file - basename.txt"
# \description Logs the following:
#   "Valid: " and the FA classification
#   "Alphabet: " and every character read in the alphabet.  REMOVE "`" from alphabet
#   "Accepted strings: " "a / m" where a = count(accepted strings) m = count(input strings)
#        NOTE: 0/0 for INVALID FAs


class FA_Logger:

    # \fn def __init__(self)
    # \purpose
    def __init__(self):
        self.basename = ''      # basename as given in PJ01.pdf
        self.logfile = ''       # output filename, created using basename + .log
        self.txt = ''           # output filename, created using basename + .txt
    # end def __init__(self)







    # \fn def create_log_file(self,FA)
    # \purpose create .log file with required fields
    def create_log_file(self,FA):
        try:
            # On linux systems need to mknod before writing to file
            if( sys.platform == 'linux' ):
                os.mknod(self.logfile,mode=666)

            f = open(self.logfile, 'w')

            f.write( 'Valid: ' + FA.get_valid() + '\n')

            f.write( 'States: ' + str(len(FA.get_states())) + '\n')

            tmp = ''
            for i in FA.get_alphabet():
                tmp = tmp + i
            f.write( 'Alphabet: ' + tmp + '\n' )

            f.write('Accepted Strings: ' + str(len(FA.get_accepted_strings())) + '/'+ str(FA.get_strings_processed()) + '\n')
        except PermissionError:
            print("Couldn't open %(f)s for logging" % {'f':self.logfile} )

        except FileNotFoundError:
            print("%(f)s doesn't exist for logging!" % {'f':self.logfile} )
        else:
            f.close()
    # end def create_log_file(self,FA)







    # \fn def create_txt_file(self,FA):
    # print accepted strings to the text file
    def create_txt_file(self,FA):
        try:

            # On linux systems need to mknod before writing to file
            if( sys.platform == 'linux' ):
                os.mknod(self.txt,mode=666)

            f = open(self.txt, 'w')

            for s in FA.get_accepted_strings():
                f.write(s + '\n')
        except PermissionError:
            print("Couldn't open %(f)s for text" % {'f':self.txt} )

        except FileNotFoundError:
            print("%(f)s doesn't exist for text!" % {'f':self.txt} )
        else:
            f.close()
    # end def create_txt_file(self,FA)







    # \fn def log_FA(self,FA)
    # \purpose takes an FA and creates a file with the specified format
    def log_FA(self,FA):
        self.set_filenames(FA.from_file)
        self.remove_previous_files()
        self.create_log_file(FA)
        self.create_txt_file(FA)
    # end def log_FA(self,FA)






    # \fn def remove_previous_log(self)
    # \purpose If there is an existing logfile, delete it
    def remove_previous_files(self):
        # Remove last txt and log file
        try:
            os.remove(self.basename+'.txt')
        except Exception as e:
            pass    # if it didn't exist no impact
        try:
            os.remove(self.basename+'.log')
        except Exception as e:
            pass    # if it didn't exist no impact

    # end def remove_previous_log(self)







    # \fn def set_filenames(self,filename)
    # set the names of the files we will use
    def set_filenames(self,filename):
        self.basename = filename.replace('.fa','')
        self.basename = self.basename[ self.basename.find("/") + 1 : ]
        self.basename = "Output_files/" + self.basename
        self.logfile = self.basename + '.log'
        self.txt = self.basename + '.txt'
    # end # \fn def set_filenames(self,filename)

# end  class FA_Logger:
