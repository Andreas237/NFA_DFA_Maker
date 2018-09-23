# Running the code
Author: Andreas Slovacek
Date: 23 September 2018



## System Requirements
* Unix based OS
* Python 3.x
* Tested on OSX 10.13.4; Kali Gnu/Linux Rolling



## Knowing the the files
Please see *_./html/index.html_* for Doxygen generation. It is complete documentation.

Functions are listed in the order they are called.

### fa_master.py
Master script. Reads directories and passes definition files to FA constructor
and string processor

* `run(self)` calls sub-functions
  * `build_fas(self)` calls sub-function to scan directory for .fa files, then
    passes those to the FA constructor
  * `get_input_strings(self,input_file)` creates an iterable list of all strings
    from *input.txt*
  * Run then calls on each FA to `process_string()`


### finite_automaton.py
Implementation of NFA.  DFA functionality handled the same as the NFA, except
strings containing epsilon transitions aren't processed.

* `process_def(self,from_file)` set's up a Finite Automaton based on a .fa files
  definition.  
  * `fa_type()` determines the type of the FA by checking duplicate transitions,
    epsilon tranisitons, invalid accepts states, accept state range, state range
  * `set_alphabet()` extracts the alphabet from the transition table
  * `set_states()` extracts the states from the transition table
  * `get_dupe_set()` extracts duplicate transitions from the transition table

* `process_string(in_string)` used to test strings in the FA.  The current states
  is reset with every string processed.  IF-ELIF-ELSE finds reasons to cease
  processing. Otherwise process the string, check if it ended in an accept
  state, and save the string if it did.
  * `self.strings_processed` tracks how many strings this FA has processed
  * `next_state_recurse(in_str)` recursively processes the string and shifts
    states

* `finalize_fa()` Logs the FA values in results/basename.log and echos the
  accepted strings into results/basename.txt.  Called from `fa_master.py`

*  `print_self()` Call after `process_def` to print the FA to CLI


### fa_logger.py
Handles file and directory operations.

* `log_FA(FA)` Takes an FA as parameter, sets up and writes log files
  * `set_filenames(filename)` creates a directory for results if needed and
    sets directory/filenames for the .log and .txt file associated with this FA
  * `remove_previous_files()` deletes any existing .log and .txt files
  * `create_log_file(FA)` writes (Valid,States,Alphabet,Accepted Strings) to
    .log file with input parameter FA's member variables
  * `create_txt_file(FA)` writes accepted strings to .txt with input parameter
    FA's member variables


### cleanup.sh
Cleans residual *.log* and *.txt* files in PJ01/results



### code/
Contains the Python files

### results/
Contains the output *.log* and *.txt* files generated in fa_logger.py



# NFA_DFA_Maker
Finite Automaton creator and classifier based on *_PJ01.pdf_*

In this project you will write a program that will read a simplified description of a finite
automaton, validate it, and then simulate it on each string read from an input text file. Each
string that is accepted by the DFA will be echoed to a text file; in addition each machine will
have a log file prepared containing specific pieces of information.

To avoid operating-specific case-sensitivity issues, all filenames will be all lowercase. So that all
of the files can be in the same directory and the following naming conventions will be used:
* Base name: mxx where xx is a two digit number. The first machine will have a base name of m00 and the remaining machines will be numbered sequentially. This should allow you to write a wrapper program that processes all of the machines in a single run.
* Machine description file: basename.fa
* Accepted strings: basename.txt
* Log file: basename.log
* Input file: strings.txt (the same file for all machines)
