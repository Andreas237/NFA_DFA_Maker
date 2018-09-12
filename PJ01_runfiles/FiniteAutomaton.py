from enum import Enum
import hashlib


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
class FA:
    accept_states       = set()
    classification      = Enum('classification','NFA DFA INVALID')
    current_state       = 0
    transition_table    = set()


    def __init__(self, nameIn="FA"):
        self.name = nameIn

    def get_accept_states(self):
        return self.accept_states

    def get_transition_table(self):
        return self.transition_table

    # add tuple t to our list of transitions.  Dupes handled by set
    def set_transition(self,delta:tuple):
        self.transition_table.add(delta)

    # add list states to our list of transitions.  Dupes handled by set
    def set_accept_states(self,inStates:list):
        for state in inStates:
            self.accept_states.add(state)
