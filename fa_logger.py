import os

#   "States: " number of states in the FA, plus state 255
##################################################################################
#-----------------      CLASS: FA_Logger
##################################################################################
# Purpose:  meet the requirements defined in the project spec for
#           "Log file - basename.log"
#           "Output file - basename.txt"
# Logs the following:
#   "Valid: " and the FA classification
#   "Alphabet: " and every character read in the alphabet.  REMOVE "`" from alphabet
#   "Accepted strings: " "a / m" where a = count(accepted strings) m = count(input strings)
#        NOTE: 0/0 for INVALID FAs


class FA_Logger:

    def __init__(self):
        self.basename = ''
        self.logfile = ''
        self.txt = ''








    # def create_log_file(self,FA)
    # Purpose: create .log file with required fields
    def create_log_file(self,FA):
        try:

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
            print("Couldn't open %(f)s" % {'f':self.logfile} )

        except FileNotFoundError:
            print("%(f)s doesn't exist!" % {'f':self.logfile} )
        else:
            f.close()
    # end def create_log_file(self,FA)







    # def create_txt_file(self,FA):
    # print accepted strings to the text file
    def create_txt_file(self,FA):
        try:
            os.mknod(self.txt,mode=666)

            f = open(self.txt, 'w')

            for s in FA.get_accepted_strings():
                f.write(s + '\n')
        except PermissionError:
            print("Couldn't open %(f)s" % {'f':self.txt} )

        except FileNotFoundError:
            print("%(f)s doesn't exist!" % {'f':self.txt} )
        else:
            f.close()
    # end def create_txt_file(self,FA)







    # def log_FA(self,FA)
    # Purpose: takes an FA and creates a file with the specified format
    def log_FA(self,FA):
        self.set_filenames(FA.from_file)
        self.remove_previous_files()
        self.create_log_file(FA)
        self.create_txt_file(FA)
        print("Finished FA_Logger.log_FA")
    # end def log_FA(self,FA)






    # def remove_previous_log(self)
    # Purpose: If there is an existing logfile, delete it
    def remove_previous_files(self):
        # Remove last txt and log file
        try:
            os.remove(self.basename+'.txt')
        except Exception as e:
            print("couldn't remove " + self.basename+'.txt')
            print(e)
        try:
            os.remove(self.basename+'.log')
        except Exception as e:
            print("couldn't remove " + self.basename+'.log')
            print(e)

    # end def remove_previous_log(self)







    # def set_filenames(self,filename)
    # set the names of the files we will use
    def set_filenames(self,filename):
        self.basename = filename.replace('.fa','')
        self.basename = self.basename[ self.basename.find("/") + 1 : ]
        self.basename = "Output_files/" + self.basename
        self.logfile = self.basename + '.log'
        self.txt = self.basename + '.txt'
    # end # def set_filenames(self,filename)

# end  class FA_Logger:
