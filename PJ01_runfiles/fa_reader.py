# Import the structure of the FA
from FiniteAutomaton import FA

file_prefix = 'made_up'

# Open the file for reading
with open(file_prefix+'.fa','r') as f:

    #TODO: instantiate a version of the FiniteAutomaton, set the accept and transitions vars
    fa = FA()

    # Get the fist line, accept states, turn it into a list, and set accept_states in the FA
    fa.set_accept_states((f.readline()).replace('{','').replace('\n','').replace('}','').split(','))

    #TODO: check that the contents of the transition table are validself
    #TODO: finish "plant of attack" in sketchpad
    for line in f:
        line.replace('\n','')
        fa.set_transition(tuple(line.split(',')))





print("Accept states: %(accept_states)s" % {'accept_states':fa.get_accept_states()}) # correctly
print("Accept: %(state)s" % {'state':fa.accept_states.pop()}) # member access to states
print("Transitions: %(trans)s" % {'trans':fa.get_transition_table()})


f.close()


print("Done")
