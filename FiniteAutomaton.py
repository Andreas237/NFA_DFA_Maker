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
    accept_states       = set()
    classification      = ''
    current_state       = 0
    transition_table    = set()
    from_file           = ''


    def __init__(self, from_file):
        self.from_file = from_file


    def get_accept_states(self):
        return self.accept_states

    def get_from_file(self):
        return self.from_file

    def get_transition_table(self):
        return self.transition_table

    # add list states to our list of transitions.  Dupes handled by set
    def set_accept_states(self,inStates:list):
        for state in inStates:
            self.accept_states.add(state)

    def set_classification(self, classification):
        self.classification = classification


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

    def print_self(self):
        print("From file:\t\t%(from_file)s" % {'from_file':self.get_from_file()})
        print("Accept states:\t\t%(accept_states)s" % {'accept_states':self.get_accept_states()})
        print("Transitions:\t\t%(trans)s" % {'trans':self.get_transition_table()})
        print("FA classification:\t\t%(classification)s" %{'classification':self.classification})


    # def typeCheck_FA(self)
    # Represents the type of FA (NFA, DFA, INVALID)
    # NFA's: indicated with '`', or multiple to states for a current_state, symbol combo
    # DFA: if it is a valid FA, and it isn't an NFA it is a DFA
    # INVALID: if the first line doesn't have any accept states, or is in bad format
    def typeCheck_FA(self):
        for t in self.transition_table:
            for elt in t:
                if elt == '`':
                    self.classification = 'NFA'
                    return
        if(self.check_NFA()):
            self.classification = 'NFA'
        else:
            self.classification = 'DFA'
