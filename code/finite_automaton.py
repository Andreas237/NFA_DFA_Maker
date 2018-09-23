# \author:   Andreas Slovacek
# \description: finite_automaton.py has all the functions to build an FA. The
#               most important functions are:
#               __init__() Constructor takes a definition file.
#               process_string which tests input strings on the FA
#               finalize_fa: which calls the FA_Logger
#               class Delta: is an entry in the tranistion table

# Lessons Learned:
#   - setting parameter types for fns
#   - variables set outside of __init__, e.g. below 'class NAME: var=1' are class variables
#       and thus keep their values from one instance to the next.
#   - __init__ vars are instance variables and change with each instantiation



##################################################################################
#-----------------      IMPORT FILES
#import os                       # Open files in a directory
import re                       # regex first line for validation
from fa_logger import FA_Logger   # logger for FA













##################################################################################
#-----------------      CLASS: DELTA
##################################################################################
# class delta
# Represents a transition function in the transition table
# \description
#   Plain-old-data holder for a transition given by
#   our in file.  Only sets and gets its data
class delta:
    # current_state:
    # symbol: next read symbol
    # next_state:

    # Init the data in Transitions
    def __init__(self,delta):
        self.set_delta(delta)

    # get the transition function
    def elta(self):
        return (self.current_state, self.symbol, self.next_state)



    # Set the members of the
    def set_delta(self, delta):
        self.current_state = transition[0]
        self.symbol     = transition[1]
        self.next_state   = transition[2]


#end class delta













