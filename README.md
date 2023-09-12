# An Airbnb clonning project
# we are starting with the console portion of the project. A console is a control panel where commands run through, for there to be any form of interraction between user and the app.


# We shall start creating the console by creating the command line interpreter. Which works like the shell terminal. The CMD line intepreter will be created using cmd.Cmd method. By importing cmd.

# What we build during this project will be used when we shall be doing HTML/CSS, templating, database storage, API, front-end intergration...

# the tasks:
	# Creare a BaseModel
	# Create a serialization/deserialization
	# Create Classes: (User, State, City, Place ...)
	# Create the first abstracted storage engine (File Storage)
	# Create unittests to validate the Classes and Storage Engine

# this is the code for creating the command line interpreteri:

import cmd

class Airbnb1cmd(cmd.Cmd):
	prompt = "(AirbnbJM) "

Airbnb1cmd().cmdloop()


# the command line Interprettershouls be able to:
	# Create a new object (New use, New Place)
	# Retrieve an object from a file, a database etc...
	# Do operations on objects (Count, compute stats, etc...)
	# Update attributes of an object
	# Destroy an object
