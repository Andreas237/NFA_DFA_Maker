# Running the code
? What do I need to run it?
? What directory is it in?
? What is the file to execute, what inputs?
? Where does everything happen?
? What are the other files

# NFA_DFA_Maker
Finite Automaton creator and classifier based on PJ01.pdf

In this project you will write a program that will read a simplified description of a finite
automaton, validate it, and then simulate it on each string read from an input text file. Each
string that is accepted by the DFA will be echoed to a text file; in addition each machine will
have a log file prepared containing specific pieces of information.

Undergraduate students are only responsible for being able to process deterministic machine
descriptions, while graduate students must also be able to process nondeterministic machine
descriptions. However, all students will receive the same set of machines, so undergraduates
will need to be able to determine whether a machine is deterministic or not.

To avoid operating-specific case-sensitivity issues, all filenames will be all lowercase. So that all
of the files can be in the same directory and the following naming conventions will be used:
* Base name: mxx where xx is a two digit number. The first machine will have a base name of m00 and the remaining machines will be numbered sequentially. This should allow you to write a wrapper program that processes all of the machines in a single run.
* Machine description file: basename.fa
* Accepted strings: basename.txt
* Log file: basename.log
* Input file: strings.txt (the same file for all machines)