##################################################################################
#CLASS: FA
##################################################################################
# class FA:
# \description
#   Takes a file and sets the: accept state(s), transition table, alphabet
#   Given a string check that we can process the string
#       (char in string vs. alphabet), and then check whether the string ends
#       in an accept state.
class FA:








    # \fn def __init__(self)
    def __init__(self, def_file):
        self.accept_states       = set()     # accept_states read from .fa file
        self.accepted_strings    = []        # Strings that reached an "accept" state
        self.alphabet            = set()     # alphabet of the input language
        self.current_state       = '0'       # state the FA is currently in.  Default start 0
        self.epsilon_trans       = set()     # set of transitions with multiple "to" states
        self.from_file           = ''        # which .fa file defined this FA
        self.states              = set()     # set of states, derived from transition_table
        self.strings_processed   = 0
        self.transition_table    = set()     # transition function tuples from FA file
        self.valid               = ''        # classification of the FA (NFA, DFA, INVALID)
        self.valid_reason        = ''        # why this classification?
        self.process_def(def_file)
    # \fn def __init__(self)









    # \fn def build_fa_from_file(self)
    def build_fa_from_file(self):
        try:
            with open(self.from_file,'r') as f:
                # Create an FA at the next index
                line = f.readline()

                # If the first line is invalid cease processing
                if self.check_accept_states(line) == 1:
                    self.set_classification = 'INVALID'
                    self.valid_reason = 'Bad accept states in file'
                    return None
                self.set_accept_states((line).replace('{','').replace('\n','').replace('}','').split(','))

                # Read in the transitions
                for line in f:
                    line = line.replace('\n','')    # remove \n from the line
                    line = tuple(line.split(','))   # create a tuple from the line
                    if( len(line) > 1 ):
                        self.set_transition(line)         # add the transition to the table
                # end for line in f

                # Internally process the fa, validate, and set vars

        # If the file can't be opened notify
        except PermissionError:
            print("Couldn't open %(f)s" % {'f':filename} )

        except FileNotFoundError:
            print("%(f)s doesn't exist!" % {'f':filename} )

        # If no errors add the FA to the list and close the file
        else:
            f.close()
    # end def build_fa_from_file(self)







    # \fn def check_accept_states(self,line)
    # if the line doesn't match the regular expression of a line return 1
    # else return 0
    def check_accept_states(self,line):
        exp = re.compile('\{[\d,]*\}',re.ASCII)
        if ('255' in line):
            return 1
        elif exp.match(line):
            return 0
        else:
            return 1
    # end def check_accept_states(self,line)








    # \fn def check_state_range
    # \purpose return 1 if there is an accept state outside of [0,254]
    def check_accept_state_range(self):
        for state in self.accept_states:
            # if it is an integer test it
            try:
                state = int(state)
            except ValueError as e:
                print("EXCEPTIONS: (%(state)s) couldn't be converted to int." %{'state':state})

            if(isinstance(state,int)):
                # if the state is out of range
                if state not in range(0,255):
                    print("State out of range: " + state)
                    return 1
                # end if state not in range(0,255)
            # Empty string is acceptable
            elif( len(state) != 0):
                print("State length bad: " + state + " len(state)= " + str(len(state)))
                return 1
        # end for state in self.accept_states
        return 0

    # end # \fn def check_state_range










    # \fn def check_dupe_tranisitons(self)
    # Return 1 if there is a duplicate value in the list of (current_state, symbol)
    def check_dupe_tranisitons(self):
        temp = []
        for t in self.transition_table:
            temp.append((t[0],t[1]))
        if( len(temp) != len(set(temp)) ):
            return 1
        else:
            return 0
    # end def check_dupe_tranisitons(self)








    # \fn def check_epsilon_transitions
    # \return epsilon_trans 1 if there are epsilon transitions, 0 otherwise
    def check_epsilon_transitions(self):
        for t in self.transition_table:
            for elt in t:
                if elt == '`':
                    return 1
        return 0
    # end def check_epsilon_transitions









    # \fn def check_empty_string_accept(self,in_string)
    # \brief Check if this is machine accepts the empty string
    # \return 1 if yes, 0 otherwise
    def check_empty_string_accept(self,in_string):
        if(in_string == '\n'):
            return 1
        else:
            return 0
    # end def check_empty_string_accept(self,in_string)









    # \fn def check_final_symbol_accept(self,in_char)
    # \purpose if the char doesn't transition to an accept state then the alphabet
    #          isn't worth processing.
    # Return 0 if the final symbol doesn't lead to an accept state
    #        1 otherwise
    def check_final_symbol_accept(self,in_string):
        for a_state in self.accept_states:
            # check each tuple to see if it leads to an accept state
            for delta in self.transition_table:
                if(a_state == delta[2]):
                    # If the tuple leads to an accept state check that the input
                    # character is in the "accept" tuple
                    # -2 because -1 is \n
                    if( in_string[len(in_string)-2] == delta[1]):
                        return 1
        # If no accept state then return 0, failure
        return 0
    # end def check_final_symbol_accept(self,in_char)









    # \fn def check_in_str_alphabet(self,in_str)
    # \purpose If any character in the string isn't in the alphabet stop processing
    # Return 1 if all characters in the alphabet
    #        0 if ANY character isn't in the alphabet
    def check_in_str_alphabet(self,in_string):
        for i in range(len(in_string)-1):
            # epsilon isn't in the alphabet, move on
            if( in_string[i] == '`'):
                pass
            elif in_string[i] not in self.alphabet:
                return 0
        return 1
    # end def check_in_str_alphabet(self,in_str)








    # \fn def check_transition_state_range(self)
    # return 1 if a transition goes outside of [0,255]
    def check_transition_state_range(self):
        for t in self.transition_table:
            if( int(t[0]) < 0 | int(t[0]) > 255 | int(t[2]) < 0 | int(t[2]) > 255):
                return 1
            return 0
    # end def check_transition_state_range(self)








    # \fn def fa_type()
    # \purpose the FA has been defined based on the file. Purpose
    #       current info to check the type
    # Cases:
    #   - (NFA) multiple transition rules with the same current_state and symbol
    #   - (NFA) epsilon transition rules, where '`' used
    #   - (INVALID) transitions from/to states not in [0,255]
    #   - (INVALID) accept states contain values not in [0,255)
    def fa_type(self):
        # FA may have been classified while reading in
        if (self.valid != ''):
            return None
        if( self.check_dupe_tranisitons() ):
            self.valid = 'NFA'
            self.valid_reason = 'Duplicate transition rules with the same (current_state,symbol)'
            return None
        if( self.check_epsilon_transitions() ):
            self.valid = 'NFA'
            self.valid_reason = "has '`' transition"
            return None
        if( self.check_transition_state_range() ):
            self.valid = 'INVALID'
            self.valid_reason = "Transition states not in [0,255]"
            return None
        if( self.check_accept_state_range() ):
            self.valid = 'INVALID'
            self.valid_reason = "Accept states not in [0,254]"
            return None

        self.valid = 'DFA'
        self.valid_reason = 'All checks for NFA/Invalid failed'
    # end def fa_type(self)






    # \fn def finalize_fa(self)
    # \brief Create an FA_Logger and call it on the FA
    # \param[out] Creates log and txt files for the FA
    def finalize_fa(self):
        me = FA_Logger()
        me.log_FA(self)
    # end def finalize_fa(self)





    # \fn def get_accepted_strings(self)
    # \brief gets the accepted strings.  Called from logger
    # \return strings the FA has accepted
    def get_accepted_strings(self):
        return self.accepted_strings
    # end def get_accepted_strings(self)






    # \fn def get_alphabet(self)
    # \brief gets the alphabet.  Called from logger
    # \return the FA alphabet
    def get_alphabet(self):
        return self.alphabet
    # end def get_alphabet(self)






    # \fn def e_set(self,symbol)
    # \brief Checks the transition table for entries that have (current state,
    #        symbol) and returns them.
    # \ return dupes set() of possible duplicates
    def get_dupe_set(self):
        dupes = set()
        for delta in self.transition_table:
            # Copy the table each time, and remove the current delta
            temp = self.transition_table.copy()
            temp.remove(delta)

            # Check delta against all other transitions
            for j in temp:
                for a in self.alphabet:
                    # Are the current states the same?
                    if( delta[0] == self.current_state):
                        if(j[0] == self.current_state ):
                            # Are the symbols the same?
                            if( delta[1] == a):
                                if(j[1] == a ):
                                    self.epsilon_trans.add(j)

    # end def get_dupe_set(self,symbol)






    # \fn def get_states(self)
    # \return the FA states
    def get_states(self):
        return self.states
    # end def get_states(self)






    # \fn def get_strings_processed(self)
    # \return the strings processed by the FA
    def get_strings_processed(self):
        return self.strings_processed
    # end def get_strings_processed(self)






    # \fn def get_classification(self)
    # \return the FA valid (DFA/NFA/INVALID)
    def get_valid(self):
        return self.valid
    # end def get_classification(self)






    # \fn def next_state_recurse(self,in_char)
    def next_state_recurse(self,in_str):
    #def next_state_recurse(self,in_str):
        # find the transition with the same state and symbol, then set the
        # the current state and call again
        if( len(in_str) - 1):
            for transition in self.transition_table:
                if self.current_state == transition[0]:
                    if transition[1] == in_str[0] :
                        self.current_state = transition[2]
                        break
            return self.next_state_recurse(in_str[1:])
        else:
            return 1
    # end def next_state_recurse(self,in_char)






    # \fn def print_self
    # Prints variables stored in the class
    def print_self(self):
        print("Current state:\t\t%(cs)s" %{'cs':self.current_state})
        print("From file:\t\t%(from_file)s" % {'from_file':self.from_file})
        print("Accept states:\t\t%(accept_states)s" % {'accept_states':self.accept_states})
        print("(%(count)d)Transitions:\t\t%(trans)s" % { 'count':len(self.transition_table)  ,'trans':self.transition_table})
        print("Alphabet:\t\t%(alphabet)s" % {'alphabet':self.alphabet})
        print("FA classification:\t\t%(classification)s" %{'classification':self.valid})
        print("FA classification reason:\t\t%(class_reason)s" %{'class_reason':self.valid_reason})
        print("epsilon-Transition functions: %(eps)s" %{'eps':str(self.epsilon_trans)})
        print("\n\n\n")
    # end def print_self(self)









    # \fn def process_def(self,filename)
    def process_def(self,from_file):
        self.from_file = from_file
        self.build_fa_from_file()   # Open a file and take a definition
        self.fa_type()              # What is the FA type?
        self.set_alphabet()         # What symbols are in the alphabet
        self.set_states()
        self.current_state = '0'    # after processing reset the current state
        self.get_dupe_set()         # create a set of all the duplicates
    # end def process_def(self,filename)









    # \fn def process_string(self,filename)
    # \purpose when given a string take the following actions
    # \param in_string string to be tested against FA definition
    # \ description Check if processing the empty string would result in success,
    #               if yes cease processing.
    #               Check that the final symbol in the string would lead to an
    #               accept state, cease processing if not.
    #               Check that the input string is in the acceptable alphabet,
    #               cease processing if not.
    #               Else advance through the states with next_state_recurse(symbol)
    #               and check that we're at an accept state after
    def process_string(self,in_string):
        self.strings_processed += 1 # update number of strings processed
        temp = in_string                # save a copy of the string for manip
        self.current_state = '0'        # Be sure to start from the start state

        # If in_string is empty string and accept states are null
        if( self.check_empty_string_accept(in_string) ):
            self.accepted_strings.append(in_string)
            return None


        # if the final symbol doesn't lead to an accept state stop processing, go to trap
        elif( self.check_final_symbol_accept(in_string) != 1 ):
            self.current_state = '255'
            return None


        # Stop processing the string if it has characters not in the alphabet, go to trap
        elif( self.check_in_str_alphabet(in_string) != 1 ):
            self.current_state = '255'
            return None

        # if the string doesn't immediately fail run it through the machine
        else:
            # Process the string to the final character
            if( self.next_state_recurse(temp) ):
                if( self.current_state in self.accept_states):
                    self.accepted_strings.append(in_string)
            # else string_rejected

    # end def process_string










    # \fn def set_accept_states(self,inStates:list)
    # \brief add list states to our list of transitions.  Dupes handled by set
    # @param in_states list of states
    def set_accept_states(self,in_states:list):
        for state in in_states:
            self.accept_states.add(state)
        # end for state in inStates
    # end def set_accept_states(self,inStates:list)









    # \fn def set_alphabet
    # \brief given the transition table read all input symbols and
    #       setup the alphabet for the FA
    def set_alphabet(self):
        for t in self.transition_table:
            if(t[1] != '`'):
                self.alphabet.add(t[1])
    # end def set_alphabet









    # \fn def set_states(self)
    # \brief Set the var:states
    def set_states(self):
        for t in self.transition_table:
            self.states.add(t[0])
            self.states.add(t[2])
        # 255 is in every FA by default
        self.states.add(255)
    # end def set_states(self)








    # \fn def set_transition(self,delta:tuple)
    # \brief add tuple t to our list of transitions.  Dupes handled by set
    def set_transition(self,delta:tuple):
        self.transition_table.add(delta)
    # end def set_transition(self,delta:tuple)





#end class FA
