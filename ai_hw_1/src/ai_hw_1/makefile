#
# A simple makefile for compiling three java classes
#

# define a makefile variable for the java compiler
#
JCC = javac

# define a makefile variable for compilation flags
# the -g flag compiles with debugging information
#
JFLAGS = -g

# typing 'make' will invoke the first target entry in the makefile 
# (the default one in this case)
#
default: main.java Problem.java State.java

# this target entry builds the main class
# the main.class file is dependent on the main.java file
# and the rule associated with this entry gives the command to create it
# main.class: main.java
		$(JCC) $(JFLAGS) main.java

Problem.class: Problem.java
		$(JCC) $(JFLAGS) Problem.java

State.class: State.java
	$(JCC) $(JFLAGS) State.java

# To start over from scratch, type 'make clean'.  
# Removes all .class files, so that the next make rebuilds them
#
clean: 
		$(RM) *.class