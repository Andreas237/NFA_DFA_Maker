"""
@package fa_logger
Logging function for PJ01, see PJ01.pdf for project spec. Order of opertaions:
    Set the file names
    Remove any previou files if they exists
    Create the .log file
    Create the .txt file
"""

# \author:   Andreas Slovacek
# \description:
#

import os
import sys  # determine platform for directory operations




class FA_Logger:
    """FA_Logger
        Meet the requirements defined in the project spec for "Log file - basename.log" and "Output file - basename.txt"
        Logs the following:
            * "Valid: " and the FA classification
            * "Alphabet: " and every character read in the alphabet.  REMOVE "`" from alphabet
            * "Accepted strings: " "a / m" where a = count(accepted strings) m = count(input strings)
            * 0/0 for INVALID FAs
    """


    ## Initialize the logger fields
    # @param self pointer to self
    def __init__(self):
        ## basename as given in PJ01.pdf
        self.basename = ''
        ## output filename, created using basename + .log
        self.logfile = ''
        ## output filename, created using basename + .txt
        self.txt = ''
    # end def __init__(self)







    ## Create .log file with required fields. Get the values from the FA. Logic
    ## applied to VALID.
    # @param FA a finite automaton
    # @param self pointer to self
    def create_log_file(self,FA):

        try:
            # On linux systems need to mknod before writing to file
            if( sys.platform == 'linux' ):
                os.mknod(self.logfile,mode=666)

            f = open(self.logfile, 'w')
            valid = FA.get_valid()
            f.write( 'Valid: ' + valid + '\n')

            f.write( 'States: ' + str(len(FA.get_states())) + '\n')

            tmp = ''
            for i in FA.get_alphabet():
                tmp = tmp + i
            f.write( 'Alphabet: ' + tmp + '\n' )
            # If invalid log 0/0
            if(valid == 'INVALID'):
                f.write('Accepted Strings: 0 / 0\n')
            else:
                f.write('Accepted Strings: ' + str(len(FA.get_accepted_strings())) + '/'+ str(FA.get_strings_processed()) + '\n')

        except PermissionError:
            print("Couldn't open %(f)s for logging" % {'f':self.logfile} )

        except FileNotFoundError:
            print("%(f)s doesn't exist for logging!" % {'f':self.logfile} )
        else:
            f.close()
    # end def create_log_file(self,FA)







    ## Print accepted strings to a text file.  Create the text file as needed.
    # @param FA a finite automaton
    # @param self pointer to self
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







    ##  Takes an FA and creates a file with the specified format
    # @param self pointer to self
    def log_FA(self,FA):
        self.set_filenames(FA.from_file)
        self.remove_previous_files()
        self.create_log_file(FA)
        self.create_txt_file(FA)
    # end def log_FA(self,FA)






    ##  If there is an existing log file or text file, delete it. Fail silently
    # @param self pointer to self
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







    ## Set the name of the file to be created, make sure the results/ exists,
    ## set the names of the .log and .txt files
    # @param self pointer to self
    def set_filenames(self,filename):
        index = filename.find('m')
        self.basename = filename[index:].replace('.fa','')
        if( not os.path.exists("../results/")):
            os.makedirs("../results/")
        self.basename = "../results/" + self.basename
        self.logfile = self.basename + '.log'
        self.txt = self.basename + '.txt'
    # end # \fn def set_filenames(self,filename)

# end  class FA_Logger:
