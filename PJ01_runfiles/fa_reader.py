# Import the structure of the FA
import FiniteAutomaton

file_prefix = 'made_up'

# Open the file for reading
with open(file_prefix+'.fa','r') as f:
    #TODO: instantiate a version of the FiniteAutomaton, set the accept and transitions vars
    #TODO: clean this file up s.t. it isn't a pile of print statements.  Write test fns for it
    #Read the first line as accept states
    line = f.readline()
    print("Accept states: ", (line.replace('{','').replace('\n','').replace('}','')).split(','))
    for line in f:
        trans = line.split(',')
        print("Transition:%(line)s     current_state:%(current_state)s    symbol:%(symbol)s    new_state:%(new_state)s"
                             %{'line':line,'current_state':trans[0],'symbol':trans[1],'new_state':trans[2]})



f.close()


print("Done")
