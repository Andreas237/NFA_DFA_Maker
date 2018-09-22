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
    def get_delta(self):
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
    def __init__(self):
        self.accept_states       = set()     # accept_states read from .fa file
        self.accepted_strings    = []        # Strings that reached an "accept" state
        self.alphabet            = set()     # alphabet of the input language
        self.valid      = ''                 # classification of the FA (NFA, DFA, INVALID)
        self.valid_reason        = ''        # why this classification?
        self.current_state       = '0'         # state the FA is currently in.  Default start 0
        self.from_file           = ''        # which .fa file defined this FA
        self.states              = set()     # set of states, derived from transition_table
        self.strings_processed   = 0
        self.transition_table    = set()     # transition function tuples from FA file
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









    # \fn def check_final_symbol_accept(self,in_char)
    # \purpose if the char doesn't transition to an accept state then the alphabet
    #          isn't worth processing.
    # Return 0 if the final symbol doesn't lead to an accept state
    #        1 otherwise
    def check_final_symbol_accept(self,in_char):
        for a_state in self.accept_states:
            # check each tuple to see if it leads to an accept state
            for delta in self.transition_table:
                if(a_state == delta[2]):
                    # If the tuple leads to an accept state check that the input
                    # character is in the "accept" tuple
                    if( in_char == delta[1]):
                        return 1
        # If no accept state then return 0, failure
        return 0
    # end def check_final_symbol_accept(self,in_char)









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









    # \fn def check_final_symbol_accept(self,in_char)
    # \purpose if the char doesn't transition to an accept state then the alphabet
    #          isn't worth processing.
    # Return 0 if the final symbol doesn't lead to an accept state
    #        1 otherwise
    def check_final_symbol_accept(self,in_char):
        for a_state in self.accept_states:
            # check each tuple to see if it leads to an accept state
            for delta in self.transition_table:
                if(a_state == delta[2]):
                    # If the tuple leads to an accept state check that the input
                    # character is in the "accept" tuple
                    if( in_char == delta[1]):
                        return 1
        # If no accept state then return 0, failure
        return 0
    # end def check_final_symbol_accept(self,in_char)









    # \fn def check_in_str_alphabet(self,in_str)
    # \purpose If any character in the string isn't in the alphabet stop processing
    # Return 1 if all characters in the alphabet
    #        0 if ANY character isn't in the alphabet
    def check_in_str_alphabet(self,in_str):
        for c in in_str:
            # epsilon isn't in the alphabet!
            if( c == '`'):
                a = 1
            elif c not in self.alphabet:
                #print('WARNING: ' + c + ' NOT in alphabet')
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
    def finalize_fa(self):
        me = FA_Logger()
        me.log_FA(self)
    # end def finalize_fa(self)





    # \fn def get_accepted_strings(self)
    def get_accepted_strings(self):
        return self.accepted_strings
    # end def get_accepted_strings(self)






    # \fn def get_alphabet(self)
    def get_alphabet(self):
        return self.alphabet
    # end def get_alphabet(self)






    # \fn def get_states(self)
    def get_states(self):
        return self.states
    # end def get_states(self)






    # \fn def get_strings_processed(self)
    def get_strings_processed(self):
        return self.strings_processed
    # end def get_strings_processed(self)






    # \fn def get_classification(self)
    def get_valid(self):
        return self.valid
    # end def get_classification(self)






    # \fn def next_state(self,in_char)
    # \purpose
    #   Advance the machine's current state based on the character input and
    #   the current state
    def next_state(self,in_char):
        # for each transition in the table, if the t[0] == current state
        # TODO: if transition isn't included send to trap state
        for transition in self.transition_table:
            if self.current_state == transition[0]:
                if transition[1] == in_char :
                    print("Move from %(curr)s to %(next)s with symbol %(sy)s!" % {'curr':self.current_state,'sy':in_char, 'next':transition[2]} )
                    self.current_state = transition[2]
                    return None

            # if t[1] == in_char then set the current_state to t[2]
    # end def next_state(self,in_char)






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
        print("\n\n\n")
    # end def print_self(self)









    # \fn def process_def(self,filename)
    def process_def(self,from_file):
        self.from_file = from_file
        self.build_fa_from_file()   # Open a file and take a definition
        self.fa_type()              # What is the FA type?
        self.set_alphabet()         # What symbols are in the alphabet
        self.current_state = '0'      # after processing reset the current state
        # self.print_self()
    # end def process_def(self,filename)









    # \fn def process_string(self,filename)
    # \purpose when given a string take the following actions
    # \param in_string string to be tested against FA definition
    def process_string(self,in_string):


        self.strings_processed = self.strings_processed + 1 # update number of strings processed
        temp = in_string                # save a copy of the string for manip
        self.current_state = '0'        # Be sure to start from the start state


        # If in_string is empty string and accept states are null
        if( len(in_string) == 0  & len(self.accept_states)):
            print("ACCEPTED STRING: (" + in_string + ")")
            self.accepted_strings.append(in_string)


        # if the final symbol doesn't lead to an accept state stop processing, go to trap
        elif( self.check_final_symbol_accept(in_string[len(in_string)-1]) != 1 ):
            print("Final symbol doesn't lead to accept - trap")
            self.current_state = '255'
            return None


        # Stop processing the string if it has characters not in the alphabet, go to trap
        elif( self.check_in_str_alphabet(in_string) != 1 ):
            print("chars not in alphabet - trap")
            self.current_state = '255'
            return None

        # if the string doesn't immediately fail run it through the machine
        else:
            # Process the string to the final character
            while( temp ):
                self.next_state(temp[0])
                temp = temp[1:]

            # if the current_state is in the accept states then string_accepted
            if( self.current_state in self.accept_states):
                print("ACCEPTED STRING: (" + in_string + ")")
                self.accepted_strings.append(in_string)
            else:
                print("REJECTED STRING")
            # else string_rejected
        print('Process %(in)d strings so far.  Accepted %(ac)d\n' % {'ac':len(self.accepted_strings), 'in':self.strings_processed })
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








    # \fn def string_accept(self,in_string)
    # This string has been accepted!  Add it to the accepted strings list





#end class FA












##################################################################################
#-----------------      TEST RUN
##################################################################################

#x = FA()
#x.process_def("PJ01_runfiles/m02.fa")
#x = FA()
#x.process_def("PJ01_runfiles/m01.fa")
#x = FA()
#x.process_def("PJ01_runfiles/m00.fa")
#x = FA()
#x.process_def("PJ01_runfiles/m03.fa")



#y = FA()
#y.process_def("PJ01_runfiles/made_up.fa")
#y.process_string('1a` ')
#y.process_string('1a`34  ')
#y.process_string('1a`43 ')
#y.process_string('1a1`0 1 b a')
#y.finalize_fa()
