# Lessons Learned:
#   - setting parameter types for fns
#   - variables set outside of __init__, e.g. below 'class NAME: var=1' are class variables
#       and thus keep their values from one instance to the next.
#   - __init__ vars are instance variables and change with each instantiation


##################################################################################
#-----------------      IMPORT FILES
import os                       # Open files in a directory
import re                       # regex first line for validation













##################################################################################
#-----------------      CLASS: DELTA
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


#end class delta













##################################################################################
#-----------------      CLASS: FA
# class FA:
# Description:
#   Finite Automaton
#   Needs list of accept states
#   Needs list of tuples of transition functions (deltas)
class FA:








    # def __init__(self)
    def __init__(self):
        self.accept_states       = set()     # accept_states read from .fa file
        self.accepted_alphabets  = []        # alphabets accepted by this FA
        self.alphabet            = set()     # alphabet of the input language
        self.classification      = ''        # classification of the FA (NFA, DFA, INVALID)
        self.class_reason        = ''        # why this classification?
        self.current_state       = 0         # state the FA is currently in.  Default start 0
        self.from_file           = ''        # which .fa file defined this FA
        self.states              = set()     # set of states, derived from transition_table
        self.transition_table    = set()     # transition function tuples from FA file
    # def __init__(self)









    # def build_fa_from_file(self)
    def build_fa_from_file(self):
        try:
            with open(self.from_file,'r') as f:
                # Create an FA at the next index
                line = f.readline()

                # If the first line is invalid cease processing
                if self.check_accept_states(line) == 1:
                    self.set_classification = 'INVALID'
                    self.class_reason = 'Bad accept states in file'
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
                #TODO: replace fa.process() with a function call after it is built

        # If the file can't be opened notify
        except PermissionError:
            print("Couldn't open %(f)s" % {'f':filename} )

        except FileNotFoundError:
            print("%(f)s doesn't exist!" % {'f':filename} )

        # If no errors add the FA to the list and close the file
        else:
            f.close()
    # end def build_fa_from_file(self)







    # def check_accept_states(self,line)
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








    # def check_state_range
    # Purpose: return 1 if there is an accept state outside of [0,254]
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

    # end # def check_state_range









    # def check_dupe_tranisitons(self)
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








    # def check_epsilon_transitions
    # return 1 if there are epsilon transitions, 0 otherwise
    def check_epsilon_transitions(self):
        for t in self.transition_table:
            for elt in t:
                if elt == '`':
                    return 1
        return 0
    # end def check_epsilon_transitions








    # def check_transition_state_range(self)
    # return 1 if a transition goes outside of [0,255]
    def check_transition_state_range(self):
        for t in self.transition_table:
            if( int(t[0]) < 0 | int(t[0]) > 255 | int(t[2]) < 0 | int(t[2]) > 255):
                return 1
            return 0
    # end def check_transition_state_range(self)








    # def fa_type()
    # Purpose: the FA has been defined based on the file. Purpose
    #       current info to check the type
    # Cases:
    #   - (NFA) multiple transition rules with the same current_state and symbol
    #   - (NFA) epsilon transition rules, where '`' used
    #   - (INVALID) transitions from/to states not in [0,255]
    #   - (INVALID) accept states contain values not in [0,255)
    def fa_type(self):
        # FA may have been classified while reading in
        if (self.classification != ''):
            return None
        if( self.check_dupe_tranisitons() ):
            self.classification = 'NFA'
            self.class_reason = 'Duplicate transition rules with the same (current_state,symbol)'
            return None
        if( self.check_epsilon_transitions() ):
            self.classification = 'NFA'
            self.class_reason = "has '`' transition"
            return None
        if( self.check_transition_state_range() ):
            self.classification = 'INVALID'
            self.class_reason = "Transition states not in [0,255]"
            return None
        if( self.check_accept_state_range() ):
            self.classification = 'INVALID'
            self.class_reason = "Accept states not in [0,254]"
            return None

        self.classification = 'DFA'
        self.class_reason = 'All checks for NFA/Invalid failed'
    # end def fa_type(self)






    # def print_self
    # Prints variables stored in the class
    def print_self(self):
        print("From file:\t\t%(from_file)s" % {'from_file':self.from_file})
        print("Accept states:\t\t%(accept_states)s" % {'accept_states':self.accept_states})
        print("(%(count)d)Transitions:\t\t%(trans)s" % { 'count':len(self.transition_table)  ,'trans':self.transition_table})
        print("FA classification:\t\t%(classification)s" %{'classification':self.classification})
        print("FA classification reason:\t\t%(class_reason)s" %{'class_reason':self.class_reason})
        print("\n\n\n")
    # end def print_self(self)









    # def process(self,filename)
    def process(self,from_file):
        self.from_file = from_file
        self.build_fa_from_file()
        self.fa_type()
        #self.print_self()
    # end def process(self,filename)









    # def process(self,filename)
    def process_test(self,from_file):
        self.from_file = from_file
        self.build_fa_from_file()
        self.fa_type()
        self.print_self()
    # end def process(self,filename)










    # add list states to our list of transitions.  Dupes handled by set
    def set_accept_states(self,inStates:list):
        for state in inStates:
            self.accept_states.add(state)
        # end for state in inStates
    # end def set_accept_states(self,inStates:list)









    # Set the var:states
    def set_states(self):
        for t in self.transition_table:
            self.states.add(t[0])
            self.states.add(t[2])
        # 255 is in every FA by default
        self.states.add(255)
    # end def set_states(self)








    # add tuple t to our list of transitions.  Dupes handled by set
    def set_transition(self,delta:tuple):
        self.transition_table.add(delta)
    # end def set_transition(self,delta:tuple)





#end class FA












##################################################################################
#-----------------      TEST RUN

file_prefix = 'm'                               # prefix of FA definition files
file_suffix = '.fa'                             # suffix of FA definition files
file_dir    = 'PJ01_runfiles/'                  # subdirectory of FA definition files

def test_run(count:int):
    x = FA()
    files = []
    if( count <= 1):
        x.process_test("PJ01_runfiles/m09.fa")
    else:

        for i in range(count):
            #build the filename, then run it
            filename = file_dir + file_prefix
            if( i < 10):
                filename = filename + str(0) + str(i)
            else:
                filename = filename + str(i)
            filename = filename + file_suffix
            x.process_test(filename)
            files.append(filename)

    print("CREATED %(n)d FAs\n" % { 'n':len(files) })
    print("FROM FILES %(fs)s\n" % { 'fs':files })

##################################################################################

x = FA()
x.process_test("PJ01_runfiles/m02.fa")
y = FA()
y.process_test("PJ01_runfiles/made_up.fa")
x = FA()
x.process_test("PJ01_runfiles/m01.fa")
x = FA()
x.process_test("PJ01_runfiles/m00.fa")
x = FA()
x.process_test("PJ01_runfiles/m03.fa")
#test_run(4)
