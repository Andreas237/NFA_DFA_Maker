


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

# end  class FA_Logger:
