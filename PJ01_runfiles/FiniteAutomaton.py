from enum import Enum

class FA:
    accept_states   = []
    classification  = Enum('classification','NFA DFA INVALID')
    current_state   = 0
    transitions     = []

    def __init__(self, nameIn):
        self.name = nameIn

    def set_accept_state(self,states):
        self.accept_states = states

    def log_accept_states(self):
        print(self.accept_states)
