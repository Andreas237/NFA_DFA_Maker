# class FA_Logger:
# Purpose:  meet the logging requirements in defined in the project spec for
#           "Log file - basename.log"
# Logs the following:
#   "Valid: " and the FA classification
#   "States: " number of states in the FA, plus state 255
#   "Alphabet: " and every character read in the alphabet.  REMOVE "`" from alphabet
#   "Accepted strings: " "a / m" where a = count(accepted strings) m = count(input strings)
#        NOTE: 0/0 for INVALID FAs


class FA_Logger:

    def __init__(self):
        print("logging...")

    # def log_FA
    # Purpose: takes an FA and creates a file with the specified format
    def log_FA(self,FA):
        #TODO: stop doing this.  DRAW IT OUT!
        #NOTE: {}accept states accepts empty string
        basename = FA.from_file.replace(".fa",'')
        f = open( basename + '.log', 'w')
        f.write('Valid: ' + FA.classification+'\n')






    # def remove_previous_log(self)
    # Purpose: If there is an existing logfile, delete it
    def remove_previous_log(self):

    # end def remove_previous_log(self)

# end  class FA_Logger:
