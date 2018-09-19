# Lessons Learned:
#   - setting parameter types for fns


from enum import Enum           # Enums for FA classification




# class delta
# Represents a transition function in the transition table
# Description:
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


# class FA:
# Description:
#   Finite Automaton
#   Needs list of accept states
#   Needs list of tuples of transition functions (deltas)
#   TODO: check that accept states are valid
class FA:
    accept_states       = set()     # accept_states read from .fa file
    alphabet            = set()     # alphabet of the input language
    classification      = ''        # classification of the FA (NFA, DFA, INVALID)
    current_state       = 0         # state the FA is currently in.  Default start 0
    from_file           = ''        # which .fa file defined this FA
    states              = set()     # set of states, derived from transition_table
    transition_table    = set()     # transition function tuples from FA file
    accepted_alphabets  = []        # alphabets accepted by this FA









    # Initialize self and var:from_file with the name of the file defining this FA
    def __init__(self, from_file):
        self.from_file = from_file









    # Return the var:accept_states
    def get_accept_states(self):
        return self.accept_states









    # Return the var:classification
    def get_classification(self):
        return self.classification









    # Return var:from_file
    def get_from_file(self):
        return self.from_file









    # Return the var:transition_table
    def get_transition_table(self):
        return self.transition_table









    # add list states to our list of transitions.  Dupes handled by set
    def set_accept_states(self,inStates:list):
        for state in inStates:
            self.accept_states.add(state)









    # Set the var:classification
    def set_classification(self, classification:str):
        self.classification = classification









    # Set the var:states
    def set_states(self):
        for t in self.transition_table:
            print(self.from_file + str(t))
            self.states.add(t[0])
            self.states.add(t[2])








    # add tuple t to our list of transitions.  Dupes handled by set
    def set_transition(self,delta:tuple):
        self.transition_table.add(delta)









    # If there is a duplicate value in the list of (current_state, symbol)
    # then this is an NFA
    def check_NFA(self):
        temp = []
        for t in self.transition_table:
            temp.append((t[0],t[1]))
        if( len(temp) == len(set(temp)) ):
            return 0
        else:
            return 1
    # end def check_NFA(self)









    # def print_self
    # Prints variables stored in the class
    def print_self(self):
        print("From file:\t\t%(from_file)s" % {'from_file':self.get_from_file()})
        print("Accept states:\t\t%(accept_states)s" % {'accept_states':self.get_accept_states()})
        print("Transitions:\t\t%(trans)s" % {'trans':self.get_transition_table()})
        print("FA classification:\t\t%(classification)s" %{'classification':self.classification})
        print("\n\n\n")
    # end def print_self(self)









    # def process(self)
    # Purpose:
    #   TODO: get this list of states
    #   TODO: determine what type of FA this is
    def process(self):
        self.set_states()
        self.typeCheck_FA()






    # def reset_self
    # Purpose: reset the object to accept another string
    def reset_self(self):
        self.alphabet.clear()
        self.classification         = ''
        self.current_state          = 0
        # accept_states       = set()       # Taken from FA definition, don't change
        # self.from_file           = ''     # Taken from FA definition, don't change
        # states              = set()       # set of states, derived from transition_table
        # transition_table    = set()       # Taken from FA definition, don't change
        print("%(name)s\t\tSTATUS=RESET" % {'name':self.from_file} )






    # def string_processor
    # Purpose: takes a string and tests it agains the FA







    # def typeCheck_FA(self)
    # Purpose: fill in FA type of (NFA, DFA, INVALID)
    # Invalid checked when the file is read in, hence return None if already set
    #   validate_transitions checks whether transitions are valid
    # NFA and DFA checked here.
    # NFA's: indicated with '`', or multiple to states for a current_state, symbol combo
    # DFA: if it is a valid FA, and it isn't an NFA it is a DFA
    # INVALID: if the first line doesn't have any accept states, or is in bad format
    def typeCheck_FA(self):
        if (self.classification != ''):
            return None

        # Check if accept states in range [0,254]
        for state in self.accept_states:
            if int(state) > 254:
                print("State out of range: " + state)
                return 1
            elif int(state) < 0:
                print("State out of range: " + state)
                return 1
        # end for state in self.accept_states

        # Check each transition for epsilon characters
        for t in self.transition_table:
            for elt in t:
                if elt == '`':
                    self.classification = 'NFA'
                    return
            # end for elt in t
        # end for t in self.transition_table

        # Check for repeated (current_state,symbol) which indicates NFA
        if(self.check_NFA()):
            self.classification = 'NFA'
        # If all else fails it is a DFA
        else:
            self.classification = 'DFA'
    # end def typeCheck_FA(self)









    # def validate_transitions(self)
    # Purpose: check that each element in the transition functions
    #   is a valid ASCII character
    def validate_transitions(self):

        for tup in self.transition_table:
            for elt in tup:
                isascii = lambda s: len(s) == len(s.encode())
                print("Type: %(t)s" %{'t':isascii } )
